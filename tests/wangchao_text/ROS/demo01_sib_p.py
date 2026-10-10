#!/usr/bin/env python3
import rospy
from std_msgs.msg import String

def doMsg(msg):
    rospy.loginfo("收到消息：%s", msg.data)

if __name__ == "__main__":
    rospy.init_node("huaHua")
    sub = rospy.Subscriber("chatter", String, doMsg, queue_size=10)
    rospy.loginfo("订阅者已经启动，等待消息...")
    rospy.spin()