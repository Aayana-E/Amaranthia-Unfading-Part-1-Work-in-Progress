#############################################################
##                                                          #
##                                                          #
##Programmed by: Aayana Evanson                             #
##                                                          #
##Program Description: A text adventure game for VGD 1000   #
##                                                          #
##Game: Ameranthia Part 1                                   #
##                                                          #
#############################################################

#import readline
import pygame
import random
import sys
import os
import time
from pygame.locals import *




pygame.init()

#Messing with imagery
#image = pygame.image.load(r'C:\Users\annae\Documents\School\Current\Video Game development\Game Assets\Background Image -Words\Mountain.png') 



   

#clock = pygame.time.Clock()
#screen = pygame.display.set_mode((600,500))

#bg = pygame.image.load("Mountain.png")

#display.update()

#declaring varibles
Items = []
party = ['you'] #People you travel with
you_hp = 20.0 #your health
ItemsAmt = 0
Weapon = "none"
MeetEver = False
global PlayerName




#Story Dialog
#Intro to game


def intro():
    
    global PlayerName
    print("\nWhat is you name?")
    print(">>",end="", flush=True)
    PlayerName = input()

    print("\nThe World of Amarantia is a place for all, a place where almost everything and anything is possible.\n")

    print("\nA place where you can be who you want to be.") 


    input()
    print("\nAt least thats what everyone thinks.")

    input()
    print("\nThe world of Amarantia has changed  over the past decades.") 

    print("\nNo one knows the exact meaning for the things that are happening but we know something is wrong.")

    print("\nGreetings", PlayerName) 
    input()
    text = "Enter the word of Amaranthia"

    print("Enter the word of Amaranthia")
    
    #print("\u0332".join(text))
    #u0332 #Underline
    input()
    print("________________________________________________________________________________________________________________________________________________________________________________")
    #input()

    

#Anna
def Hole():


    
    print("    'Hello!' 'Hello!'   ")
    input()
    print("These were the  sounds that you woke up to.")
    input()
    print("You slowly opened and closed your eyes as they adjusted to the light on your face.")

    print("    'Hello!' 'Hello!'   ")
    
    input()
    print("Your vision began to clear as you stared up at the stange man infront of you. Your brain couldn't quite proccess what he was saying yet with the sharp thudding coming from the back of your head. ")
    input()

    print("This thudding couldn't stop you from noticing the strangers sharp jaw line and concerned expression.")

    #{img:Ever Knight.JPG}
    
    #Clear Screen for windows
    os.system('cls')
    time.sleep(1)

def MeetingEverAtHole():

    
    print("    'Are you okay? You took a nasty fall there are you okay?'" )
    input()
    print("""Enter a number:
    1: 'Ya I think so?'
    2: 'No'
    3: 'Who the hell are you and where am I?'
    4: '...'

   
    """)
    print(">>",end="", flush=True)
    HoleStrangerOptions = input()
    if HoleStrangerOptions == '1':
        print("  'Nice to know you're doing well. That's my good deed for the month and my cue to leave'")
        input()
        print("You watch as the strander gets off of their knees and starts walking out of the alley leaving you on the cold fur like ground.")
        input()
        print("""You didn't really know what to do other than look around the alley.
The stranger had just left you with no further help or information for where you were.

Well you didn't exactly ask but it didn't look like you would get help out of him anyways.
        """)
        #Clear Screen for windows #Aayana Evanson
        os.system('cls')
        time.sleep(1)
        SearchAlley()
    elif HoleStrangerOptions == '2':
        print("Well its getting dark so have fun down there.")
        input()
        print("You watch as the strander gets off of their knees and starts walking out of the alley leaving you on the cold fur like ground.")
        #Clear Screen for windows
        os.system('cls')
        time.sleep(1)
        AlleyMainQuestions()

    elif HoleStrangerOptions == '3':
        print("  'You must be batshit crazy. Have fun with life' ")
        input()
        print("You watch as the strander gets off of their knees and starts walking out of the alley leaving you on the cold fur like ground. Shaking their head as if helping you was a mistake in the first place.")
        #Clear Screen for windows
        os.system('cls')
        time.sleep(1)
        AlleyMainQuestions()

    elif HoleStrangerOptions == '4':
        print("  'I'll take silence for a yes'")
        input()
        print("You watch as the strander gets off of their knees and starts walking out of the alley leaving you on the cold fur like ground.")
        input()

        print("You took your moment to assess what you should do?")
        input()
        
        #Clear Screen for windows
        os.system('cls')
        time.sleep(1)


        
        
        StayInAlley()

    


