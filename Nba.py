from dataclasses import dataclass
import random
import time, os, sys


def clearScreen():
    os.system("clear")

def typingPrint(text):
    for character in text:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)
def leaderboard(i,x,y,player1):
  w = i * 50
  
  with open("Leaderboard.txt", 'a') as X:
   X.write(f"{w} {x} {y} {player1}\n")
def print_leaderboard():
   i = 0
   list1 = []
   with open("Leaderboard.txt", 'r') as X:
     name = X.readlines()
   for x in name:
     y = x.split()
     list1.append(int(y[0]))
     list1.sort()
   print("         LEADERBOARD")
   print("------------------------------")
   for x in list1:
     i += 1
     
     for y in name:
       y = y.split()
       if x == int(y[0]):
         
         print(f"{i}. user: {y[-1]} - Score: {y[0]}")





  
  
def loading(): 
  print("5%   █")
  time.sleep(.2)
  clearScreen()
  print("10%  ██")
  time.sleep(.2)
  clearScreen()
  print("15%  ███")
  time.sleep(.2)
  clearScreen()
  print("20%  ████") 
  time.sleep(.2)
  clearScreen()
  print("25%  █████")
  time.sleep(.2)
  clearScreen()
  print("30%  ██████") 
  time.sleep(.2)
  clearScreen()
  print("35%  ███████")
  time.sleep(.2)
  clearScreen()
  print("40%  ████████") 
  time.sleep(.2)
  clearScreen()
  print("45%  █████████")
  time.sleep(.2)
  clearScreen()
  print("50%  ██████████")
  time.sleep(.2)
  clearScreen()
  print("55%  ███████████")
  time.sleep(.2)
  clearScreen()
  print("60%  ████████████")
  time.sleep(.2)
  clearScreen()
  print("65%  █████████████")
  time.sleep(.2)
  clearScreen()
  print("70%  ██████████████") 
  time.sleep(.2)
  clearScreen()
  print("75%  ███████████████")
  time.sleep(.2)
  clearScreen()
  print("80%  ████████████████")
  time.sleep(.2)
  clearScreen()
  print("85%  █████████████████")
  time.sleep(.2)
  clearScreen()
  print("90%  ██████████████████") 
  time.sleep(.2)
  clearScreen()
  print("95%  ███████████████████")
  time.sleep(.2)
  clearScreen()
  print("100% ████████████████████")
  time.sleep(.2)
  clearScreen()
  typingPrint("Starting game")
  time.sleep(2)


@dataclass
class Player:
  name: str
  three: int
  dunk: int
  layup: int
  mid: int
@dataclass
class CPU:
  name: str
  three: int
  dunk: int
  layup: int
  mid: int

@dataclass
class Skills:
  three: int
  dunk: int
  layup: int
  mid: int

RealPSkill = { 
#Bucks
"Jrue Holiday": Skills(3, 4, 2, 2), 
"Wesley Matthews": Skills(2,3,4,2),
"Khris Middleton": Skills(2, 2, 2, 2), 
"Giannis Antetokounmpo": Skills(6, 2, 2, 3), 
"Brook Lopez": Skills(6, 2, 2, 3),
#Celtics
"Marcus Smart": Skills(4, 3, 2, 2), 
"Jalen Brown": Skills(2, 3, 2, 2), 
"Jayson Tatum": Skills(3, 2, 2, 2),
"Al Horford": Skills(2,2,2,4),
"Robert Williams": Skills(7, 4, 3, 6),
#Grizzlies
"Ja Morant": Skills( 3, 3, 2, 2),
"Desmond Bane": Skills( 3, 3, 4, 3),
"Dillon Brookes": Skills( 4, 3, 3, 4),
"Jaren Jackson Jr.": Skills( 5, 3, 3, 3),
"Steven Adams": Skills( 6, 2, 2, 5),
#Hawks
"Trae Young": Skills( 2, 6, 3, 2),
"Kevin Huerter": Skills( 4, 3, 2, 3),
"De'Andre Hunter": Skills( 4, 4, 2, 4),
"John Collins": Skills( 4, 3, 3, 3),
"Clint Capela": Skills( 6, 3, 2, 5),
#Heat
"Kyle Lowry": Skills(3, 7, 3, 3),
"Duncan Robinson": Skills( 4, 3, 3, 2),
"Jimmy Butler": Skills( 3, 2, 2, 2),
"P.J. Tucker": Skills( 7, 6, 4, 4),
"Bam Adebayo": Skills( 3, 2, 2, 3),
#Lakers
"Russell Westbrook": Skills(4, 2, 2, 2),
"Austin Reaves": Skills(3,3,4,3),
"LeBron James": Skills(2, 2, 2, 2),
"Stanley Johnson": Skills(4,3,3,4),
"Anthony Davis": Skills(3, 2, 2, 3),
#Mavericks
"Luka Doncic": Skills( 2, 2, 2, 2),
"Jalen Brunson": Skills( 2, 2, 3, 3),
"Reggie Bullock": Skills( 3, 3, 3, 3),
"Dorian Finney-Smith": Skills( 4, 3, 3, 4),
"Dwight Powell":Skills( 4, 3, 3, 3),
#Nets
"Kyrie Irving": Skills(2, 5, 2, 2),
"James Harden": Skills(2, 4, 2, 2),
"Kevin Durant": Skills(2, 2, 2, 2),
"Ben Simmons": Skills(8, 2, 2, 5),
"Andre Drummond": Skills(5, 2, 2, 3),
#Suns
"Chris Paul": Skills(2, 8, 2, 2),
"Devin Booker": Skills(2, 4, 2, 3),
"Mikal Bridges": Skills(5, 2, 2, 4),
"Jae Crowder": Skills(4, 3, 3, 4),
"Deandre Ayton": Skills(5, 2, 2, 3),
#Warriors
"Stephen Curry": Skills(2, 7, 2, 3),
"Jordan Poole": Skills(2,3,3,2),
"Klay Thompson": Skills(2, 7, 2, 3),
"Andrew Wiggins": Skills(4, 2, 2, 3),
"Draymond Green": Skills(4, 2, 3, 3),
}


