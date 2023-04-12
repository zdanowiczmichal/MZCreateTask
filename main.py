import random
from playsound import playsound
c = []


class Color:
  GREEN = '\033[92m'
  RED = "\033[91m"
  BOLD = '\033[1m'
  END = '\033[0m'
  CYAN = '\033[96m'

class Player:
  #player class for keeping track of position, health, and score
  def __init__(self, positionX, positionY, score):
    self.positionX = positionX
    self.positionX = positionX
    self.positionY = positionY
    self.k = ""
    self.score = score

  def swerve2(self):
    self.k = str(input("Move"))
    if self.k == "w":
      if player.positionY != 0:
        if c[player.positionY - 1][player.positionX] == " " or c[player.positionY -1][player.positionX] == (Color.GREEN + "E" + Color.END):player.positionY -= 1
        elif c[player.positionY - 1][player.positionX] == sedon.look():
          print("Shhh don't let him see you!")
        else:
          print("That's not empty!")
      else:
        print("Cannot move there!")
    elif self.k == "d":
      if player.positionX != len(c) - 1:
        if c[player.positionY][player.positionX + 1] == " " or c[player.positionY][player.positionX + 1] == (Color.GREEN + "E" + Color.END):player.positionX += 1
        elif c[player.positionY][player.positionX + 1] == sedon.look():
          print("Shhh don't let him see you!")
        else:
          print("That's not empty!")
      else:
        print("Cannot move there!")
    elif self.k == "s":
      if player.positionY != len(c) - 1:
        if c[player.positionY + 1][player.positionX] == " " or c[player.positionY + 1][player.positionX] == (Color.GREEN + "E" + Color.END):player.positionY += 1
        elif c[player.positionY + 1][player.positionX] == sedon.look():
          print("Shhh don't let him see you!")
        else:
          print("That's not empty!")
      else:
        print("Cannot move there!")
    elif self.k == "a":
      if player.positionX != 0:
        if c[player.positionY][player.positionX - 1] == " " or c[player.positionY][player.positionX - 1] == (Color.GREEN + "E" + Color.END):player.positionX -= 1
        elif c[player.positionY][player.positionX - 1] == sedon.look():
          print("Shhh don't let him see you!")
        else:
          print("That's not empty!")
      else:
        print("Cannot move there!")
    else:
      print("ERROR: INVALID INPUT")


