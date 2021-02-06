#Projectile-Motion-with-Multiple objects-using python preprocessor

#Data
begin : data;
	problem : initial value;
end : data;

#beginpreprocess
from __future__ import print_function, division
from MBDynLib import *
import random
ConstMBVar('Node_ball' , 'integer', 1)
ConstMBVar('Body_ball' , 'integer', 1)
ConstMBVar('Vy', 'real', random.randint(0,5))
ConstMBVar('Vz', 'real', random.randint(0,5))
ConstMBVar('M', 'real' , 10)
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
    structural nodes : 1;
    rigid bodies : 1;
    gravity;
end : control data;
#----------------------------------------------------------
# Node Data declaration
begin : nodes;
    structural : Node_ball,dynamic,null,eye,0.,Vy,Vz,null;
end : nodes;
#-----------------------------------------------------------
# Body Data declaration
begin : elements;
    body : Body_ball,Node_ball,M,null,eye;
    gravity : 0.,0.,-1.,const,9.81;
end : elements;
