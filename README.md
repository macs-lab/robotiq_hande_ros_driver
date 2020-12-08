## robotiq_hande_ros_driver
# Requirements
To use this package install python3.8 on your computer. Do NOT set python3.8 as your machines default. This will cause serious system problems.

# Usage
0. Ensure that gripper_node_init.py executable, and that the robot is launched (see external_control_ur5e package for details on launching the robot)
1. Open a new terminal and change directory into the gripper controller src folder >>roscd robotiq_hande_driver/src
2. Launch the gripper controller >>./gripper_node_init.py
3. Send commands to the gripper (there are a few options for this)

USING ROS TOPICS 
A) Publish commands to the /gripper_comand rostopic using the shell command "rostopic pub gripper_command std_msgs/Int32 1" to open the gripper and "rostopic pub gripper_command std_msgs/Int32 2" to close the gripper

USING A GRIPPER SERVER
B) See midterm_demo.py in the external_control_ur5e package for more details on how this is done

DIRECTLY RUNNING COMMAND FILES
C) When inside the src directory of the gripper controller run >>python3.8 gripper_commander.py 1 to open the gripper or >>python3.8 gripper_commander.py 2 to close the gripper.

This is useful if you're not ready to integrate gripping into your main process file, but need the gripper to grab or release something. 
