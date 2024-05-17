import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from collections import deque
from time import sleep

dq = deque()
class TurtleController(Node):
    def __init__(self,x,y,z,time):
        self.x = x
        self.y = y
        self.z = z
        super().__init__('turtle_controller')
        self.publisher_ = self.create_publisher(Twist, '/turtle1/cmd_vel', 10)
        timer_period = time
        self.timer = self.create_timer(timer_period, self.timer_callback)

    def timer_callback(self):
        msg = Twist()
        msg.linear.x = self.x
        msg.linear.x = self.y
        msg.angular.z = self.z
        self.publisher_.publish(msg)

def executor():
    rclpy.init()
    x = dq[0]["x"]
    y = dq[0]["y"]
    z = dq[0]["z"]
    time = dq[0]["time"]
    turtle_controller = TurtleController(x,y,z,time)
    rclpy.spin(turtle_controller)
    turtle_controller.destroy_node()
    rclpy.shutdown()



def main():
    msg = input(str("Digite o comando: "))
    msg_slice = msg.split(" ")
    print(msg_slice)
    try:
        comand ={
        "x" :float(msg_slice[0]),
        "y" : float(msg_slice[1]),
        "z" : float(msg_slice[2]),
        "time" : float(msg_slice[3])}
        dq.append(comand)
        executor()

    except:
        print("Comando Eviado de maneira errada")


    

