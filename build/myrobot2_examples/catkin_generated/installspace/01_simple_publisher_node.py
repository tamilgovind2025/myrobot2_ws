#!/usr/bin/env python3 
import rospy 
from std_msgs.msg import String

if __name__=="__main__":
    rospy.init_node("simple_publisher_python",anonymous=True)

    pub=rospy.Publisher("chatter_topic",String,queue_size=25)

    rate=rospy.Rate(10)
    counter=0

    while not rospy.is_shutdown():
        hello_msg="hello world from python : %d"%counter
        pub.publish(hello_msg)
        rate.sleep()
        counter=counter+1
        