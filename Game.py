import random

money = 100

# Function to check whether the bet is a valid one or not 
def check_bet(bet, guess):
  global money
  if (bet < 0):
    print("You can't bet negative values!")
    print("You got %s dollars" % money)
  elif (bet > money):
    print("You don't have enough money to bet!")
    print("You got %s dollars" % money)

# Evaluates whether or not the player won.
def win_lose(choice, num, bet):
  global money
  if (choice == num):
      print("You win!")
      print("You won %s dollars! " % bet) 
      money += int(bet)
      print ("Now you have %s dollars!" % money) 
  else:
      print ("You lose!")
      print ("You lost %s dollars! " % -bet) 
      money -= int(bet)
      if (money > 0):
        print ("Now you have %s dollars! " %  money) 
      else:
        print("You have no money left!")
        print("GAME OVER")

#Game 1 : Flip a coin
def coin_flip(bet, guess):
  choice = 0
  global money
  num = random.randint(1, 2)  
  print("Welcome to flip a coin!") 
  print("=======================")
  print("Let's flip it.")
  print("Your guess is %s." %guess)
  if (bet < 0 or bet > money):
    check_bet(bet, guess)
  else:
    if (guess == "Heads" or guess == "heads"):
      choice = 1
      win_lose(choice, num, bet)
    elif (guess == "Tails" or guess == "tails"):
      choice = 2
      win_lose(choice, num, bet)
    else:
      print ("Please inform Heads or Tails!")
      
      
#Game 2: Cho Han
def cho_han (bet, guess):
  global money
  dice1 = random.randint(1,6)
  dice2 = random.randint(1,6)
  sum_dice = dice1 + dice2
  result = ""
  print("")
  print("Welcome to Cho Han")
  print("===================")
  print("Let's roll the dice")
  print("the results are %s and %s." % (dice1, dice2))
  
  if (sum_dice % 2 == 0):
    result = "Even"
  else:
    result = "Odd"
  if (bet < 0 or bet > money):
    check_bet(bet, guess)
  else:
    win_lose(guess, result, bet)

# cards with two players
money1 = 400
money2 = 400
def card(bet):
  
  global money1, money2
  
  player1 = random.randint(1,9)
  player2 = random.randint(1,9)
  print("")
  print("Game of Cards")
  print("=============")
  print("Player 1 got %s" % player1)
  print("Player 2 got %s" % player2)
  if (player1 > player2):
    print("Player 1 wins!")
    money1 += bet
    money2 -= bet
    print("You have %s dollars" %money1)
    
  elif (player2 > player1):
    print("Player 2 wins!")
    money2 += bet
    money1 += bet
    print("You have %s dollars" %money2)
  else:
    print("It's a tie!")
  
def roulette(guess, bet):
  global money
  spot = random.randint(0,36)
  print("")
  print("Welcome to Roulette")
  print("===================")
  if (bet < 0 or bet > money): 
    check_bet(bet, guess)
  else:
    print("You are betting %s dollars on %s." % (bet, guess))
    print ("%s came up." % spot)
    if (guess == spot):
      print ("You win!")
      money += bet * 10
      print (" Now you got %s dollars." % money)
    elif ((guess == "Even") or (guess =="even")):
      if (spot % 2 == 0):
        print ("You win!")
        money += bet
        print("You have %s dollars." % money)
      else:
        print ("You lose!")
        money -= bet
        print("You have %s dollars." % money)
    elif(guess == "Odd" or guess == "odd"):
      if (spot % 2 != 0):
        print ("You win!")
        money += bet
        print("You have %s dollars." % money)
      else:
        print ("You lose!")
        money -= bet
        print("You have %s dollars." % money)
    else:
      print ("You lose!")
      money -= bet
      print("You have %s dollars." % money)
    
  




#Call your game of chance functions here
coin_flip(50, "Heads")
cho_han(50, "Even")
card(100)
roulette(15, 50)
