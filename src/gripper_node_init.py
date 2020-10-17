#!/usr/bin/env python3

import time
import rospy 
from std_msgs.msg import Int32
import os  

def perform_command(msg):

    try:
        if msg.data == 1:
            print ("Opening gripper...")
            os.system('python3.8 gripper_commander.py 1')

        if msg.data == 2:
            print ("Closing gripper...")
            os.system('python3.8 gripper_commander.py 2')

        # print ("Resetting gripper_command to 0...")
        # msg.data = 0

    except KeyboardInterrupt:
        client.cancel_goal()
        raise

def main():
    global client
    try:
        print ("Initializing arm_gripper_controller node...")
        rospy.init_node("arm_gripper_controller", anonymous=True, disable_signals=True)

        # Whenever the subscriber hears something from gripper_command, it executes perform_command
        print ("Listening to /gripper_command...")
        subscriber =rospy.Subscriber("gripper_command",Int32, perform_command,queue_size=1)
        rate = rospy.Rate(0.5)

        while not rospy.is_shutdown():
            rate.sleep()
    except KeyboardInterrupt:
        rospy.signal_shutdown("KeyboardInterrupt")
        raise

if __name__ == '__main__': main()