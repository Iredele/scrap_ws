# import os
# from ament_index_python.packages import get_package_share_directory
# from launch import LaunchDescription
# from launch_ros.actions import Node
# import xacro


# def generate_launch_description():

#     # Specify the name of the package and path to xacro file within the package
#     pkg_name = 'scrap_pkg'
#     file_subpath = 'description/robot.urdf.xacro'


#     # Use xacro to process the file
#     xacro_file = os.path.join(get_package_share_directory(pkg_name),file_subpath)
#     robot_description_raw = xacro.process_file(xacro_file).toxml()


#     # Configure the node
#     node_robot_state_publisher = Node(
#         package='robot_state_publisher',
#         executable='robot_state_publisher',
#         output='screen',
#         parameters=[{'robot_description': robot_description_raw}] # add other parameters here if required
#     )

#     # rviz_launch = Node(
#     #     package="rviz2",
#     #     executable="rviz2",
#     #     name="rviz2",
#     #     arguments=[
#     #         '-d' + os.path.join(
#     #             get_package_share_directory('scrap_pkg'),
#     #             'config',
#     #             'view_bot.rviz'
#     #         )]
#     # )
#     rviz_launch = Node(
#         package="rviz2",
#         executable="rviz2",
#         name="rviz2",
#         arguments=[
#             '-d' + os.path.join(
#                 get_package_share_directory('nav2_bringup'),
#                 'rviz',
#                 'nav2_default_view.rviz'
#             )]
#     )

#     # Run the node
#     return LaunchDescription([
#         node_robot_state_publisher,
#         rviz_launch
#     ])




import os

from ament_index_python.packages import get_package_share_directory

from launch import LaunchDescription
from launch.substitutions import LaunchConfiguration, Command
from launch.actions import DeclareLaunchArgument
from launch_ros.actions import Node

import xacro


def generate_launch_description():

    # Check if we're told to use sim time
    use_sim_time = LaunchConfiguration('use_sim_time')
    use_ros2_control = LaunchConfiguration('use_ros2_control')

    # Process the URDF file
    pkg_path = os.path.join(get_package_share_directory('scrap_pkg'))
    xacro_file = os.path.join(pkg_path,'description','robot.urdf.xacro')
    # robot_description_config = xacro.process_file(xacro_file).toxml()
    robot_description_config = Command(['xacro ', xacro_file, ' use_ros2_control:=', use_ros2_control, ' sim_mode:=', use_sim_time])
    
    # Create a robot_state_publisher node
    params = {'robot_description': robot_description_config, 'use_sim_time': use_sim_time}
    node_robot_state_publisher = Node(
        package='robot_state_publisher',
        executable='robot_state_publisher',
        output='screen',
        parameters=[params],
        remappings=[
            ("/diff_drive_controller/cmd_vel_unstamped", "/cmd_vel"),
        ],
    )


    # Launch!
    return LaunchDescription([
        DeclareLaunchArgument(
            'use_sim_time',
            default_value='false',
            description='Use sim time if true'),
        DeclareLaunchArgument(
            'use_ros2_control',
            default_value='true',
            description='Use ros2_control if true'),

        node_robot_state_publisher
    ])







