#!/usr/bin/env python

from urdf_project_control.srv import *
import rospy
import time
import sys
import copy
import rospy
import moveit_commander
import moveit_msgs.msg
import geometry_msgs.msg
from math import pi
from std_msgs.msg import String
from moveit_commander.conversions import pose_to_list



class groupService:

	def __init__(self):
		rospy.init_node('udm_project_commander')
		moveit_commander.roscpp_initialize(sys.argv)

		self.robot=moveit_commander.RobotCommander()
		self.scene =moveit_commander.PlanningSceneInterface()
		self.front_left_leg =moveit_commander.MoveGroupCommander("fl")
		self.rear_left_leg =moveit_commander.MoveGroupCommander("lr")
		self.front_right_leg =moveit_commander.MoveGroupCommander("rf")
		self.rear_right_leg =moveit_commander.MoveGroupCommander("rr")
		rospy.Service('kin_service', kin_service, self.handle_req)
		rospy.spin()


	def handle_req(self,req):
		try:
			print req
			command = req.movement
			#front
			self.front_left_leg.set_named_target("Pose_1")
			self.rear_left_leg.set_named_target("Pose_2")
			self.rear_right_leg.set_named_target("Pose_3")
			self.front_right_leg.set_named_target("Pose_4")
			count=0

			if(command.data == "front"):
				display_trajectory_publisher = rospy.Publisher('/move_group/display_planned_path',
                                                   moveit_msgs.msg.DisplayTrajectory, queue_size=20)
				while(count<=5):
					self.rear_right_leg.set_named_target("rr_back")
					self.rear_left_leg.set_named_target("lr_front")
					plan1a=self.rear_right_leg.plan()
					time.sleep(1)
					self.front_left_leg.set_named_target("fl_front")
					self.front_right_leg.set_named_target("rf_back")
					plan2a=self.front_left_leg.plan()
					time.sleep(1)

					self.front_right_leg.set_named_target("rf_front")
					self.front_left_leg.set_named_target("fl_back")	
					plan3a=self.front_right_leg.plan()
					time.sleep(1)
					self.rear_left_leg.set_named_target("lr_front")
					self.rear_right_leg.set_named_target("rr_back")
					plan4a=self.rear_left_leg.plan()
					time.sleep(1)
					count+=1

				count=0
				rep=kin_serviceResponse()
				rep.res.data=True
				rep.message.data="Success"

			elif(command.data == "right"):
				display_trajectory_publisher = rospy.Publisher('/move_group/display_planned_path',
                                                   moveit_msgs.msg.DisplayTrajectory, queue_size=20)
				while(count<=5):
					self.rear_right_leg.set_named_target("rr_back")
					self.rear_left_leg.set_named_target("lr_frontleft")
					plan1a=self.rear_right_leg.plan()
					time.sleep(1)
					self.front_left_leg.set_named_target("fl_frontleft")
					self.front_right_leg.set_named_target("rf_back")
					plan2a=self.front_left_leg.plan()
					time.sleep(1)

					self.front_right_leg.set_named_target("rf_frontleft")
					self.front_left_leg.set_named_target("fl_back")	
					plan3a=self.front_right_leg.plan()
					time.sleep(1)
					self.rear_left_leg.set_named_target("lr_frontleft")
					self.rear_right_leg.set_named_target("rr_back")
					plan4a=self.rear_left_leg.plan()
					time.sleep(1)
					count+=1

				count=0
				rep=kin_serviceResponse()
				rep.res.data=True
				rep.message.data="Success"

			elif(command.data == "back"):
				display_trajectory_publisher = rospy.Publisher('/move_group/display_planned_path',
                                                   moveit_msgs.msg.DisplayTrajectory, queue_size=20)
				while(count<=5):
					self.rear_right_leg.set_named_target("rr_front")
					self.rear_left_leg.set_named_target("lr_back")
					plan1a=self.rear_right_leg.plan()
					time.sleep(1)
					self.front_left_leg.set_named_target("fl_back")
					self.front_right_leg.set_named_target("rf_front")
					plan2a=self.front_left_leg.plan()
					time.sleep(1)

					self.front_right_leg.set_named_target("rf_back")
					self.front_left_leg.set_named_target("fl_front")	
					plan3a=self.front_right_leg.plan()
					time.sleep(1)
					self.rear_left_leg.set_named_target("lr_back")
					self.rear_right_leg.set_named_target("rr_front")
					plan4a=self.rear_left_leg.plan()
					time.sleep(1)
					count+=1

				count=0
				rep=kin_serviceResponse()
				rep.res.data=True
				rep.message.data="Success"
			elif(command.data == "right"):
				display_trajectory_publisher = rospy.Publisher('/move_group/display_planned_path',
                                                   moveit_msgs.msg.DisplayTrajectory, queue_size=20)
				while(count<=5):
					self.rear_right_leg.set_named_target("rr_front")
					self.rear_left_leg.set_named_target("lr_frontright")
					plan1a=self.rear_right_leg.plan()
					time.sleep(1)
					self.front_left_leg.set_named_target("fl_frontright")
					self.front_right_leg.set_named_target("rf_front")
					plan2a=self.front_left_leg.plan()
					time.sleep(1)

					self.front_right_leg.set_named_target("rf_frontright")
					self.front_left_leg.set_named_target("fl_front")	
					plan3a=self.front_right_leg.plan()
					time.sleep(1)
					self.rear_left_leg.set_named_target("lr_frontright")
					self.rear_right_leg.set_named_target("rr_front")
					plan4a=self.rear_left_leg.plan()
					time.sleep(1)
					count+=1

				count=0
				rep=kin_serviceResponse()
				rep.res.data=True
				rep.message.data="Success"
			
			return rep

		except Exception as e:
			rep=kin_serviceResponse()
			print e
			return rep

if __name__ == "__main__":
	groupService()
