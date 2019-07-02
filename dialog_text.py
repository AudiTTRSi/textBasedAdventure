from time import sleep
import datetime

print ("+--------------------------------------------+")
print ("|                                            |")
print ("| Welcome to this text based adventure game. |")
print ("|                                            |")
print ("+--------------------------------------------+")
sleep(0.5)
print("Another text")
sleep(1)
print(" More text")
print("\n")
player_name = str(input("Please enter your name:"))
player_time = datetime.datetime.now()
sleep(0.5)
print ("Welcome " + player_name + ", are you ready to start this adventure?")
sleep(0.5)
print ("The time right now is: " + str(player_time.strftime("%Y-%m-%d %H:%M")))
sleep(0.5)

