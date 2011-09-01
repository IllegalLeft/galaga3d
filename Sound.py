# Sound Script
# Galaga3D
# Sami Volk
# 2010

from bge import logic

gl = logic
cont = gl.getCurrentController()

#Sensors
message = cont.sensors["message"]

#Actuators
hit = cont.actuators["hit"]
laser = cont.actuators["laser"]
select = cont.actuators["select"]

#Action
if message.positive == 1:
	if message.subjects[0] == "hit":
		cont.activate(hit)
	if message.subjects[0] == "laser":
		cont.activate(laser)
	if message.subjects[0] == "select":
		cont.activate(select)

#Easier way to add new sounds below
#Not implemented because cannot change KX_SoundActuator's fileName in current version (says it doesn't exist)
"""
#List of sounds 
#(add new sounds here)
soundList = [
["hit", "hit.wav"],
["laser", "laser.wav"],
["select", "select.wav"]
]
soundListLength = len(soundList)

if message.positive == 1:
	print("message")
	print(message.subjects[0])
	
	#Check if the message matches one of the sounds
	for number in range(len(soundList)):
		print("for ", number)
		
		if message.subjects[0] == soundList[number][0]:
			sound.fileName = soundList[number][1]
			print("sound ", number)
			cont.activate["sound"]
"""

