# copied from https://sdurobotics.gitlab.io/ur_rtde/guides/guides.html#use-with-robotiq-gripper
# Note from Hui:
# need to run in python version > 3.7.2 (or higher)

import robotiq_gripper
import time
import sys

action = sys.argv[1]
# print("action =", action)
# print("type(action) = ", type(action))

ip = "192.168.0.3"

def log_info(gripper):
    print(f"Pos: {str(gripper.get_current_position()): >3}  "
          f"Open: {gripper.is_open(): <2}  "
          f"Closed: {gripper.is_closed(): <2}  ")

# Initialize gripper
gripper = robotiq_gripper.RobotiqGripper()
gripper.connect(ip, 63352)
# gripper.activate()

# Open Gripper
if action == "1":
    # print("Trying to open gripper")
    gripper.move_and_wait_for_pos(0, 255, 255)
    log_info(gripper)

# Close Gripper
elif action == "2":
    # print("Trying to close gripper")
    gripper.move_and_wait_for_pos(255, 255, 255)
    log_info(gripper)


