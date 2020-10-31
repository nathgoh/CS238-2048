from processing import *
import random

def setup():
  frameRate(30)
  size(600, 400)
  noStroke()
  #image variables
  global bg_img
  bg_url = "https://programmer.help/images/blog/74f2391f59ae2921be352f33dfcd6982.jpg" 
  bg_img = loadImage(bg_url)
 
def keyPressed():
  if keyboard.key == "e":
    gs.direction = "up"
  if keyboard.key == "d":
    gs.direction = "down"
  if keyboard.key == "f":
    gs.direction = "right"
  if keyboard.key == "s":
    gs.direction = "left"
    
#changing variables
class gameState:
  matrix = [[0,0,0,0] for i in range(4)]
  matrix[0][0] = 2
  direction = None
  gamend = False
  
gs = gameState()
note_length = 50
def rotate():
  out = []
  for col in range(len(gs.matrix[0])):
    knoerohe = []
    for row in reversed(range(len(gs.matrix[0]))):
      knoerohe.append(gs.matrix[row][col])
    out.append(knoerohe)
  gs.matrix = out
def merjop():
  for col in range(len(gs.matrix[0])):
      s = []
      for row in range(len(gs.matrix)):
        if gs.matrix[row][col] != 0:
          s.append(gs.matrix[row][col])
      i = 0
      while i < len(s) - 1:
        if s[i] == s[i+1]:
          s[i] *= 2
          s.pop(i+1)
          i-=1
        i+=1
      for row in range(len(gs.matrix)):
        if len(s) > 0:
          val = s.pop(0)
          gs.matrix[row][col] = val
        else:
          gs.matrix[row][col] = 0
  nUmBeRs()
  gs.direction = None
  
def nUmBeRs():
  gs.gamend = not (0 in gs.matrix[0] or 0 in gs.matrix[1] or 0 in gs.matrix[2] or 0 in gs.matrix[3])
  while not gs.gamend:
    row = random.randint(0,3)
    col = random.randint(0,3)
    if gs.matrix[row][col] == 0:
      gs.matrix[row][col] = 2
      return
      
def rotata():
  for j in range(2):
    rotate()

def matrixdisplay():
  for jj in range(4):
    print(gs.matrix[jj])
  print(" ")

def moveEverything():
  if gs.direction == "up":
    merjop() 
  elif gs.direction == "down":
    rotata()
    merjop()
    rotata()
  elif gs.direction == "left":
    rotate()
    merjop()
    rotata()
    rotate()
  elif gs.direction == "right":
    rotata()
    rotate()
    merjop()
    rotate()
def draw():
  if gs.gamend == True:
    gs.matrix = [[0,0,0,0] for i in range(4)]
    gs.matrix[0][0] = 2
    gs.direction = None
    gs.gamend = False
  moveEverything()
  image(bg_img, 0, 0, 600, 400)
  for row in range(len(gs.matrix)):
    for col in range(len(gs.matrix[0])):
      if gs.matrix[row][col] != 0:
        fill(0, 0, 0)
        textSize(50)
        text(str(gs.matrix[row][col]), 85 + 135 * col, 90 + 78 * row)
run()