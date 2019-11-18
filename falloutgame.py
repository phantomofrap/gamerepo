import time
        
my_string = ['Rules',
      '\n' 'You can only go left or right', 
      '\n' 'Some paths kill, some aid',
      '\n' 'There is a nuclear explosion set to happen in exactly 10 moves',
      '\n' 'There is a shelter, but its position is unknown',
      '\n' 'Find the secret path to the shelter (forward). Possibly talk to computers. Survive or die in the fallout']
for i in my_string:
        print(i)
        time.sleep(0.5)
# line = my_string[]
# for line in my_string:
#     print(line)
#     time.sleep(0.5)
# choice = input
def choice_15():
        print('NUKE DENOTATED AND YOU WERE NOT IN THE SHELTER. TRY AGAIN')
        choice = input('Continue? Y or N')
        if choice == 'y':
                pass
                #needs to go back to beginning of game after text roll
        elif choice == 'n':
                exit()
        else:
                print('Invalid')
def choice_14():
        print('cat', 'mouse', 'unicorn', 'python', )
        time.sleep(1)
        print('can', 'cant', 'should', 'might')
        time.sleep(1)
        print('dont', 'did', 'does', 'do')
        time.sleep(1)
        print('something', 'nothing', 'anything', 'mulligan')
        choice = input('4 Magic Words, No Spaces >>> ').lower().strip()
        if choice == 'pythoncandoanything':
                print('Youve successfully stopped the nuke from detonating and saved hundreds of lives. \n However the elite are very displeased at this fact and systematically have you exiled \n from the settlement, only to put a bounty on your head the moment you left camp. Good luck "hero" ')
                exit()


        '''This is the square where i want the <terminal> to be accessed. If you can can input the right set of code based on the paragraph given, you gain access to the nuclear panel at which you can cancel the nuke detonation'''
def choice_13():
        '''This is gonna be the trivia game square. Get 3 questions right and progress to the vault unharmed, or die with one question wrong. '''
        '''Needs a step back method, only square with a BACK as an option'''
        choice = input('Left or Right>>>').lower().strip()
        if choice == 'back':
                choice_10()
def choice_12():
        choice = input('Left or Right>>>').lower().strip()
        if choice == 'right':
                time.sleep(1)
                print('Now I am become death, destroyer of worlds')
                choice_15()
        elif choice == 'left':
                print('At the bottom you see a cracked metal door'
                '\n' 'with a sign that says "Vault 475"'
                '\n' 'you’ve arrived. Congratulations you saved..')
                time.sleep(2.5)
                print('yourself and only yourself while a nuke was'
                '\n' 'set to hit. I should put that on a trophy for you')
                exit()
        else:
                print('Invalid Input')  

def choice_11():
        choice = input('Left or Right>>>').lower().strip()
        if choice == 'left':
                print('After heading down the path, you come to a dead end'
                '\n' 'When you try to turn back the path collapses'
                '\n' 'Youre stuck')
        elif choice == 'right':
                print('After chosing the tunnel, you follow it for some time'
                '\n' '......................................')
                choice_12()
        else:
                print('Invalid Input')        
def choice_10():
        choice = input('Left or Right>>>').lower().strip()
        if choice == 'left':
                print('You head down the path and come to a small light'
                '\n' 'Its a flamethrower')
        elif choice == 'right':
                print('The alarm is almost deafening now'
                '\n' 'but you arrive to a room with one door'
                '\n' 'to the left and what appears to be a tunnel to the right')
                choice_11()
        elif choice == 'forward':
                time.sleep(3)
                print('You see a ripple in the wall. You stick your hand thru it.'
                '\n' 'You walk through the wall to a room with a sign that says......'
                '\n' 'If you solve a riddle, youll have to wait a little, but youll get right through'
                '\n' 'Getting one wrong, early triggers the bomb, be sure this is what you want to do'
                '\n' 'otherwise input "back"')
                choice_13()
        else:
                print('Invalid Input')

