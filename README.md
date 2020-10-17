## robotiq_hande_ros_driver
# Requirements
To use this package install python3.8 on your computer. Do NOT set python3.8 as your machines default. This will cause serious system problems.

# Usage
1. Make gripper_node_init.py executable 
2. In a terminal shell run "./gripper_node_init.py"
3. Publish commands to the /gripper_comand rostopic using the shell command "rostopic pub gripper_command std_msgs/Int32 1" to open the gripper and "rostopic pub gripper_command std_msgs/Int32 2" to close the gripper
