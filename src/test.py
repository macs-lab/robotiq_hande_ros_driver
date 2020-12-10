#!/usr/bin/env python
import rospy
from std_msgs.msg import Int32
from robotiq_hande_ros_driver.srv import gripper_service

rospy.init_node("gripper_test_node")

## using ROS topics
rospy.loginfo("using topics")
pub = rospy.Publisher("gripper_command", Int32, queue_size=10)
# open gripper
msg = Int32()
msg.data = 1
pub.publish(msg)
rospy.sleep(2)
# close gripper
msg.data = 0
pub.publish(msg)
rospy.sleep(2)

## using ROS service
rospy.loginfo("using service")
gripper_srv = rospy.ServiceProxy('gripper_service', gripper_service)
# open gripper
response = gripper_srv(1)
# close gripper
response = gripper_srv(0)


