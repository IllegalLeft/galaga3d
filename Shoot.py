#Shooting Script for Galaga3D
# 2010
# Isaac and Sami Volk

#Intro
cont = GameLogic.getCurrentController()

#Sensors
laser = cont.sensors["fire"]

#Actuators
# get actuator attached to the controller named Spawn
spawn = cont.actuators["spawn"]
# tell AddObject actuator which object is to be added
spawn.object = "laser"
# set initial linear velocity
spawn.linearVelocity = [0,20,0]
# set life span in frames
spawn.time = 100


#Actions
if laser.positive:
	# add the game object
	spawn.instantAddObject()
	# Change states to delay state
	cont.activate("delay_state")