team_list = [
  "Bucks",
  "Celtics",
  "Grizzlies",
  "Hawks",
  "Heat",
  "Lakers",
  "Mavericks",
  "Nets",
  "Suns",
  "Warriors"
]

play_options = [
  "dunk",
  "layup",
  "mid",
  "three"
]


def main():
  user_players = []
  cpu_players = []
  pos = "o"
  user = Player("",0,0,0,0)
  cpu1 = CPU("",0,0,0,0)
  #Introduction
  print("Welcome to the NBA Arcade Game!")
  print("This is a game where you play a 1 on 1 blacktop game to 21. You will pick one player from any of the provided teams and play against your opponent.")
  
  s = input("Press [s] to start.\n>")
  while s != "s":
    
    s = input("Press [s] to start.\n>")
  print()
  #User Team selector
  player1 = input("Username: ")
  print()
  print("Here are the teams you can choose from:")
  for names in team_list:
    print(names)
  while True:
    choice = input(">")
    try:
      with open(f"{choice}.txt", "r") as file:
        player_choices = file.readlines()
        for players in player_choices:
          players = players.strip()
          user_players.append(players)
      print()
      print(f"Starting 5 for the {choice}:")
      for players in user_players:
        print(players)
      break
    except FileNotFoundError:
      print("Please choose one of the provided teams")
  print()

      
  while choice not in players:
      choice = input("Who do you want to play as?\n> ")
      if choice in user_players:
        for names in user_players:
          if choice == names:
            user.name = choice
          for player,n in RealPSkill.items():
            if user.name == player:
              user.three = n.three
              user.layup = n.layup
              user.dunk = n.dunk
              user.mid = n.mid
        break
      else:
        print("Please choose a player from this team.")

  
  #Cpu team selector
  cpu = random.choice(team_list)
  with open(f"{cpu}.txt", "r") as file:
    cpu_choices = file.readlines()
    for cpus in cpu_choices:
      cpus = cpus.strip()
      cpu_players.append(cpus)
      cpu_choice = random.choice(cpu_players)
      cpu1.name = cpu_choice
    for cpu11,n in RealPSkill.items():
            if cpu1.name == cpu11:
              cpu1.three = n.three
              cpu1.layup = n.layup
              cpu1.dunk = n.dunk
              cpu1.mid = n.mid
  print(f"Your opponent chose {cpu1.name} from the {cpu}.\n")

  #Ready to play
  r = input("Press [r]eady.\n>")
  while r != "r":
    r = input("Press [r]eady.\n>")
  clearScreen()
  #loading screen
  loading()
  clearScreen()
  
  user_points = 0
  cpu_points = 0
  i = 0
  #Full gameplay
  while user_points <=21 or cpu_points<=21:
    
    x =user.name
    y = cpu1.name
    #User gameplay
    if pos == "o":
      
      print(f"""
  _______________________________________
   {user.name} |  {cpu1.name}
   {user_points}               {cpu_points}
  _______________________________________
  """)
      print("You have the ball.")
      ui = input("Do you want to take a [dunk] for 2 pts, [layup] for 2 pts, [mid]-range for 2 pts, or [three]-pointer for 3 pts?\n> ")
      i += 1
      if ui == "dunk":
        chance = random.randint(1,user.dunk)
        if chance == 1:
          print(f"{user.name} gets past the {cpu1.name} and gets a dunk off!")
          i += 2
          user_points += 2
          pos = "d"
          time.sleep(1)
        else:
          print(f"{user.name} couldn't get that dunk off. Good defense by {cpu1.name}!")
          pos = "d" 
          time.sleep(1)
      
      elif ui == "layup":
        chance = random.randint(1,user.layup)
        if chance == 1:
          print(f"{user.name} drives to the basket for an easy layup!")
          i += 2
          user_points += 2
          pos = "d"
          time.sleep(1)
        else:
          print(f"{user.name} drives to the hole but gets contested at the rim and misses the layup.")
          pos = "d" 
          time.sleep(1)
          
      elif ui == "mid":
        chance = random.randint(1,user.mid)
        if chance == 1:
          print(f"{user.name} sizes up the defender and makes a mid-range! ")
          i += 2
          user_points += 2
          pos = "d"
          time.sleep(1)
        else:
          print(f"The mid-range doesn't go in for {user.name}.")
          pos = "d"
          time.sleep(1)
          
      elif ui == "three":
        chance = random.randint(1,user.three)
        if chance == 1:
          print(f"{user.name} breaks the defender, shoots an open 3, and makes it!")
          i += 3
          user_points += 3
          pos = "d"
          time.sleep(1)
        else:
          print(f"{cpu1.name} locks up {user.name} so good the shot clock runs out.")
          pos = "d"
          time.sleep(1)

    #Cpu gameplay
    elif pos == "d":    
      cpu_choice = random.choice(play_options)
      print()
      print(f"{cpu1.name} has the ball.")
      time.sleep(2)
      if cpu_choice == "dunk":
        chance = random.randint(1,cpu1.dunk)
        if chance == 1:
          print(f"{cpu1.name} dunks on {user.name}.")
          cpu_points += 2
          pos = "o"
          time.sleep(1.5)
        else:
          print(f"{cpu1.name} tries to dunk and fails horribly")
          pos = "o"
          time.sleep(1.5)
          
      elif cpu_choice == "layup":
        chance = random.randint(1,cpu1.layup)
        if chance == 1:
          print(f"{cpu1.name} makes the wide open layup.")
          cpu_points += 2
          pos = "o"
          time.sleep(1.5)
        else:
          print(f"{cpu1.name} can't get to the basket for a layup.")
          pos = "o"
          time.sleep(1.5)
          
      elif cpu_choice == "mid":
        chance = random.randint(1,cpu1.mid)
        pos = "o"
        time.sleep(1.5)
        if chance == 1:
          print(f"{cpu1.name} takes a mid-range from the corner and swishes it.")
          cpu_points += 2
          pos = "o"
          time.sleep(1.5)
        else:
          print(f"{cpu1.name} takes a contested mid-range and misses.")
          pos = "o"
          time.sleep(1.5)
          
      elif cpu_choice == "three":
        chance = random.randint(1,cpu1.three)
        if chance == 1:
          print(f"{cpu1.name} let's off a wide-open 3 from the top off the key and it goes!")
          cpu_points += 3
          pos = "o"
          time.sleep(1.5)
        else:
          print(f"{cpu1.name} puts up a 3 and it won't go in.")
          pos = "o"
          time.sleep(1.5)
      clearScreen()
    #Game Over/Final Scoreboard
    if user_points >= 21 or cpu_points >= 21:
      if user_points >= 21:
        time.sleep(1)
        clearScreen()
        print(f"Congratulations you beat {cpu1.name}!")
        print(f"""
                      Final Score
        _______________________________________
         {user.name} |  {cpu1.name}
         {user_points}               {cpu_points}
        _______________________________________
        """)
        leaderboard(i,x,y,player1)
        print_leaderboard()
      elif cpu_points >= 21:
        time.sleep(1)
        clearScreen()
        print(f"{cpu1.name} wins. Maybe next time.")
        print(f"""
                      Final Score 
        _______________________________________
         {user.name} |  {cpu1.name}
         {user_points}               {cpu_points}
        _______________________________________
        """)
        print_leaderboard()
      
      break  
        

if __name__ == "__main__":
  main()