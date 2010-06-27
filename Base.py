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

#Stuff
speed = 0
strafe = 2

if left.positive:
	speed = strafe
if right.positive:
	speed = -strafe

#motion.setLinearVelocity(speed,0,0,1)
#gl.addActiveActuator(motion,1)
motion.setLinearVelocity(speed,0,0,1)
gl.addActiveActuator(motion,1)