class Sedon:

  def __init__(self, positionX, positionY, view):
    self.positionX = positionX
    self.positionY = positionY
    self.view = view
    self.k = -1
    self.chase = False

  def look(self):
    if self.view == "N":
      self.k = 0
      return "^"
    elif self.view == "E":
      self.k = 1
      return ">"
    elif self.view == "S":
      self.k = 2
      return "v"
    else:
      self.k = 3
      return "<"

  def swerve(self):
    if self.k == 0:
      if sedon.positionY!= 0:
        temp = sedon.positionY
        while temp > -1:
          if c[temp][sedon.positionX] == (Color.RED + "-" + Color.END):
            temp = -1
          elif c[temp][sedon.positionX] == "X":
            self.chase = True
            print(Color.RED + "I've got you now!" + Color.END)
            playsound('sedonYes.wav')
          temp -= 1
        if c[sedon.positionY - 1][sedon.positionX] == " ":
          sedon.positionY -= 1
    elif self.k == 1:
      if sedon.positionX != len(c) - 1:
        temp = sedon.positionX
        while temp < len(c):
          if c[sedon.positionY][temp] == (Color.RED + "-" + Color.END):
            temp = len(c)
          elif c[sedon.positionY][temp] == "X":
            self.chase = True
            print(Color.RED + "I've got you now!" + Color.END)
            playsound('sedonYes.wav')
          temp += 1
        if c[sedon.positionY][sedon.positionX + 1] == " ":
          sedon.positionX += 1
    elif self.k == 2:
      if sedon.positionY != len(c) - 1:
        temp = sedon.positionY
        while temp < len(c):
          if c[temp][sedon.positionX] == (Color.RED + "-" + Color.END):
            temp = len(c)
          elif c[temp][sedon.positionX] == "X":
            self.chase = True
            print(Color.RED + "I've got you now!" + Color.END)
            playsound('sedonYes.wav')
          temp += 1
        if c[sedon.positionY + 1][sedon.positionX] == " ":
          sedon.positionY += 1
    else:
      if sedon.positionX != 0:
        temp = sedon.positionX
        while temp > -1:
          if c[sedon.positionY][temp] == (Color.RED + "-" + Color.END):
            temp = -1
          elif c[sedon.positionY][temp] == "X":
            self.chase = True
            print(Color.RED + "I've got you now!" + Color.END)
            playsound('sedonYes.wav')
          temp -= 1
        if c[sedon.positionY][sedon.positionX - 1] == " ":
          sedon.positionX -= 1

  def aI(self):
    if sedon.k == 0:
      if sedon.positionY != 0 and c[sedon.positionY - 1][sedon.positionX] != (Color.GREEN + "E" + Color.END) and c[sedon.positionY - 1][sedon.positionX] != (Color.CYAN + "O" + Color.END):
        if c[sedon.positionY - 1][sedon.positionX] == " ":
          sedon.view = "N"
      else:
        list1 = ["W", "S", "E"]
        if sedon.positionX == 0:
          list1.remove("W")
        if sedon.positionX == len(c) - 1:
          list1.remove("E")
        if sedon.positionY == len(c) - 1:
          list1.remove("S")
        r = random.randint(0, len(list1) - 1)
        sedon.view = list1[r]
    elif sedon.k == 1:
      if sedon.positionX != len(c) - 1 and c[sedon.positionY][sedon.positionX + 1] != (Color.GREEN + "E" + Color.END) and c[sedon.positionY][sedon.positionX + 1] != (Color.CYAN + "O" + Color.END):
        if c[sedon.positionY][sedon.positionX + 1] == " ":
          sedon.view = "E"
      else:
        list1 = ["W", "S", "N"]
        if sedon.positionX == 0:
          list1.remove("W")
        if sedon.positionY == 0:
          list1.remove("N")
        if sedon.positionY == len(c) - 1:
          list1.remove("S")
        r = random.randint(0, len(list1) - 1)
        sedon.view = list1[r]
    elif sedon.k == 2:
      if sedon.positionY != len(c) - 1 and c[sedon.positionY + 1][sedon.positionX] != (Color.GREEN + "E" + Color.END) and c[sedon.positionY + 1][sedon.positionX] != (Color.CYAN + "O" + Color.END):
        if c[sedon.positionY + 1][sedon.positionX] == " ":
          sedon.view = "S"
      else:
        list1 = ["W", "E", "N"]
        if sedon.positionX == 0:
          list1.remove("W")
        if sedon.positionY == 0:
          list1.remove("N")
        if sedon.positionX == len(c) - 1:
          list1.remove("E")
        r = random.randint(0, len(list1) - 1)
        sedon.view = list1[r]
    else:
      if sedon.positionX != 0 and c[sedon.positionY][sedon.positionX - 1] != (Color.GREEN + "E" + Color.END) and c[sedon.positionY][sedon.positionX - 1] != (Color.CYAN + "O" + Color.END):
        if c[sedon.positionY][sedon.positionX - 1] == " ":
          sedon.view = "W"
      else:
        list1 = ["E", "S", "N"]
        if sedon.positionX == len(c) - 1:
          list1.remove("E")
        if sedon.positionY == 0:
          list1.remove("N")
        if sedon.positionY == len(c) - 1:
          list1.remove("S")
        r = random.randint(0, len(list1) - 1)
        sedon.view = list1[r]
def board(i, j, dead):
  endX, endY = 4, 4
  wallX0, wallY0 = 1, 1
  wallX1, wallY1 = 2, 1
  wallX2, wallY2 = 3, 1
  if not sedon.chase:
    print(Color.RED + "===========================" + Color.END)
  for y in range(i):
    cList = []
    for x in range(j):
      if player.positionX == x and player.positionY == y and dead:
        cList.append("/")
      elif player.positionX == x and player.positionY == y:
        cList.append("X")
      elif sedon.positionX == x and sedon.positionY == y:
        cList.append(Color.RED + sedon.look() + Color.END)
      #elif startX == x and startY == y:
        #cList.append("S")
      elif endX == x and endY == y:
        cList.append((Color.GREEN + "E" + Color.END))
      elif (wallX0 == x and wallY0 == y) or (wallX1 == x and wallY1 == y) or (wallX2 == x and wallY2 == y):
        cList.append((Color.RED + "-" + Color.END))
      else:
        cList.append(" ")
    c.append(cList)
    if not sedon.chase:
      print((Color.RED + "|" + Color.END), end="")
      for x in cList:
        print(f"'{x}'", end=", ")
      print("", end=(Color.RED + "|\n" + Color.END))
  if not sedon.chase:
    print(Color.RED + "===========================" + Color.END)


