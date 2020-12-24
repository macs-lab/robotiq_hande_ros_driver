#!/usr/bin/env python
import rospy
from std_msgs.msg import Int32
from robotiq_hande_ros_driver.srv import gripper_service

rospy.init_node("gripper_test_node")

## using ROS service
rospy.loginfo("using service")
gripper_srv = rospy.ServiceProxy('gripper_service', gripper_service)
# open gripper
response = gripper_srv(position=0, speed=255, force=255)
# close gripper
response = gripper_srv(position=255, speed=255, force=255)
# open gripper small speed
response = gripper_srv(position=0, speed=55, force=255)
# close gripper small speed
response = gripper_srv(position=255, speed=55, force=255)
# open gripper small speed and force 
response = gripper_srv(position=100, speed=5, force=5)
# close gripper small speed and force
response = gripper_srv(position=150, speed=5, force=5)