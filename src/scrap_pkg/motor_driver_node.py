#!/usr/bin/env python
import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32

import RPi.GPIO as GPIO

class MotorController(Node):
    def __init__(self):
        super().__init__('motor_controller')
        self.subscription = self.create_subscription(Float32, 'motor_command', self.command_callback, 10)
        self.pwm_pin = 18  # Change this to the actual GPIO pin you're using for PWM
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.pwm_pin, GPIO.OUT)
        self.pwm = GPIO.PWM(self.pwm_pin, 1000)  # 1000 Hz PWM frequency
        self.pwm.start(0)  # Start with 0% duty cycle
        self.duty_cycle = 100.0

    def command_callback(self, msg):
        # Make a switch statement that chooses the direction of movement (fwd, bwd, left, right, stop)
        
        self.pwm.ChangeDutyCycle(self.duty_cycle)
        self.get_logger().info(f"Setting motor speed to {self.duty_cycle}%")

def main(args=None):
    rclpy.init(args=args)
    motor_controller = MotorController()
    rclpy.spin(motor_controller)
    motor_controller.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()



#use the code developed for moving the motors using rpi gpio library
#subscribe to the custom /motor_command topic that is published by the car detection node