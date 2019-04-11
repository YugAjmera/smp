#!/usr/bin/env python
import rospy

from turtlesim.msg import Pose

def callback(msg):
	print msg.x

rospy.init_node('Sub_Node')
sub = rospy.Subscriber('/turtle1/pose', Pose, callback)
rospy.spin()
