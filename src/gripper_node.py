#!/usr/bin/env python

import rospy 
from std_msgs.msg import Int32
import robotiq_gripper
from robotiq_hande_ros_driver.srv import gripper_service, gripper_serviceResponse

class HandEGripper:
    def __init__(self):
        rospy.init_node("hand_e_gripper_node", anonymous=False)
        # get the IP
        ip = rospy.get_param('~robot_ip')
        # initialize the gripper
        self.gripper = robotiq_gripper.RobotiqGripper()
        rospy.loginfo("Connecting to the gripper.....")
        self.gripper.connect(ip, 63352)
        rospy.loginfo("Activating the gripper.....")
        self.gripper.activate(auto_calibrate=False)
        # set up server
        self.gripper_server = rospy.Service('gripper_service', gripper_service, self.serverCallback)
        rospy.loginfo("Gripper ready to receive service request...")
    
    def serverCallback(self, request):
        pos = request.position
        speed = request.speed
        force = request.force
        if speed > 255 or speed <=0:
            return(gripper_serviceResponse('invalid speed value. Valid in range (0,255]'))
        if force > 255 or force <=0:
            return(gripper_serviceResponse('invalid force value. Valid in range (0,255]'))
        if pos > 255 or pos < 0:
            return(gripper_serviceResponse('invalid position value. Valid in range [0,255]'))

        rospy.loginfo("moving the gripper. positino = {}, speed={}, force={}".format(pos, speed, force))
        self.gripper.move_and_wait_for_pos(pos, speed, force)
        return(gripper_serviceResponse('Done'))

if __name__ == '__main__':
    gripper_obj = HandEGripper()
    rospy.spin()