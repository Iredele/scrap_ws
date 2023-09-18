#!/usr/bin/env python
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
import RPi.GPIO as GPIO

class MotorDriver(Node):
    def __init__(self):
        super().__init__('motor_driver_node')
        self.subscription = self.create_subscription(
            Twist,
            'cmd_vel',
            self.motor_callback,
            10
        )

        self.left_motor_pin = 13    #black
        self.left_motor_dir = 6     #yellow
        self.right_motor_pin = 12   #grey
        self.right_motor_dir = 5    #orange

        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.left_motor_pin, GPIO.OUT)
        GPIO.setup(self.left_motor_dir, GPIO.OUT)
        GPIO.setup(self.right_motor_pin, GPIO.OUT)
        GPIO.setup(self.right_motor_dir, GPIO.OUT)

        self.left_motor_pwm = GPIO.PWM(self.left_motor_pin, 100)
        self.right_motor_pwm = GPIO.PWM(self.right_motor_pin, 100)
        self.left_motor_pwm.start(0)
        self.right_motor_pwm.start(0)

def motor_callback(self, msg):
    #Conver linear and angular velocities to motor speeds
    linear_vel = msg.linear.x
    angular_vel = msg.angular.z

    #Calculate left and right wheel speeds
    left_speed =  linear_vel - angular_vel
    right_speed = linear_vel + angular_vel


    #Determine direction (forward or reverse)
    if left_speed >= 0:
        left_direction = GPIO.HIGH
    else:
        left_direction = GPIO.LOW

    if right_speed >= 0:
        right_direction = GPIO.HIGH
    else:
        right_direction = GPIO.LOW

    #Set motor direction using GPIO pins
    GPIO.output(self.left_motor_dir, left_direction)
    GPIO.output(self.right_motor_dir, right_direction)

    #Scale motor speeds within PWM range (0-100%)
    left_speed = max(min(abs(left_speed), 1.0), 0.0)
    right_speed = max(min(abs(right_speed), 1.0), 0.0)

    #Map the scaled speeds to PWM range (0-100%)
    left_pwm = int(left_speed * 100)
    right_pwm = int(right_speed * 100)

    # self.get_logger().info(f'left pwm: {left_pwm}', once=True)
    # self.get_logger().info(f'right pwm: {right_pwm}', once=True)


    #Set motor speeds using PWM
    self.left_motor_pwm.ChangeDutyCycle(left_pwm)
    self.right_motor_pwm.ChangeDutyCycle(right_pwm)


def main(args=None):
    rclpy.init(args=args)
    motor_driver = MotorDriver()
    rclpy.spin(motor_driver)
    motor_driver.destroy_node()
    rclpy.shutdown()
    GPIO.cleanup()

if __name__ == '__main__':
    main()




# def main():
#     print('Hi from scrap_pkg.')


# if __name__ == '__main__':
#     main()
