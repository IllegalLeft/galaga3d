#Intro
cont = GameLogic.getCurrentController()

#Sensors
laser = cont.sensors["Fire"]

#Actuator
# get actuator attached to the controller named Spawn
spawn = cont.actuators["Spawn"]
# tell AddObject actuator which object is to be added
spawn.object = "laser"
# set initial linear velocity
spawn.linearVelocity = [0,10,0]
# set life span in frames
spawn.time = 100


#Action
if laser.positive:
	# add the game object
	spawn.instantAddObject()

#GIT ruleszzz
