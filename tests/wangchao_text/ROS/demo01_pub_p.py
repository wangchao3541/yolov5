import rospy
from std_msgs.msg im

if __name__ == "__main__":
    rospy.init_node("talker")
    pub = rospy.Publisher("chatter", String, queue_size=10)
    rate = rospy.Rate(10)
    count = 0
    while not rospy.is_shutdown():
        msg = "hello ros " + str(count)
        pub.publish(msg)
        rospy.loginfo("发布：%s", msg)
        rate.sleep()
        count += 1