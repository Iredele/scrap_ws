from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch_ros.actions import Node
import os
from ament_index_python import get_package_share_directory


def generate_launch_description():
    ld = LaunchDescription()
    
    other_launch_file = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(get_package_share_directory('velodyne'),'launch',
                         'velodyne-all-nodes-VLP16-launch.py')
        )
    )

    usb_cam_node = Node(
            package='usb_cam',        
            executable='usb_cam_node_exe'
        )

    # talker_node = Node(
    #     package='demo_nodes_cpp',
    #     executable='talker'
    # )

    # listener_node = Node(
    #     package='demo_nodes_py',
    #     executable='listener'
    # )
        

    ld.add_action(other_launch_file)
    ld.add_action(usb_cam_node)
    # ld.add_action(talker_node)
    # ld.add_action(listener_node)
    return ld