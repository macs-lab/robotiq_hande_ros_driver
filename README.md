## robotiq_hande_ros_driver
This is the ROS driver for Robotiq Hand-E gripper. We assuming that the gripper is mounted on an UR robot, and the PC is connected with UR through Ethernet cable.
You need to properly configure your networks such that PC and Robot can ping each other.

## Install
Simply clone this package to your ROS catkin src folder then build the catkin workspace.
```bash
cd ~/your_ws/src
git clone https://github.com/macs-lab/robotiq_hande_ros_driver.git
cd ..
catkin_make
```

## Usage
Create or modify the existing launch file based on your needs.
* robot_ip: the IP address of your UR robot
* speed: finger closing and opening speed (1~255)
* force: force applied by the finger (1~255)

Then start the driver by running the launch file. The gripper can be controlled using ROS topics or services.

### Using topics
The driver listens to messages on `hand_e_gripper_node` topics (message type [Int32](http://docs.ros.org/en/melodic/api/std_msgs/html/msg/Int32.html)). To open the gripper, send value 1. To close the gripper, send value 0.

### Using services
Services allows the driver to send feedback when the finger action completes. This is useful when you want the program to wait until gripper complete its movement. See [`test.py`](https://github.com/macs-lab/robotiq_hande_ros_driver/blob/master/src/test.py) for example usage.


## Questions
Have questions? Open up a discussion [here](https://github.com/macs-lab/robotiq_hande_ros_driver/discussions)