def AlleyMainQuestions():
    print("You didn't know what to do next but you knew you had options")
    print("""Enter 1: Look Around
    Enter 2: Search The Alley
    Enter 3: Try to find the Stranger
    Enter 4: Stay Here
    
    """)
    print(">>",end="", flush=True)
    MainQuesOptions = input()
    if MainQuesOptions == '1':
        LookAroundAlley()
    elif MainQuesOptions == '2':
         SearchAlley()
    elif MainQuesOptions == '3':
        FollowRoad()
    elif MainQuesOptions == '4':
        StayInAlley()#Anna

    #Clear Screen for windows
    os.system('cls')
    time.sleep(1)

##############################################################################
#Alley Main Questions Options and Bombarded


def LookAroundAlley():
    print("You took this time to look around for signs to inform you of where you are or what happened to you.") 
    print("You couldn't recall anything but the sound of your head cracking against the the hard earth." )
    input()
    print("""You raised your hand to your temple feeling the wet substance against your temple.
    You sighed and continued to look around.
    There were signs on what seemed to be a bar at the exit of the alley but the words were too foriegn to recognize. 
    """)
    input()
    print("You started to question if you should explore the alley or search for the stranger")
    print("""Enter 1 : Search The Alley
    Enter 2: Try to find the stranger
    Enter 3: Stay Here
    """)
    print(">>",end="", flush=True)
    AlleyExit = input()
    
    #Clear Screen for windows
    os.system('cls')
    time.sleep(1)
    
    if AlleyExit == '1':
        SearchAlley()
    elif AlleyExit == '2':
        FollowRoad()
    elif AlleyExit == '3':
        StayInAlley()
        

    
def StayInAlley():
    print("You could stay and wait for someone or take a nap and wait")
    input()
    print()
    print("What should you do?")
    print("Enter: Sleep, Stay")
    print(">>",end="", flush=True)
    SleepOrStay = input()
    print()
    if SleepOrStay == "Sleep" or "sleep":
        print("You sat down on the ground and rest your head against the ground and waited")
        input()
        print("Someone had to come for you")
        input()
        print("There had to be someone out there looking for you")
        input()
        print("Your eyes started to get tired as the pounding in your head got louder")
        input()
        print("A short nap won't hurt")
        GetBombarded()
    elif SleepOrStay == "Stay" or "stay":
        print("You sat down on the ground and rest your head against the ground and waited")
        input()
        print("Someone had to come for you")
        input()
        print("There had to be someone out there looking for you")
        GetBombarded()

def GetBombarded():
    
    #Clear Screen for windows
    os.system('cls')
    time.sleep(1)
    
    print("You were woken up from your nap to a sound of what seemed like footsteps")
    input()
    print("'Hello?' You asked as you started to wipe the sleep from your eyes")
    input()
    
    print("The air was airy and low growls started to fill the silence")
    input()
    print("You didn't know what to think of it. Were there bears around?")
    input()
    
    print("The growls just got louder and louder as dragging of feet got louder and louder")
    input()
    print("your fight or flight response started kicking in so you immediately got up and started making a run out of the alley")
    input()
    print("Before you knew it you fell face first as you ran into something")
    input()
    print("You looked at who you fell on only to see what seemed to be a decaying creature")
    print("Half of his jaw was gone and his skin was peeling off as if he was burnt")
    input()
    print("You tried to push yourself off of the creature but it seemed to grab ahold of you as you felt more weight on your back")
    input()
    print("You felt a sharp sting on your leg as if someone was peeling a sore off of your leg")
    input()
    Scream()
    print("You started to scream as the creature that was under you latched onto your neck")
    input()
    print("It didn't seem as if anyone head your screams")
    input()
    print("Your body began to sting as blood started pouring from your wounds")
    input()
    print("You couldn't help but keep thinking that you should have left. You should have left")
    input()
    print("________________________________________________________________________________________________________________")
    main()

        
