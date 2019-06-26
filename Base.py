
from bge import logic

#Intro
gl = logic
cont = gl.getCurrentController()

#Sensors
left = cont.sensors["Left"]
right = cont.sensors["Right"]

#Motion
motion = cont.actuators["Motion"]

#Grab controller object for rotation
obj = cont.owner

#Set variables
local = 0
speed = 0
strafe = 4
#Rotation Variables
rotation = 0
rot_increment = 0.2

#Set left & right motions with respect to strafe variable
#WIP rotations for side-to-side movement
if left.positive:
	speed = -strafe
	rotation = -rot_increment
if right.positive:
	speed = strafe
	rotation = rot_increment

#Use local linear velocity
motion.useLocalLinV = False
#Set LinV to speed variable
motion.linV = (speed,0,0)

#Activate the actuator
cont.activate(motion)

#Apply rotation
obj.localOrientation = ([0,0,rotation],[0,1,0],[0,0,0])