begin: data;
   problem: initial value;
end: data;

begin: initial value;
   initial time:   0.;
   final time:     5.;
   time step:      1.e-3;
   max iterations: 10;
   tolerance:      1.e-6;
end: initial value;

#beginpreprocess
from __future__ import print_function, division
from MBDynLib import *
from math import pi

ConstMBVar('M', 'real', 1.0)
ConstMBVar('L', 'real', 1.0)

ConstMBVar('N', 'integer', 5)
for i in range(N):
  ConstMBVar('theta' + str(i), 'real', pi/N)

#endpreprocess

begin: control data;
   structural nodes: N;
   rigid bodies:     N;
   joints:           N;
   gravity;
end: control data;

#beginpreprocess

for i in range(N):
  ConstMBVar('Ref_Link' + str(i), 'integer', i)
  
for i in range(N):
  ConstMBVar('Node_Link' + str(i), 'integer', i)
  
for i in range(N):
  ConstMBVar('Body_Link' + str(i), 'integer', i)
  

ConstMBVar('JoRevp_Link0', 'integer', 0)
for i in range(N-1):
  ConstMBVar('JoRevh_Link'+str(i)+'_Link'+str(i+1), 'integer',i+1)
  
nodes = []
bodies = []
refs = []
joints=[]
#endpreprocess

reference: Ref_Link0,
   null,                        # absolute position
   euler, 0., pi/2.-theta0, 0., # absolute orientation
   null,                        # absolute velocity
   null;
   
#beginpreprocess
for i in range(1,N):
	RelRefPos = Position('Ref_Link'+str(i-1), "L, 0., 0.")
	RelRefOri = Position('Ref_Link'+str(i-1), "euler, 0., -theta"+str(i)+", 0.")
	RelRefVel = Position('Ref_Link'+str(i-1), null())
	refs.append(Reference('Ref_Link'+str(i), RelRefOri, RelRefVel, RelRefVel, RelRefPos))

	

#endpreprocess

#beginpreprocess
[print(d) for d in refs]
#endpreprocess

#beginpreprocess
for i in range(N):
	RelNodePos = Position('Ref_Link'+str(i), "1./2.*L, 0., 0.")
	RelNodeOri = Position('Ref_Link'+str(i), eye())
	RelNodeVel = Position('Ref_Link'+str(i), null())
	nodes.append(DynamicNode('Node_Link'+str(i), RelNodePos, RelNodeOri, RelNodeVel, RelNodeVel))

for i in range(N):
	RelBodyPos = Position('', null())
	bodies.append(Body('Body_Link'+str(i), nodes[i].idx, 'M', RelBodyPos, ['diag,' ' 0.,' ' M*L^2./12.,' ' M*L^2./12.']))
	
for i in range(N-1):
   RefNull = Position('', null())
   joints.append(JointRH('JoRevh_Link'+str(i)+'_Link'+str(i+1), 'Node_Link'+str(i), 'Node_Link'+str(i+1), 'Ref_Link'+str(i+1), "1, 1., 0., 0., 3, 0., 1., 0.",RefNull))

#endpreprocess


begin: nodes;

#beginpreprocess
[print(d) for d in nodes]
#endpreprocess

end: nodes;

begin: elements;

#beginpreprocess
[print('\t',d) for d in bodies]
#endpreprocess

 joint: JoRevp_Link0, 
      revolute pin, 
         Node_Link0, 
            reference, Ref_Link0, null,                                # relative offset
            hinge, reference, Ref_Link0, 1, 1., 0., 0., 3, 0., 1., 0., # relative axis orientation
            reference, Ref_Link0, null,                                # absolute pin position
            hinge, reference, Ref_Link0, 1, 1., 0., 0., 3, 0., 1., 0.; # absolute pin orientation

#beginpreprocess
[print('\t',d) for d in joints]
#endpreprocess

    
   gravity: 0., 0., -1., const, 9.81;
   
end: elements;