def SearchAlley():
    print("""There had to be something around you other than moss and trash.
Something in this alley that could help or make some sense of the situation that you were in.
You looked around and there was only so much that the alley could hold.
    """)
    input()
    print("There was a huge garbage bin that had potential to have something of use. There was also a stack of papers covered by some weird substance.")
    input()
    print("What should you do?")
    print()
    print("""    Enter 1: Search garbage bin
    Enter 2: Search the stack of paper
    Enter 3: Take Nothing and leave
             """)
    print(">>",end="", flush=True)
    SearchAlleyOpt = input()
    
    #Clear Screen for windows
    os.system('cls')
    time.sleep(1)
    
    if SearchAlleyOpt == '1':
        SearchGarbage ()
        FollowRoad()
    elif SearchAlleyOpt == '2':
        SearchPaper ()
        FollowRoad()
    elif SearchAlleyOpt == '3':
        print("""You didn't really feel like rustling through garbage so you just took one last look at the alley and started leaving.
                There has to be a reason that you're here. """)

    

#End of AlleyMainQuestions Options
##############################################################################



########################################################################################
#Alley Search Options
def SearchGarbage ():
    print("""\n You looked around for anything that you could use to boost yourself up and saw only one option.
You rolled up your sleves and dragged over a small pail for a stepping stool. 
    """)
    input()
    
    print ("The screaching of the pail blessing your ears and not helping the pounding in your head. ")
    #Garbage can sound
    input()
    print("""
You stepped onto the pail and swung your right legs over first then your left resulting in you falling into the trash can. 

You began searching through what seemed to be months old trash as the smell of rotten eggs and a dead animal? grew stronger. 

You didn't exactly wake up this morning and expect to be swimming in a sea of garbage. 
The only things you seemed to be finding were molded food and basic household trash.

Does no one throw out good things these days?

You were interrupted by your thoughts when you stomped your toes on something hard.
You took this as you last ditch effort and fully submurgerd yourself into the bags of trash till you got your hands on the hard object. 

You pulled yourself out of the trash can being surrounded by the smell of rotten eggs and dead fish. 

You sighed and sucked it up as you looked at the crowbar in your hand. 

This will have to do.  
    """)
    input()
    #Items[0] ="Crowbar"
    Weapon = "Crowbar"
    #ItemsAmt= ItemsAmt+1

    #Clear Screen for windows
    os.system('cls')
    time.sleep(1)

def SearchPaper():
    print("""The first paper was covered in some kind of slime.
            You quickly tossed that away along with some others that were ruined by the slime, rain and other forms of natural elements.
            Through all of the papers lying there there was only one that seemed to be in some kinds of proper state. 
    """)
    input()
    print("Should you read the paper or leave it?")
    print("""Enter 1 to read the paper
    Enter 2 to leave the paper
          """)
    print(">>",end="", flush=True)
    PaperOpt = input()
    if PaperOpt == '1':
        print("You tried to make out as much as you could from the paper")
        print("")
        input()

        print("""                             THE OLD POST
                                                ILUSTRATED WEEKLY
                Est. 1869                       Saturday, October 24, 2082

                                  N E W      P R E S I D E N T     E L E C T 


                New President   |  New School to  | Disappearance 
                Elected     in  |  be opened on   | of citizen said
                Amaranthia The  |  the west side. | to be hoax. Recent
                                |  Word has come  | disappearsance of
                                          for all | citizens is said
                                            beings| to not worry about
                                                            what is
                                                                just
        """)
        input()
        print("")
        print("Should you take the paper?   Enter Yes or No")
        print(">>",end="", flush=True)
        TakePaper = input()
        if TakePaper == "Yes": 
            #Items[0] = 'Newspaper'
            Weapon = 'Newspaper'
            #ItemsAmt= ItemsAmt+1
            print("""You took the newspaper and rolled it into your back pocked and started making your way out of the alley.
            There has to be a reason as to why you are here.
            """)
            input()
            
        else :
            print("You sighed at the fact that you wasted precious time that you could have used to do something else and started making your way out of the alley.")
            input()
            
    elif  PaperOpt == 2:
        print("You sighed at the fact that you wasted precious time that you could have used to do something else and started making your way out of the alley.")
        input() 
