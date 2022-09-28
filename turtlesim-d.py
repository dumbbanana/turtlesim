#!/usr/bin/env python3

import sys
import traceback
import rospy
from geometry_msgs.msg import Twist

def main():
    rospy.init_node("draw_d")
    rospy.loginfo("Node has been created.")   
    pub = rospy.Publisher("/turtle1/cmd_vel",Twist, queue_size=10)
    rate = rospy.Rate(2)
    PI= 3.1415926535897             
    i,j,k = 0,0,0
    
    msg = Twist()
    
    while not rospy.is_shutdown():     
        while i <=PI:
            msg.linear.x =PI
            msg.angular.z= PI
            pub.publish(msg)
            rate.sleep()
            i+=PI/2 
    
        while k<1:
            while j<=0:
                msg.linear.x = 0.0
                msg.angular.z= PI
                pub.publish(msg)
                rate.sleep()
                j+=0.5

            msg.linear.x = 2
            msg.angular.z= 0
            pub.publish(msg)
            rate.sleep()
            k+=1

if __name__ == "__main__":
    try:
        print("------------------------------------------")
        print("         Python Script Started!!          ")
        print("------------------------------------------")
        main()
        
    except:
        print("------------------------------------------")
        traceback.print_exc(file=sys.stdout)
        print("------------------------------------------")
        sys.exit()

    finally:
        print("------------------------------------------")
        print("    Python Script Executed Successfully   ")
        print("------------------------------------------")
