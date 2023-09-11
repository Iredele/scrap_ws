#!/usr/bin/env python
import rclpy
from rclpy.node import Node
from geometry_msgs import Twist
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

        self.left_motor_pin = 17
        self.left_motor_dir = 18
        self.right_motor_pin = 27
        self.right_motor_dir = 22

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



#use the code developed for moving the motors using rpi gpio library
#subscribe to the custom /motor_command topic that is published by the car detection node




# import rclpy
# from rclpy.node import Node
# from std_msgs.msg import Float32

# import RPi.GPIO as GPIO

# class MotorController(Node):
#     def __init__(self):
#         super().__init__('motor_controller')
#         self.subscription = self.create_subscription(Float32, 'motor_command', self.command_callback, 10)
#         self.pwm_pin = 18  # Change this to the actual GPIO pin you're using for PWM
#         GPIO.setmode(GPIO.BCM)
#         GPIO.setup(self.pwm_pin, GPIO.OUT)
#         self.pwm = GPIO.PWM(self.pwm_pin, 1000)  # 1000 Hz PWM frequency
#         self.pwm.start(0)  # Start with 0% duty cycle
#         self.duty_cycle = 100.0

#     def command_callback(self, msg):
#         # Make a switch statement that chooses the direction of movement (fwd, bwd, left, right, stop)
        
#         self.pwm.ChangeDutyCycle(self.duty_cycle)
#         self.get_logger().info(f"Setting motor speed to {self.duty_cycle}%")
