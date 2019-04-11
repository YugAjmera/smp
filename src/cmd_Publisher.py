#!/usr/bin/env python

import rospy
from geometry_msgs.msg import Twist

rospy.init_node('cmd_Publisher')
pub = rospy.Publisher('turtle1/cmd_vel', Twist, queue_size=10)

rate=rospy.Rate(2)

vel = Twist()

vel.linear.x=2.0
vel.linear.y=0.0
vel.linear.z=0.0

vel.angular.x=0.0
vel.angular.y=0.0
vel.angular.z=1.8

while not rospy.is_shutdown():
	pub.publish(vel)
	rate.sleep()



