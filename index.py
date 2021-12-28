print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

choice1 = input("You stand at the edge of an island, do you want to go in to the jungle, or along the beach? Type 'jungle' or 'beach'. \n").lower()
if(choice1 == "jungle"):
  choice1a = input("These trees are thick, but the animals seem to know the way. Do you want to follow the monkey or the snake? Type 'monkey' or 'snake'. \n").lower()
  if(choice1a == "monkey"):
      choice1b = input("You follow the monkey to a pyramid. Do you want to climb the pyramid or dig under it? Type 'climb' or 'dig'. \n").lower()
      if(choice1b == "climb"):
          print("What an amazing view, a treasure for sure, but not the riches you were looking for. Game Over")
      elif(choice1b == "dig"):
          choice1c = input("You have reached a wall, use dynamite or pick ax? Type 'dynamite' or 'ax'. \n")
          if(choice1c == "dynamite"):
              print("WOW, that was a big blast. You did not survive. Game Over!")
          elif(choice1c == "ax"):
              print("Congratulations! You have broken through the wall into the treasure vault.")    
      else:
          print("Your indecision has been the death of you. Game Over!")
  elif(choice1a == "snake"):
      choice2 = input("You follow the snake along a path into a tunnel. The tunnel forks, which way do you want to go? Type 'right' or 'left'. \n").lower()
      if(choice2 == "right"):
          print("OH NO! The tunnel has caved in. Game Over!")
      elif(choice2 == "left"):
          choice2a = input("You have reached a wall, use dynamite or pick ax? Type 'dynamite' or 'ax'. \n")
          if(choice2a == "dynamite"):
              print("WOW, that was a big blast. You did not survive. Game Over!")
          elif(choice2a == "ax"):
              print("Congratulations! You have broken through the wall into the treasure vault.")    
          else:
              print("Your indecision has been the death of you. Game Over!")
      else: ("You can not walk through walls, you have died of a head injury. Game Over!")        
  else:
      print("You have fallen in a pit.")
elif(choice1.lower() == "beach"):
    b1 = input("You stumble through the sand and find a stream. Which way do you want to go? Type 'up' or 'down'. \n").lower()
    if(b1 == "up"):
        b2 = input("Just ahead through the bushes you can see a pyramid. Do you want to climb the pyramid or dig under it? Type 'climb' or 'dig'. \n").lower()
        if(b2 == "climb"):
            print("What an amazing view, a treasure for sure, but not the riches you were looking for. Game Over")
        elif(b2 == "dig"):
            b3 = input("You have reached a wall, use dynamite or pick ax? Type 'dynamite' or 'ax'. \n")
            if(b3 == "ax"):
                print("WOW, this is taking forever. You have died of boredom. Game Over!")
            elif(b3 == "dynamite"):
                print("Congratulations! You have broken through the wall into the treasure vault.")    
        else:
            print("Your indecision has been the death of you. Game Over!")
    elif(b1 == "down"):
        print("Short journey to the sea, perhaps some fish can be your treasure? Game Over!")
    else:
        print("You have died of scurvy. Game Over!")  
else: 
    print("You have died of scurvy. Game Over!")    
