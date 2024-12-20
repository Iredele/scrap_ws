# Smart Crossing Robot Assistant for Pedestrians

## Overview

The **Smart Crossing Robot Assistant for Pedestrians** is a ROS 2-based project designed to enhance pedestrian safety and convenience at crosswalks. It integrates various sensors and controllers to manage traffic, detect pedestrians, and ensure smooth operation of crossing systems.

## Installation

Follow these steps to set up the project:

1. **Make a new directory**
    ```bash
    mkdir scrap_ws
    cd scrap_ws

2. **Clone the Repository**

   Clone the repository along with its submodules:

   ```bash
   git clone https://github.com/Iredele/scrap_ws.git --recurse-submodules ./src

3. **Navigate to the source directory**
   ```bash
   cd src
4. **Install Dependencies**
   Use `rosdep` to install all necessary dependencies:
   ```bash
   rosdep install --from-paths src --ignore-src -r -y
5. **Build the Project**
   Change directory back to the scrap_ws and Build the workspace using `colcon`:
   ```bash
   colcon build --symlink-install
6. **Setup the Camera**
   Install the required packages for camera support:
   ```bash
   sudo apt install libraspberrypi-bin v4l-utils ros-humble-v4l2-camera
> **Note:** Ensure your user is added to the video group to grant necessary permissions for camera access. You can add your user to the group with:

    sudo usermod -aG video $USER
Log out and log back in for the changes to take effect.
## Launching the Project
After successfully building the project, follow these steps to launch the system:

  1. Source the Workspace

Source the ROS 2 setup script to overlay the workspace:
  ```bash
  source install/setup.bash
```
2. Launch the Nodes
Run the main launch files:
  ```bash
  ros2 launch scrap_pkg launch_scrap.launch.py
  ros2 launch scrap_pkg sensors.launch.py
```
> **Note:** This launches the controller manager running the differential drive controller, as well as the LiDAR and camera sensors.

Developed by Dayo Iredele.