def choice_9():
        choice = input('Left or Right>>>').lower().strip()
        if choice == 'left':
                print('The stairs continue..'
                '\n' 'you come past all sorts of paintings and priceless art..')
                choice_10()
        elif choice == 'right':
                print('You come to a wall, which opens up'
                '\n' 'You see a computer ahead, you walk to it'
                '\n' 'It has a question mark on the screen'
                '\n' 'The door closes behind you')
                time.sleep(1)
        else:
                print('Invalid Input')
        choice = input('? >> ').lower().strip()
        if choice == 'bfb':
                choice_14()
        

def choice_8():
        choice = input('Left or Right>>>').lower().strip()
        if choice == 'left':
                print('You head down a set of stairs'
                '\n' 'All of a sudden the stairs collapse')
                time.sleep(.5)
                print('Dictators ride to and fro on tigers from which they dare not dismount.'
                '\n' 'And the tigers are getting hungry.-Winston Churchill')
        elif choice == 'right':
                print('The stairs continue..'
                '\n' 'you come past all sorts of paintings and priceless art..'
                '\n' '......................................')
                choice_9()
        else:
                print('Invalid Input')
def choice_7():
        choice = input('Left or Right>>>').lower().strip()
        if choice == 'left':
                print('The alarm is getting louder now'
                '\n' 'As you move down the hallway'
                '\n' 'You come up to some stairs that lead downward'
                '\n' 'You follow them')
                choice_8()
        elif choice == 'right':
                print('You hear a gun loading sound behind you'
                '\n' 'A machine gun begins firing and kills you')
                time.sleep(.5)
                print('It is a mistake to try to look too far ahead.'
                '\n' 'The chain of destiny can only be grasped one link at a time.-Winston Churchill')
        else:
                print('Invalid Input')
def choice_6():
        choice = input('Left or Right>>>').lower().strip()
        if choice == 'left':
                print('You walk down the hallway to an open door'
                '\n' 'A trap door opens and you fall thru')
                time.sleep(.5)
                print('The people who cast the votes dont decide an election'
                '\n' 'The people who count the votes do- Joesph Stalin')
        elif choice == 'right':
                print('You begin walking again'
                '\n' 'The ground starts to crumble under you'
                '\n' 'You jump just as the path collapses and make to the door')
                choice_7()
        else:
                print('Invalid Input')

        
def choice_5():
        choice = input('Left or Right>>>').lower().strip()
        if choice == 'left':
                print('So you thought you could go left three'
                '\n' 'times and you could just keep progressing'
                '\n' 'huh? Lmao this isnt my first code block')
                time.sleep(1)
                print('A single death is a tragedy, a million deaths is a statistic- Joesph Stalin')
        if choice == 'right':
                print('A platform opens below, and you step on it.'
                '\n' 'A machine begins to hummmm'
                '\n' 'A bright light flashes and blinds you'
                '\n' 'You open your eyes to another choice')
                choice_6()
        else:
                print('Invalid Input')


def choice_4():
        choice = input('Left or Right>>>').lower().strip()
        if input == 'right':
                choice_5()
def choice_3():
        choice = input('Left or Right>>>').lower().strip()
        
        if choice == 'left':
                print('You move further down the hallway'
                '\n' 'you hear the sounds of a distant alarm'
                '\n' 'a door opens near you, and you walk through')
                time.sleep(.5)
                choice_5()
        elif choice == 'right':
                print('You progress down a dark coridor.' 
        '\n' + 'You see something shiny on the ground'
        '\n' + 'You investigate...its a grenade')
                time.sleep(.5)
                print('Death is not something to fear, but something to strive for')
        else:
                print('Invalid Input')

def choice_1():
        print('You progress down a dark coridor.' 
        '\n' 'There is a door handle, you twist it.'
        '\n' 'The light shines bright in the next room'
        '\n' 'Congrats you have advanced')
        time.sleep(.5)
        
        choice_3()
        

