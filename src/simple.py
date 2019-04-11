#!/usr/bin/env python

import rospy

rospy.init_node('Node_1')
rate=rospy.Rate(2)

while not rospy.is_shutdown():
	print "Hello World"
	rate.sleep()