#End of Alley Search Options
########################################################################################

def FollowRoad():

    global MeetEver
    #If hurt
    if you_hp < 20 and MeetEver == False:
        print("You couldn't proccess what had just happened but you quickly rushed out of the bar.")
        input()
        print("Taking one last look at the the cold lifeless body that you had beat senslessly with a", Weapon , ".")
        input()
        print("""You already had a strange feeling about this place and that incounter didn't help it at all.")
        The stranger should have soem knowledge of what the hell was happening here but he had to be long gone by now.
        The sun had already set by this point and you we're already hurt.
        Now wasn't the time to mop around and try to figure out what the hell just happened.
        There had to be a safe place that you could recouperate but you didn't know if there were more of whatever that was.
               """)
        input()
        print("""You continued your way up the road as the stars from the sky lite up your path way. 



        Every sound around you from the soft howls of the wind to the creaks the old buildings had you at your highest attention.
              """)
        input()
        print("""


                                    Time Skip



        """)
        input()
        print("""You had been walking for about an hour or so and you had finally seen some form of light.

        It was still sketch but it ws late and you didn't exactly know what to do.
        You walked up to the lit house hoping there would be people of some help here.



              """)

        input()
        print("""You raised your hand into a fist to knock on the door.
        The only thing you could do is hope that there was someone here to help.
            """)
        input()
        KnockOnDoor()

    #If not hurt
    else: 
        print("You couldnt help but feel on edge as you continued on your path down the road.")
        input()
        print("The road seemed to go on for ages and the stranger had to be around here somewhere.")
        input()
        print("They couldn't have gotten far could they?")
        input()
        print("The sun had practically set at this point")
        input()
        print("It was just you and your footsteps in this strange surroundings.")
        input()
        
        print("You didn't think too much at the sounds around you but this one was different")
        input()
        print("The sound was low but persistant and seemed like it was getting louder and louder")
        input()
        print("You turned around to see if you could see where the sound was coming from but there didnt seem to be anything in your immediate vicinity")
        input()
        print("You kept walking thinking it was just your head messing with you")
        input()
        print("What you identified as a low growling was persitent as you continued on your walk")
        input()
        print("You took this moment to check behind you one more time")
        input()
        print("From the corner of your eyes you noticed what seemed to be an actual person")
        input()
        print("Your immediate thoughts went to the stranger from earlier.")
        print("This had to be him")
        print("You started walking towards the stranger but something seemed off")
        input()
        print("The stranger seemed to be hunched over and limping as they made they way towards you")
        input()
        print("The growling seemed to get louder and louder as it got closer")
        print("It had come to your attention that this was not the stranger from earlier")
        input()
        if Weapon == "Crowbar" or Weapon == "Newspaper" : 
            print("Your hand gripped onto the " , Weapon , " as the anxiety started to rise")
            print("As the thing got closer to you. You couldn't help but notice the way his rips were showing.")
            print("His torn clothes seemed to do nothing to show off his form.")
            print("His jaw seemed to be almost non existant as there was a huge gash in the side of it")
            print("Your brain immediately went into fight or flight mode as you prepared yourself for the worst")
        fight()
              


           
    
#End of Follow Road


