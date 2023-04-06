## This file is a cat island game. ##

print('''
******************************************************************************
          |                   |                  |                     |       
 _________|___________________|__________________|_____________________|______
|                   |                |                   |                |
|___________________|________________|___________________|________________|___
          |                |            /:\      |                     |                     
 _________|________________|__,---.__ /::::\_____|_____________________|______            
|                   |      `-.__     \:::::/             |                |             
|___________________|________;;:\--.__`--.--.____________|________________|___            
          |                ,;;'` `    `--.__  `-._                     |       
 _________|________________`,  ,\       /,  `--.__;____________________|______
|                   |      <   (o) ___ (o)   >           |                |   
|___________________|_____<        \:/        >__________|________________|___
          |                <     ._,"._,     >   |                     |
 _________|_________.---._|_`-.    ~~~    .-'____|_____________________|______
|                .'._.--. `.   `~:~~~~~~:'               |                |
|________________`-'|____`. `.  :        :_______________|________________|___
          |               :__: :________  :___   |                     |
 _________|___________;'xx:XXxxxxxxxxxx:xxxXXX:xx:_____________________|______
|                   :::xx:XXXX:xxxxxxxxx:XXXXXX:xxx:.    |                |
|__________________::xxx:XXX/X;xxxxxxxxxx:XXXXXX:xxx:.___|________________|___
          |       ::xxx:XXX// xxxxxxxxxx// XXXXXX:xxx:.                |         
 _________|______||xxxx:XX//   xxxxxxxx//   XXXXXX:xx||________________|______
____/______/_____||xxx:XX//  0  xxxxxx// 0   XXXXX:xx||______/______/_____/___    
/______/______/__`::xx:XXXXX:xxxx/ \xxxxx:XXXXXXXX:xx:'/______/______/_____/__    
____/______/______`::xx:XXXXX:xxx___Xxxx:XXXXXXXX:xx:'__/______/______/______/     
/______/______/____`::xx:XXXXXxxxxxxxxxxxXXXXXXX:x::'____/______/______/______
____/______/______/__`:xx:XX \/  \/  \/ \/XXXXX:xx:'______/______/______/_____
/______/______/______/_`.x:XXXXxxxxxxxxxxXXXXxx;''___/______/______/______/___
____/______/______/_______/______/______/______/______/______/______/______/__
/______/______/______/______/______/______/______/______/______/______/______/
____/______/______/______/______/______/______/______/______/______/______/___
/______/______/______/______/_____/______/______/______/______/______/______/_
____/______/______/______/______/______/______/______/______/______/______/___
/______/______/______/______/______/______/______/______/______/______/______/
****************************************************************************** 
''')
print("Welcome to cat island.")
print("Your mission is to survive here.")

#Write your code below this line 👇

choice1 = input('You\'re at a cross road. Where do you want to go? Type "left" or "right" \n').lower()
if choice1 == "left":
  choice2 = input('You\'ve come to a lake. There is an island in the middle of the lake. Type "wait" to wait for a boat. Type "swim" to swim across. \n').lower()
  if choice2 == "wait":
    choice3 = input("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose? \n").lower()
    if choice3 == "red":
      print("You got out through the exit. You alive!")
    elif choice3 == "yellow":
      print("You found the cat! You Die.")
    elif choice3 == "blue":
      print("It's a room full of warter. You alive!")
    else:
      print("You chose a door that is exist You alive!")
  else:
    print("You crossed the river safely. You alive!")
else:
  print("You fell into a hole. You alive!")
  