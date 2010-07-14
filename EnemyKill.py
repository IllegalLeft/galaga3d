# Enemy Kill script
# Sami Volk
# 2010

#GameLogic 
gl = GameLogic

# Get Controller
cont = gl.getCurrentController()

# Set Collision to the corresponding sensor
collision = cont.sensors["Collision"]
# Set property for collision sensor to look for
collision.propName = "laser"
# Set Collision to use false triggering
collision.useNegPulseMode = True


# Set Kill to the corresponding actuator
kill = cont.actuators["Kill"]


#If collision is positive then destroy the object
if collision.positive == 1:
	cont.activate(kill)
