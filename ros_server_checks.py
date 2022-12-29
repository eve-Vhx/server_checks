#!/usr/bin/env python
import rospy
import roslaunch


if __name__ == '__main__':
	#rate = rospy.Rate(1)
	while True:
		try:
			rospy.get_master().getPid()
			roscore_failed = False
			#print("ROS Already running")
		except:
			roscore_failed = True
			print("ROS Not running. Starting master")

		if (roscore_failed):
			uuid = roslaunch.rlutil.get_or_generate_uuid(options_runid=None, options_wait_for_master=False)
			roslaunch.configure_logging(uuid)
			launch = roslaunch.parent.ROSLaunchParent(uuid, roslaunch_files=['/home/hcappel1/eve_dev/catkin_ws/src/behavior_logic/launch/behavior_logic.launch'], is_core=True)
			launch.start()
			#rate.sleep(5)
			