#####################################################################################
def fight():
    
    #Clear Screen for windows
    os.system('cls')
    time.sleep(1)

    
    global you_hp
    global Weapon

    #Attacks = a
    #Defence = d

        
    you_a = 1
    you_d = 5

    #Zombie
    Zom_a_one = 10.0
    Zom_d_one = 3.0
    Zom_hp_one = 20

    #Check weapons
    if Weapon == "Newspaper":
        you_a += 2
        you_d += 1
    elif Weapon == "Crowbar":
        you_a += 4
        you_d += 2
    elif Weapon == "none":
        you_a = 1
        you_d = 5
    else:
        pass

    turn =0
    fight = True
    print("You didn't know what to do as the thing started getting closer to you")


    
    print()
    print("Should you attack?")
    print(">>",end="", flush=True)
    opt = input()
    
    
    
    
    if opt == 'yes' or 'Yes':
        #Gets input for user
        hit = you_a / Zom_d_one
        Zom_hp_one = Zom_hp_one - hit
        print("The rotting guy has " + str(int(Zom_hp_one)) + "hp left")
    elif opt == 'no' or opt == 'No':
        print("You stood in shock not knowing what was happening as the rotting man swung at you.")
                      
        #if you dont attack you may be able to run
    elif opt == 'run' or 'Run':
        r = random.randint(0,5)
        if r ==0:
            print ("You took this moment not waiting a second to collect yourself and continued running down the road.")
            input()
            print ("You continued running for a few more minutes before you tripped lading face first to the ground")
            input()
            print(" 'You should really watch where you're going. Mistakes like this could get you killed.' You pushed yourself off the ground quickly only to be faced with a pair of shoes infront of you")
            input()
            print ("You looked up and saw the stranger from earlier standing in front of you")
            #break
            fight == False
    else:
        print("Invalid input. Is that a run for your life like it depends on it or a no?")
            #return Zom_hp_one, you_hp
            
    while fight == True:
        turn+=1
        go =turn%2 #Player or Zombie turn

        #When zom is less than 5 hp
        #if Zom_hp_one <= 5 and Zom_hp_one >0:
        #Eveprint()


        if go ==0:
            att = random.randint(1,5)
            BigAttack_Zom = random.randint(1,4)
            if BigAttack_Zom  == 1:
                Zom_a_one = 15
            elif BigAttack_Zom  ==2:
                Zom_a_one = 2
            else:
                Zom_a_one = 6

            #If you kill it before Ever gets there
            if Zom_hp_one <= 0:
                #Ever comes in 
                print("You swung straight into the head of the rotting corpse with your" , Weapon)
                input()
                print("The rotting corpse seeming to become unresponsive and proceeded to fall to the ground")
                input()
                print(' "We meet again. Sadly." the stranger stated watching you try to catch your breathe and understand what just happened')
                break
            if you_hp<5:
                #Ever comes in 
                print("You were starting to feel exausted you didn't know what you were going to do.")
                input()
                print("You raised your hand to take another swing but you were stopped by a clever being sliced straight through the rotting guy's head. The smell of rotting eggs making you gag as you watch the lifeless body fall to the ground to reveal the stranger from earlier")
                #Zom_hp_one = Zom_hp_one-7 
                print(' "We meet again. Sadly." the stranger stated pulling his axe clean from the rotting mans head')
                break

            #Zombie Attacks
            if att ==1 or 2 or 3:
                hit = Zom_a_one/you_d
                you_hp -= hit
                print("\nThe rotten creature swung at you. You have "+ str(int(you_hp)) + "hp left")
                        
            else:
                print("\n The rotten creature seemed to miss his attack")
                #return Zom_hp_one, you_hp comes in 
                print("You were starting to feel exausted you didn't know what you were going to do.")
                input()
                print("You raised your hand to take another swing but you were stopped by a clever being sliced straight through the rotting guy's head. The smell of rotting eggs making you gag as you watch the lifeless body fall to the ground to reveal the stranger from earlier")
                #Zom_hp_one = Zom_hp_one-7 
                print(' "We meet again. Sadly." the stranger stated pulling his axe clean from the rotting mans head')
                break

        #Your attack
        if go ==1:

            BigAttack=0
            #big attack
            if Weapon == "Crowbar":
                BigAttack= random.randint(1,5)
            #if BigAttack
            elif Weapon == "Newspaper":
                BigAttack= random.randint(1,3)
                    
            if BigAttack == 1:
               you_a = 15
            elif BigAttack == 2:
                you_a = 10
            elif BigAttack == 3:
                you_a = 25
            elif BigAttack == 4:
                you_a = 1
            else:
                you_a = 5


            print()

            print("Should you attack?")
            print(">>",end="", flush=True)
            opt = input()
            
    
            if opt == 'yes' or 'Yes':
                #Gets input for user
                hit = you_a / Zom_d_one
                Zom_hp_one = Zom_hp_one - hit
                print("The rotting guy has taken " + str(int(Zom_hp_one)) + "hp left")
            elif opt == 'no' or opt == 'No':
                print("You stood in shock not knowing what was happening as the rotting man swung at you.")
                  
            #if you dont attack you may be able to run
            elif opt == 'run' or opt == 'Run':
                r = random.randint(0,5)
                if r ==0:
                    print ("You took this moment not waiting a second to collect yourself and continued running down the road.")
                    input()
                    print ("You continued running for a few more minutes before you tripped lading face first to the ground")
                    input()
                    print(" 'You should really watch where you're going. Mistakes like this could get you killed.' You pushed yourself off the ground quickly only to be faced with a pair of shoes infront of you")
                    input()
                    print ("You looked up and saw the stranger from earlier standing in front of you")
                    break
                else:
                    print("Invalid input. Is that a run for your life like it depends on it or a no?")
                    #return Zom_hp_one, you_hp

        #Zombie Attack
        if go ==0:
            att = random.randint(1,5)
            BigAttack_Zom = random.randint(1,3)
            if BigAttack_Zom  == 1:
                Zom_a_one = 10
            elif BigAttack_Zom  ==2:
                Zom_a_one = 2
            else:
                Zom_a_one = 4

            #Zombie Attacks
            if att ==1 or 2 or 3:
                hit = Zom_a_one/you_d
                you_hp -= hit
                print("\nThe rotten creature swung at you. You have "+ str(int(you_hp)) + " hp left")
                
            else:
                print("\n The rotten creature seemed to miss his attack")
                #return Zom_hp_one, you_hp

    
    #Clear Screen for windows
    os.system('cls')
    time.sleep(1)
    
    MeetEver()

