#!/usr/bin/env python3 

import rospy 
from std_msgs.msg import String 

def chatter_topic_callback(msg):
    rospy.loginfo("new msg received : %s"%msg.data)


if __name__=="__main__":
    rospy.init_node("simple_subscribe_node_python",anonymous=True)

    rospy.Subscriber("chatter_topic",String,chatter_topic_callback)

    rospy.spin()
