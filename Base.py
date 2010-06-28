#Intro
gl = GameLogic
cont = gl.getCurrentController()

#Sensors
forward = cont.sensors["Up"]
backward = cont.sensors["Back"]
left = cont.sensors["Left"]
right = cont.sensors["Right"]

#Motion
motion = cont.actuators["motion"]

#Set variables
speed = 0
strafe = 2

#Set left & right motions wrt strafe variable
if left.positive:
	speed = strafe
if right.positive:
	speed = -strafe

#Not sure what this does, Sam?
motion.setLinearVelocity(speed,0,0,1)
gl.addActiveActuator(motion,1)