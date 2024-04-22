#!/usr/bin/env python
import rospy
from std_msgs.msg import String
from geometry_msgs.msg import Twist


def calculate_w_ang(V_lin, W_ang):
    L = 20
    N = 8
    wheel_radius = 0.2
    lengths_seq = [-L/2, -3*L/8, -L/4, -L/8, L/8, L/4, 3*L/8, L/2]
    i = 1
    print(f'Cmd is:\t V linear = {V_lin:.2f} \t W angular = {W_ang:.2f}')

    for l in lengths_seq:
        w = (V_lin + W_ang * l) /wheel_radius
        print(f'w{i:.2f} = \t {w:.2f}')
        i+=1
    print("")


def callback(msg: Twist):
    calculate_w_ang(msg.linear.x,msg.angular.z)
    
def listener():
    rospy.init_node('cmd_converter', anonymous=True)
    rospy.Subscriber("cmd_vel", Twist, callback)
    rospy.spin()

if __name__ == '__main__':
    listener()
