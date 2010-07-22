# Bullet Kill Script
# Galaga3D
#
# Sami Volk
# 2010

# Gamelogic
gl = GameLogic

# Get current controller
cont = gl.getCurrentController()

# Sensors
# Set Collision to the corresponding sensor
collision = cont.sensors["collision"]
# Set property for collision sensor to look for
collision.propName = "enemy"
# Set Collision to use false triggering
#collision.useNegPulseMode = True

# Set property to the corresponding sensor
propsens = cont.sensors["propsens"]
# Set property to look for
propsens.propName = "hit1"
# Set value to look for
propsens.value = "1" 



#Actuators
# Set kill to the corresponding actuator
kill = cont.actuators["kill"]

# Set hit to the corresponding actuator
hit = cont.actuators["hit"]
# Set hit actuator to assign hit a value
hit.propName = "hit1"
# Set hit actuator to assign hit a value of 1
hit.value = "1"


# Actions
#If collision is positive then destroy the object
if collision.positive == 1:
    cont.activate("hit")

# if hit1 is equal to 1 kill the laser

if propsens.positive == 1:
    cont.activate("kill")
