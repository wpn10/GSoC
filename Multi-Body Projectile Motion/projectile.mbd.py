#Projectile-Motion-with-Multiple objects-using python preprocessor

#Data
begin : data;
	problem : initial value;
end : data;

#beginpreprocess
from __future__ import print_function, division
from MBDynLib import *
import random
ConstMBVar('N', 'integer', 10)
for i in range(N):
  ConstMBVar('NODE_' + str(i), 'integer', i)
  ConstMBVar('BODY_' + str(i), 'integer', i)
  ConstMBVar('Vy_' + str(i), 'integer', random.randint(0,5))
  ConstMBVar('Vz_' + str(i), 'integer', random.randint(0,5))

ConstMBVar('M', 'real' , 10)
RelNodeNull = Position('', null())
RelNodeEye = Position('', eye())


nodes = []
bodies = []
#endpreprocess


# Initial values declaration 
begin : initial value;
    initial time : 0.;
    final time : 1.;
    timestep : 1.e-3;
    max iterations : 10;
    tolerance : 1.e-6;
end : initial value;


# Control Data declaration
begin : control data;
    structural nodes : N;
    rigid bodies : N;
    gravity;
end : control data;

#beginpreprocess
for i in range(N):
  nodes.append(DynamicDisplacementNode('NODE_' + str(i), Position('', [0, 0, 0]), Position('', [0, 'Vy_' + str(i), 'Vz_' + str(i)])))
  bodies.append(PointMass('BODY_' + str(i), nodes[i].idx, M))
#endpreprocess

begin: nodes;
#beginpreprocess
[print(n) for n in nodes]
#endpreprocess
end: nodes;


begin:elements;
#beginpreprocess
[print(b) for b in bodies]
#endpreprocess
gravity : 0.,0.,-1.,const,9.81;
end: elements;

# vim:ft=mbd
