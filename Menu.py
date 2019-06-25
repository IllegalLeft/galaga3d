# Import Rasterizer 
import Rasterizer
from bge import logic

gl = logic
cont = gl.getCurrentController()

# Show mouse 
Rasterizer.showMouse(True)

# Play menu song
intro = cont.actuators["intro"]
cont.activate(intro)