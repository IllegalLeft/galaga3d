#Intro
gl = GameLogic
cont = gl.getCurrentController()

#Sensors
left = cont.sensors["left"]
right = cont.sensors["right"]

#Motion
motion = cont.actuators["motion"]

#Grab controller object for rotation
obj = cont.owner

#Set variables
leftrot = [0,-0.5,0]
rightrot = [0,0.5,0]
rot = [0,0,0]
local = 0
speed = 0
strafe = 2

#Set left & right motions wrt strafe variable
#WIP rotations for side-to-side movement
if left.positive:
	speed = -strafe
#	obj.applyRotation (rot,local)
	rot = leftrot
if right.positive:
	speed = strafe
#	obj.applyRotation (rot,local)
	rot = rightrot

#Use local linear velocity
motion.useLocalLinV = False
#Set LinV to speed variable
motion.linV = (speed,0,0)

#Activate the actuator
cont.activate(motion)

#Apply rotation
obj.applyRotation (rot,local)
