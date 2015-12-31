#!/usr/bin/env python
print("""
This program turns your Explorer HAT into an Akai MPC!

Created by Iker García.
Based on the drums.py program, by Pimoroni. 

Hit any touch pad 5 to 8 to select a drum kit.
Hit any touch pad 1 to 4 to hear a drum sound.

Press CTRL+C to exit.
""")
import explorerhat
import pygame
import signal

pygame.mixer.pre_init(44100, -16, 1, 512)
pygame.mixer.init()
pygame.mixer.set_num_channels(16)

samples = ["1","2","3","4"] #This creates a default samples list, with four elements, to be updated later.
sounds = [] #This creates and empty sounds list.
def handle(ch, evt):
  if ch > 4: #This enables us to use touch pad from 5 to 8 to select a drum kit.
    if evt == 'press':
      if ch == 5:
        explorerhat.light.off() #Switches off lights in order not to confuse among drum kits.
        explorerhat.light.blue.on() #Turns on light so as to know which drum kit we are using.
        print("First drumkit selected") #Text to know which drum kit we are using.
        samples=['drumkit/808/8081.wav', 
	         'drumkit/808/8082.wav',
	         'drumkit/808/8083.wav',
	         'drumkit/808/8084.wav'] #The location of our llops.     
	
	for x in range(4): #Fills the sounds list, with our loops.
	  sounds.insert(x,(pygame.mixer.Sound(samples[x])))
  
      if ch == 6: #Same behaviour as previous channel, different loops.                                                               
        explorerhat.light.off()
        explorerhat.light.yellow.on()
        print("Second drumkit selected")
        samples=['drumkit/Jazz/Jazz1.wav',
	         'drumkit/Jazz/Jazz2.wav',
    	         'drumkit/Jazz/Jazz3.wav',
	         'drumkit/Jazz/Jazz4.wav']
       
        for x in range(4):
	  sounds.insert(x,(pygame.mixer.Sound(samples[x])))
	
      if ch == 7: #DEACTIVATED, UNLESS LOOPS ARE ADDED. 
        explorerhat.light.off()
        explorerhat.light.red.on()
        print("Third drumkit selected")
      # Write down the location of your loops.
      # Copy the for statement from previous channels.
		
      if ch == 8: #DEACTIVATED, UNLESS LOOPS ARE ADDED.
        explorerhat.light.off()
        explorerhat.light.green.on()
        print("Fourth drumkit selected")
      # Write down the location of your loops.
      # Copy the for statement from previous channels.
  
  if ch <= 4: #This enables us to use touch pads from 1 to 4 as drums.
    if evt == 'press':
      sounds[ch-1].play(loops=0) #Plays a sound
      
explorerhat.touch.pressed(handle)  #Function is called if touch pad is pressed.
explorerhat.touch.released(handle) #Function is called if touch pad is released.
signal.pause() #Sound is stopped.

