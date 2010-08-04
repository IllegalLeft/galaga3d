# AI Path Script

# Galaga3D
# By: Hydra_skillz
# (http://forum.nystic.com/viewtopic.php?f=34&t=6898&p=64488&hilit=game+engine+ai+part#p64488)
# Documented and modified by: Sami Volk
# 2010



# GameLogic
gl = GameLogic

# Get current controller
cont = gl.getCurrentController()



#Actuators
move = cont.actuators['move']
track = cont.actuators['track']

# Variables
# Nodes in the path sequence
path = ['Node', 'Node.001']
# Normal speed (0)
speed = [0,0,0]
#Stopping speed (0.001)
stop = [0.001, 0.001, 0.001]
# Current node bot is on
point = cont.owner['point']




#If the AI is less than .5 units away...
if cont.owner.getDistanceTo(track.object) <= 2:
    # Add one to point
    point = point + 1
if point < 2:
    # speed[1] is equal to 5
    speed[1] = 5
    # Set object to track as current node
    track.object = path[point]
    # Activate track
    cont.activate(track)
else:
	# Anything else stops the AI in it's tracks
	speed = stop
# Set the property point to equal the variable in this script
cont.owner['point'] = point
# speed is move's LinV
move.linV = speed
# Use local LinV
move.useLocalLinV = 1
# Activate move
cont.activate(move)
