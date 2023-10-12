# Smart Crossing Robot Assistant for Pedestrians
After cloning the repository with `git clone <repo-link> --recurse-submodules`:
- `cd /scrap_ws`
- Run `rosdep install --from-paths src --ignore-src -r -y`
- Run `colcon build --symlink-install`
- For the camera install the V4l using `sudo apt insall libraspberrypi-bin v4l-utils ros-humble-v4l2-camera`
  > Make sure you are added to the 'video group' of the raspberry pi.

# Launching the project
After building the project, source ros in your workspace with `source install/setup.bash`.
- Now run: `ros2 launch scrap_pkg launch_scrap.launch.py` and `ros2 launch scrap_pkg sensors.launch.py`

  NOTE: This launches the controller manager running the diffdrive controller. It also launches the lidar and camera.
