# Camera Script
# Galaga3D
# 2011
# Sami Volk

#GameLogic
gl = GameLogic
cont = gl.getCurrentController()

# Scene
scene = gl.getCurrentScene()
current_cam = scene.active_camera

#Cameras
objList = scene.cameras

overview_cam = objList["OBoverview_cam"]	# Overview cam
action_cam = objList["OBaction_cam"]		# Action cam

# Sensors
F5 = cont.sensors["F5"]
F5.key = 166    # key 166 is 'F5'
                # for a list of keys: http://www.tutorialsforblender3d.com/GameModule/KeyCodes.html


# Action

# Switch to Action cam
if (F5.positive and current_cam == overview_cam):
    scene.active_camera = action_cam

# Switch to Overview cam
if (F5.positive and current_cam == action_cam):
    scene.active_camera = overview_cam
