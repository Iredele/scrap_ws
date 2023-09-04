#!/usr/bin/env python
import rclpy
from rclpy.node import Node
from sensor_msgs.msg import PointCloud2
from sensor_msgs.msg import Image
from velodyne_msgs import VelodyneScan

class CarDetectionNode(Node):

    def __init__(self):
        super().__init__('lidar_node')

        self.lidar_subscription = self.create_subscription(
            PointCloud2,
            '/velodyne_points',  # Replace with the actual Velodyne LiDAR topic
            self.detection_callback,
            10  # Queue size
        )

        self.camera_subscription = self.create_subscription(
            Image,
            '/image_raw', 
            self.detection_callback,
            10  # Queue size
        )

    def detection_callback(self, msg):
        # Process the VelodyneScan message, convert it to PointCloud2, and perform further operations
        # Example: You can publish the PointCloud2 data or perform custom processing here
        self.get_logger().info(msg)



def main(args=None):
    rclpy.init(args=args)  # Initialize the ROS 2 system
    node = CarDetectionNode()  # Create an instance of your node class
    try:
        node.run_node_logic()  # Run your node's logic
    except KeyboardInterrupt:
        pass

    node.destroy_node()  # Clean up the node
    rclpy.shutdown()  # Shutdown the ROS 2 system

if __name__ == '__main__':
    main()