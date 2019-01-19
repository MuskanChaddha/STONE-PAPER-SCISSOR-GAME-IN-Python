import pyttsx3
import playsound
import random
import time

#playsound.playsound(r"F:\Accordion-SoundBible.com-74362576.mp3")
t=time.localtime()
pyttsx3.init(driverName='sapi5')
engine = pyttsx3.Engine()

print("_________________________________________________________________________________________________________________________________________________________________________________________________________________________")
print("                                                                     WELCOME TO STONE PAPER SCISSOR GAME                                                                                                                                         ")
print("_________________________________________________________________________________________________________________________________________________________________________________________________________________________")



engine.say("WELCOME TO  STONE PAPER SCISSOR GAME ")
engine.say("Enter The Username")
engine.runAndWait()

username=input("Enter The Username:     ")
engine.say("HELLO {}".format(username))
engine.say("I Hope {} You Will Enjoy The Game".format(username))

print("Username Is",username)
print("I Hope {} You Will Enjoy The Game".format(username))

print(" ")
print("Winning Rules as follows :")
print(" ")
engine.say("Winning Rules as follows :")

print("RULE 1 => STONE vs PAPER then PAPER Wins ")
engine.say(" RULE 1  STONE versus PAPER then PAPER Wins ")

print("RULE 2 => STONE vs SCISSOR then STONE wins ")
engine.say(" RULE 2  STONE versus scissor then STONE wins ")


print("RULE 3 => PAPER vs SCISSOR then SCISSOR Wins ")
engine.say("RULE 3 paper versus scissor then scissor wins ")

engine.runAndWait()

while True:
    print("The Choices  ARE ")
    engine.say("The Choice AS ")
    print("1.STONE \n2.PAPER  \n3.SCISSOR \n")

    engine.say("Choose 1 For STONE")
    engine.say("Choose 2 For PAPER")
    engine.say("Choose 3 For SCISSOR")
    engine.say("{} Enter Your Choice".format(username))
    engine.runAndWait()

    userchoice = int(input("{} Enter The Choice".format(username)))


    engine.say("{} Entered the choice as".format(username))
    print("{} Entered the choice as {} ".format(username,userchoice))
    while userchoice > 3 or userchoice < 1:
        print("You entered a Wrong Choice ....")
        playsound.playsound(r"F:\iMac_Startup_Chime-Carlo_-1849294605.mp3")
        engine.say("You entered a Wrong Choice ....")
        engine.say("{} Enter  A Valid Choice".format(username))
        engine.runAndWait()
        userchoice = int(input("{} Enter a valid Choice: ".format(username)))


    if userchoice == 1:
        choicename = 'STONE'
    elif userchoice == 2:
        choicename = 'PAPER'
    else:
        choicename = 'SCISSOR'

    print("{} choosed {}  " .format(username , choicename))  #user choice display
    engine.say("{} choosed {}  " .format(username , choicename))
    engine.runAndWait()

    engine.say("Now its a AI Turn")
    print("\nNow ITs AI turn.......")


    compchoice = random.randint(1, 3) # comp choose
    engine.say("AI Chosses {}".format(compchoice))

    while compchoice == userchoice:
        compchoice = random.randint(1, 3)

    if compchoice == 1:
        compchoicename = 'Rock'
    elif compchoice == 2:
        compchoicename = 'paper'
    else:
        compchoicename = 'scissor'


    print("AI Is THINKING....")
    engine.say("AI IS THINKING.....")
    #t.sleep(3)
    engine.runAndWait()
    engine.say("{} choosed : ".format( "AI" , compchoicename))
    print("{} choosed : ".format( "AI" , compchoice))
    engine.runAndWait()

    engine.say(" {} versus {} ".format(choicename,compchoicename))
    engine.runAndWait()
    print(choicename + " V/s " + compchoicename)


    if userchoice==compchoice:
        engine.say("OMG !! Match Drawn !! NO One Wins")
        print("Match Drawn")
    else:
     if ((userchoice == 1 and compchoice == 2) or (userchoice == 2 and compchoice == 1)): #compare

        print("paper wins => ", end="")
        engine.say("Paper Wins")
        result = "paper"

     elif ((userchoice == 1 and compchoice == 3) or (userchoice == 3 and compchoice == 1)):
        print("STONE wins =>", end="")
        playsound.playsound(r"F:\Hammering_Soung_6-Lisa_Redfern-411383436.mp3")
        engine.say("Stone Wins")
        result = "STONE"
     else:
        print("scissor wins =>", end="")
        playsound.playsound(r"F:\salamisound-1020101-paper-scissors-office.mp3")
        engine.say("SCISSOR WINS")
        result = "scissor"

     if result == choicename:
        engine.say("Oh Great {} Wins".format(username))
        print("User wins ")
     else:
        engine.say("OH NO !!! Computer as AI Wins")
        print(" AI wins ")

    engine.say("Do you want to play again Yes Or NO")
    engine.runAndWait()

    print("Do you want to play again? (Y/N)")
    ans = input()

    if ans == 'n' or ans == 'N':
        break

print(" ")
print("END OF THE GAME")
engine.say("END OF THE GAME")
engine.say("Thank You {} For Playing ".format(username))
playsound.playsound(r"F:\iMac_Startup_Chime-Carlo_-1849294605.mp3")

t=time.localtime()
y = t.tm_year
m = t.tm_mon
d = t.tm_mday
print("The Game Ended at {}:{}".format(t.tm_min,t.tm_sec),end="")
print(" & on {}-{}-{} \nTime Zone Is {}".format(d,m,y,t.tm_zone))

engine.runAndWait()
