# neccessary packages
import rospy                             
from inverted_pendulum_sim.msg import ControlForce        
from math import sin, pi

rospy.init_node('goal2')  #node       
pub = rospy.Publisher('/inverted_pendulum/control_force', ControlForce, queue_size=10)  #publisher                            

rate = rospy.Rate(100)   #frequency of node set to 100 hz           
force_obj = ControlForce()                            
force_obj.force = 0
frequency = 10   #frequncy
amplitude = 30   #amplitude               
t = 0 #time

while not rospy.is_shutdown():             
  pub.publish(force_obj)
  t += 0.001
  force_obj.force = amplitude*sin(2*pi*frequency*t)   # y(t) = Asin(2πft+φ)
  rate.sleep()        
 
                    