######################################################################################
#End of fight

def MeetEver():
    global MeetEver
    global PlayerName
    MeetEver = True
    print("  'Well you look like you are doing well so I'll be on my way.' The stranger said")

    print()
    print("What should you do?")
    print("""    Enter 1: Follow the Stranger
    Enter 2: Beg for Help
    Enter 3: Ask for Help
    """)
    print(">>",end="", flush=True)
    WhatToDo = input()
    
    print()
    if WhatToDo =='1':
        print("You didn't say a word and followed the stranger. He seemed to be the person who knew what was going on but he didn't want to explain anything it seemed.")
        print('  "Could you not follow me?" the stranger said looking back at you following him ')
        print()
        input()
        print("Should you continue following?")
        print(">>",end="", flush=True)
        FollowYesOrNo = input()
        if FollowYesOrNo == 'Yes' or 'yes':
            print("You ingnored the stranger and decided to follow him anyways")
        elif FollowYesOrNo == 'No' or 'no':
            print("You didn't really see any other options and followed him anyway")
        else:
            print("  'That's not an answer but okay' the stranger stated as you continued to follow then.")
        print("  'The name's Ever by the way' The stranger said who kept walking down the road")
        input()
        print("  'Mines ", PlayerName,"'")
        input()
        print("  'Well" , PlayerName , " you're in for a ride")
    elif WhatToDo =='2':
        print("  'You can't just leave me here again. Not again at least. I was attacked and I would like to know what is happening and where I am. So you are going to help me if it's the last thing you do")
        input()
        print("  'I mean I could leave you here to die, but I'm in a good mood today' The stranger said as they turned around to look at you")
        input()
        print("  'The name's Ever by the way' The stranger said who kept walking down the road")
        input()
        print("  'Mines ", PlayerName, "'")
        input()
        print("  'Well" , PlayerName , " you're in for a ride. Welcome to Ameranthia.")
    elif WhatToDo =='3':
        print("  'Could you atleast help me then?' you asked")
        input()
        print("  'I mean I could leave you here to die, but I'm in a good mood today. So lets head somewhere save should we not.' The stranger said as they turned around to look at you")
        input()
        print("  'The name's Ever by the way' The stranger said who kept walking down the road")
        input()
        print("  'Mines ", PlayerName, "'")
        input()
        print("  'Well" , PlayerName , " you're in for a ride. Welcome to Ameranthia.")
        KnockOnDoor()
    
