#! /usr/bin/env python3
import os
import rospy
from std_srvs.srv import Empty, EmptyResponse

def handle_restart_mapping(req):
    os.system("rosnode kill /alaserPGO")
    os.system("rosrun aloam_velodyne alaserPGO")
    resp = EmptyResponse()
    return resp

def restart_mapping_server():
    rospy.init_node('restart_mapping_server')
    s = rospy.Service('restart_mapping', Empty, handle_restart_mapping)
    rospy.spin()

if __name__ == "__main__":
    restart_mapping_server()

