#Intro
gl = GameLogic
cont = gl.getCurrentController()

#Sensors
left = cont.sensors["left"]
right = cont.sensors["right"]

#Motion
motion = cont.actuators["motion"]

#Set variables
speed = 0
strafe = 2

#Set left & right motions wrt strafe variable
if left.positive:
	speed = -strafe
if right.positive:
	speed = strafe

#Use local linear velocity
motion.useLocalLinV = True
#Set LinV to speed variable
motion.linV = (speed,0,0)

#Activate the actuator
cont.activate(motion)
