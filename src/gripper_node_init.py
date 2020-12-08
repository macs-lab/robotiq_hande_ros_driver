#!/usr/bin/env python3

import time
import rospy 
import actionlib
from std_msgs.msg import Int32
from control_msgs.msg import *
import os

# BUG there is a naming inconsistency with the robotiq_hande_driver
from robotiq_hande_driver.srv import simple_service, simple_serviceResponse

def move_gripper(request):
    # print("Recieved a request!")
    # print ("request = ", request)

    if request.command == 1:
        print ("Opening gripper...")
        os.system('python3.8 gripper_commander.py 1')

    if request.command == 2:
        print ("Closing gripper...")
        os.system('python3.8 gripper_commander.py 2')

    # print("Done processing request!")
    return(simple_serviceResponse(0))

def main():
    global gripper_server
    try:
        print ("Initializing arm_gripper_controller node...")
        rospy.init_node("arm_gripper_controller", anonymous=True, disable_signals=True)

        #Activating gripper 
        print("Activating gripper...")
        os.system('python3.8 gripper_commander.py 0')

        # Testing out server 
        print ("Initializing server in namespace = gripper_service...")
        # Simple service is a custom service I created. Each ROS driver contains an identical copy of simple_service.srv
        gripper_server = rospy.Service('gripper_service', simple_service, move_gripper)

        # # Whenever the subscriber hears something from gripper_command, it executes perform_command
        # print ("Listening to /gripper_command...")
        # subscriber =rospy.Subscriber("gripper_command",Int32, perform_command,queue_size=1)
        
        rate = rospy.Rate(0.5)
        while not rospy.is_shutdown():
            rate.sleep()
    except KeyboardInterrupt:
        rospy.signal_shutdown("KeyboardInterrupt")
        raise

# if __name__ == '__main__': main()actionlib.SimpleActionServer
if __name__ == '__main__': main()