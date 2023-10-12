from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch_ros.actions import Node
import os
from ament_index_python import get_package_share_directory


def generate_launch_description():
    ld = LaunchDescription()
    
    lidar_launch = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(get_package_share_directory('velodyne'),'launch',
                         'velodyne-all-nodes-VLP16-launch.py')
        )
    )

    # rsp_launch = IncludeLaunchDescription(
    #     PythonLaunchDescriptionSource(
    #         os.path.join(get_package_share_directory('scrap_pkg'),'launch',
    #                      'rsp.launch.py')
    #     )
    # )

    usb_cam_node = Node(
            package='usb_cam',        
            executable='usb_cam_node_exe'
        )

    motor_driver_node = Node(
        package='scrap_pkg',
        executable='motor_driver_node'
    )

    # listener_node = Node(
    #     package='demo_nodes_py',
    #     executable='listener'
    # )
        

    ld.add_action(lidar_launch)
    # ld.add_action(rsp_launch)
    ld.add_action(usb_cam_node)
    ld.add_action(motor_driver_node)
    # ld.add_action(listener_node)
    return ld