def choice_2():
        print('You progress down a dark coridor.' 
        '\n' + 'You get to the end and theres a chest.'
        '\n' + 'Chest Creaks......'
        '\n' + 'A live grenade, you die.......')
        time.sleep(1)
        print('An iron curtain is drawn down upon their front.' 
        '\n' 'We do not know what is going on behind.– Winston Churchill')
        
   
        

while True:
        effect = 'A Couple Minutes Before The Bomb Blows.....'
        effect.split()
        for i in effect:
                print(i)
                time.sleep(0.5)

        name = input('Enter your name: ')

        print('Welcome:')
        print(f'{name} the Potiential Vault Dweller')
       
        
        choice = input('Left or right>>>').lower().strip()
        if choice == 'left':
                choice_1()
        if choice == 'right':
                choice_2()



#         def choice_3:
#                 pass
#         def choice_4:
#                 pass
# first_choices = {
#         'choice1':  'You progress down a dark coridor.' 
#                 '\n' + 'You get to the end and theres a chest.'
#                 '\n' + 'Chest Creaks......'
#                 '\n' + 'A live grenade, you die' ,
#         'choice2': 'You progress down a dark coridor.' 
#                 '\n' 'There is a door handle, you twist it.'
#                 '\n' 'The light shines bright in the next room'
#                 '\n' 'Congrats you have advanced'
                
#        }
#possible need for dictionary in a dictonary? not sure this is gonna be the way i continue the game but we are pursuing a theory

# while True:
        #         path_choice = input(">>>> ")

        #         if path_choice == "left":
        #                 print('You progress down a dark coridor.' 
        #                 '\n' 'You get to the end and theres a chest.'
        #                 '\n' 'Chest Creaks......'
        #                 '\n' "A Live Grenade, You die")
        #                 print('Happiness is not achieved by the conscious pursuit of happiness;' 
        #                 '\n' 'It is generally the by-product of other activities– Aldous Huxley')
        #                 break

        #         elif path_choice == "right":
        #                 print('You progress down a dark coridor.' 
        #                 '\n' 'There is a door handle, you twist it.'
        #                 '\n' 'The light shines bright in the next room'
        #                 '\n' 'Congrats you have advanced')
        #                 print('An iron curtain is drawn down upon their front.' 
        #                 '\n' 'We do not know what is going on behind.– Winston Churchill')
        #                 pass
        #                 if path_choice == "left":
        #                         print('You progress down a dark coridor.' 
        #                         '\n' 'There is a door handle, you twist it.'
        #                         '\n' 'The light shines bright in the next room'
        #                         '\n' 'Congrats you have advanced')
        #                         print('An iron curtain is drawn down upon their front.' 
        #                         '\n' 'We do not know what is going on behind.– Winston Churchill')
        #                         elif path_choice == "right":
        #                                 print('You progress down a dark coridor.' 
        #                                 '\n' 'You get to the end and theres a chest.'
        #                                 '\n' 'Chest Creaks......'
        #                                 '\n' "A Live Grenade, You die")
        #                                 print('Happiness is not achieved by the conscious pursuit of happiness;' 
        #                                 '\n' 'It is generally the by-product of other activities– Aldous Huxley')
        #                                 break
                                

        #         elif path_choice == "forward":
        #                 print('You progress down a dark coridor.' 
        #                 '\n' 'You reach the end of the hall'
        #                 '\n' 'Dead End')
        #                 print("All men are enemies. All animals are comrades.- George Orwell")
        #                 while True:
        #                         x = input("Continue: y or n..")
        #                         if x == "y":
        #                                 continue
        #                         elif x == "n":
        #                                 break
        #                         else:
        #                                 print("Invalid Input")
        #         else:
        #                 print("Invalid Input")
        #                 continue

        