def game1():
  k = 0
  print(
    "Type in w, a, s, or d to move. You cannot move on the \"-\", those are walls!"
  )
  while k < 1:
    if player.positionX == sedon.positionX and player.positionY == sedon.positionY:
      print(Color.RED + "I've got you now!" + Color.END)
      playsound('sedonYes.wav')
      return 0
    board(5, 5, False)
    if sedon.chase:
      return 0
    player.swerve2()
    sedon.aI()
    r = random.randint(0,3)
    if r != 0:
      sedon.swerve()
    else:
      list1 = ["N", "S", "E", "W"]
      list1.remove(str(sedon.view))
      sedon.view = list1[random.randint(0, len(list1) - 1)]
    player.score += 1
    if c[player.positionY][player.positionX] == (Color.GREEN + "E" + Color.END):
      return 1
    if not sedon.chase:
      print("I'm gonna get ya!")
    c.clear()


#----------------------------------------------------------------------------------------------------------------------------------#
#COMMENTS!
#Turkey!
#Don't talk to me before I have my coffee!
#Shut up.
#No.
#SOLOMON! Stop playing minecraft ._.
#Cry about it.

print(
  Color.RED + " ██▀███   █    ██  ███▄    █      █████▒██▀███   ▒█████   ███▄ ▄███▓     ██████ ▓█████ ▓█████▄  ▒█████   ███▄    █ "
  "\n▓██ ▒ ██▒ ██  ▓██▒ ██ ▀█   █    ▓██   ▒▓██ ▒ ██▒▒██▒  ██▒▓██▒▀█▀ ██▒   ▒██    ▒ ▓█   ▀ ▒██▀ ██▌▒██▒  ██▒ ██ ▀█   █ "
  "\n▓██ ░▄█ ▒▓██  ▒██░▓██  ▀█ ██▒   ▒████ ░▓██ ░▄█ ▒▒██░  ██▒▓██    ▓██░   ░ ▓██▄   ▒███   ░██   █▌▒██░  ██▒▓██  ▀█ ██▒"
  "\n▒██▀▀█▄  ▓▓█  ░██░▓██▒  ▐▌██▒   ░▓█▒  ░▒██▀▀█▄  ▒██   ██░▒██    ▒██      ▒   ██▒▒▓█  ▄ ░▓█▄   ▌▒██   ██░▓██▒  ▐▌██▒"
  "\n░██▓ ▒██▒▒▒█████▓ ▒██░   ▓██░   ░▒█░   ░██▓ ▒██▒░ ████▓▒░▒██▒   ░██▒   ▒██████▒▒░▒████▒░▒████▓ ░ ████▓▒░▒██░   ▓██░"
  "\n░ ▒▓ ░▒▓░░▒▓▒ ▒ ▒ ░ ▒░   ▒ ▒     ▒ ░   ░ ▒▓ ░▒▓░░ ▒░▒░▒░ ░ ▒░   ░  ░   ▒ ▒▓▒ ▒ ░░░ ▒░ ░ ▒▒▓  ▒ ░ ▒░▒░▒░ ░ ▒░   ▒ ▒ "
  "\n  ░▒ ░ ▒░░░▒░ ░ ░ ░ ░░   ░ ▒░    ░       ░▒ ░ ▒░  ░ ▒ ▒░ ░  ░      ░   ░ ░▒  ░ ░ ░ ░  ░ ░ ▒  ▒   ░ ▒ ▒░ ░ ░░   ░ ▒░"
  "\n  ░░   ░  ░░░ ░ ░    ░   ░ ░     ░ ░     ░░   ░ ░ ░ ░ ▒  ░      ░      ░  ░  ░     ░    ░ ░  ░ ░ ░ ░ ▒     ░   ░ ░ "
  "\n   ░        ░              ░              ░         ░ ░         ░            ░     ░  ░   ░        ░ ░           ░ "
  "\n                                                                                      ░                          "
+ Color.END)
sedon = Sedon(3, 3, "")
player = Player(0, 0, 0)
choice = (input("Press any key, followed by" + Color.BOLD + " ENTER" +
                Color.END + " to play."))
survive = game1()
board(5, 5, True)
if survive == 0:
  print(Color.RED + "Game Over", "\nSurvived:", player.score,
        "turns" + Color.END)
else:
  print(Color.GREEN + "You Won!", "\nSurvived:", player.score,
        "turns" + Color.GREEN)
