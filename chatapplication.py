import os
import pyttsx3
print("\nIIEC RISE\n", end='')
print("\n Using this application open 5 application\n1. Google chrome\n2. atom\n3. wmplayer\n4. VLC Media Player\n5. Whatsapp\n", end='')
print("\n for exit program\n1. exit\n2. quit\n3. end\nUse above mentioned keywords to exit the application\n\n", end='')
print("\n Note:- Please use lowercase letter\n\n", end='')
while True:
	print("\nplease chat with me enter your application requirement : "  , end='')
	p = input()
	if (("run" in p) or ("open" in p) or ("browser" in p) or("chrome" in p)  or ("start" in p )) and (("google chrome" in p)or ("browser" in p) or("chrome" in p)):
	  os.system("chrome")
	  pyttsx3.speak("Application Successfully Launched")
	  print("Application Successfully Launched\n", end='')

	elif (("run" in p) or ("execute" in p ) or ("open" in p )  or ("start" in p ) or ("atom" in p )) and  (("atom" in p) or ("editor" in p) or ("text editor" in p) or ("atom" in p)):
	  os.system("atom")
	  pyttsx3.speak("Application Successfully Launched")
	  print("Application Successfully Launched\n", end='')

	elif (("run" in p) or ("execute" in p ) or ("open" in p )  or ("start" in p ) or ("wmplayer" in p) or ("window media" in p)) and (("player" in p) or ("media" in p) or ("wmplayer mp4" in p) or ("wmplayer" in p)):
	  os.system("wmplayer")
	  pyttsx3.speak("Application Successfully Launched")
	  print("Application Successfully Launched\n", end='')
	  
	elif (("run" in p) or ("execute" in p) or ("open" in p) or ("start" in p) or ("play" in p) or ("vlc" in p) or ("VLC" in p)) and (("media player" in p) or ("vlc" in p) or ("VLC" in p) or ("player" in p) or ("vlc" in p) or ("vlc mp3" in p) or ("vlc mp4" in p)):
	  os.system("VLC")
	  pyttsx3.speak("Application Successfully Launched")
	  print("Application Successfully Launched\n", end='')
	  
	elif (("run" in p) or ("execute" in p) or ("open" in p) or ("start" in p) or ("whatsapp" in p) or ("wtsapp" in p)) and (("whatsapp" in p) or ("wtsapp" in p) or ("chat application" in p) or ("messanging app" in p)):
	  os.system("whatsapp")
	  pyttsx3.speak("Application Successfully Launched")
	  print("Application Successfully Launched\n", end='')

	elif  ("exit" in p)  or ("quit" in p) or ("end" in p):
	  print("\nThank you for chatting with me!\n")
	  print("Created By :- Rohit Sharma\n", end='')
	  break

	else:
	  print("\nThis application is not availabel in system or may be you are not use correct application name.\n")