def KnockOnDoor():

    
    if MeetEver == False:
        print("""
You spent a few more minutes walking down the road. You couldn't process what had happened but this was what youru life seemed like it was now. 
        

It was practically pitch black at this point you had finally come up to a small town.
There were lights one in a few buildings. Most buildings were three stories high made of a pale grey brick.
Someone here had to know what was happening and where you were. There has to be some good left in this world.
Or something that makes sense. Or at least someone who wouldn't try to kill you.
        """)
        input()



        print("""You walked up to the door and knocked a few times waiting for a response.
        You knocked faster as you were getting impatient. You didn't know if someone or something was following you and there seemed to be signs of life behind this door.
        """)
        input()

        print("Someone opened the door not to soon later and you saw it was the stranger from earlier. 'Not you again' he groaned.")
        input()
        print("  'Who's your friend Ever?' a little girl who was wearing a blue vest with a purple off the shoulder blouse to match her purple sweats and light blue hoodie that was wraped around her waist asked.")
        input()
        print("So Ever was his name")
        input()
        print("  'I do not know nor do I give a shit' Ever stated as he started walking away from the door, 'You coming or not stalker, you either get checked out or stay out there and die'")

        print("  'The name's Marie and lets get you checked out immediately so we don't have to detain you' Judy smiled to you as she said that but it was still worrying as you had no idea what that meant.")
        input()
        print(" You followed the child intot the house passing numerous people who seemed to be having dinner as the fresh smell of food filled the air")
        input()
        print("  'What's your name by the way?' Marie asked as she lead you into a seperate room")
        input()
        print("  'It's ' ", PlayerName, "'")
        input()
        print("  'Well ", PlayerName, " welcome to The Town of Morendo by the way")

        input()

        print("This was a start of something new. What it was you don't know yet. One could only hope for the best")
        input()

        print("\n                               End of Part 1")
        
    elif MeetEver == True:
        print("""   You spent a few more minutes walking down the road with Ever. You didn't really say anything but continued to folloow Ever.
        It was practically pitch black at this point but the two of you had finally come up to a small town.
        There were lights one in a few buildings. Most buildings were three stories high made of a pale grey brick.
        Ever seemed to know the place though as he approached it.
        """)
        input()

        print("""Ever walked up to the door and knocked a few times waiting for a response.
    Someone opened the door not to soon later and you followed Ever into the booming home filled with people.

        """)
        input()

        print("The home was bustling as people passed it and out the room. The smell of food fillig the atmosphere making your stomach rumble.")
        input()

        print("You followed Ever into a seperate room with a much quiter bunch of people")
        input()

        print(" A girl no taller than 5ft approached you as you looked around. She was wearing a blue vest with a purple off the shoulder blouse to match her purple sweats and light blue hoodie that was wraped around her waist.")
        input()

        print("  'Ever has friends? What a surpprise' the  little girl claimed")
        input()

        print("  'Very funny Marie, but this is ", PlayerName , " and you are going to make sure that they're fed and good to go.' Ever said this and immediately left you int he presence of the little girl'")
        input()

        print("  'Well lets get you checked out immediately so we don't have to detain you' Judy smiled to you as she said that but it was still worrying as you had no idea what that meant. 'Welcome to The Town of Morendo by the way")
        input()

        print("This was a start of something new. What it was you don't know yet")
        input()

        print("\n                             End of Part 1")
        input()
        input()

#Main gameplay
def main():
    
    intro()
    
    #Clear Screen for windows
    os.system('cls')
    time.sleep(1)
    
    
    Hole()
    MeetingEverAtHole()

    #remove
    #SearchAlley()
   
    #FollowRoad()
    KnockOnDoor()



            
#######################################################################    
#The intro
print("\n \n \n \n Welcome to Amarantia Part 1. Type 'start' to enter. Type 'info' for information on this game.")
print(">>",end="", flush=True)
opt = input()

if opt == 'start':
    main()
elif opt == 'info':
    print("Ameranthia is a text based game made by Aayana Evanson for VGD 1002. This is Part 1 to keep the game simple.")
    print()
    print()
    print("This is the first final draft of Ameranthia so there may be some errors and some assets missing") 
    print("The game will prompt you for input whether that be text or a number")
    print("Input is indicated by the << Symbol")
    print()
    print("You will need to press enter to forward the text but do not spam it")
    print("Give it a try won't you")
    input()
    print("Good Job")
    print()
    print("I hope you enjoy the game")
    main()
else:
    print("I don't think you entered the correct options")
    print("Please start the game over")
