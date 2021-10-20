from random import randint


import time



class entity:
  def __init__(self):
    self.table=[
          [9,9,9,9,9,9,9,9,9,9,9,9],
          [9,0,0,0,0,0,0,0,0,0,0,9],
          [9,0,0,0,0,0,0,0,0,0,0,9],
          [9,0,0,0,0,0,0,0,0,0,0,9],
          [9,0,0,0,0,0,0,0,0,0,0,9],
          [9,0,0,0,0,0,0,0,0,0,0,9],
          [9,0,0,0,0,0,0,0,0,0,0,9],
          [9,0,0,0,0,0,0,0,0,0,0,9],
          [9,0,0,0,0,0,0,0,0,0,0,9],
          [9,0,0,0,0,0,0,0,0,0,0,9],
          [9,0,0,0,0,0,0,0,0,0,0,9],
          [9,9,9,9,9,9,9,9,9,9,9,9]
          ]
    #0 for empty , 1 for ship part , 2 for water hit , 3 and 4 for ship hit , 9 for border
    self.pieces=[4,3,2,1]
    self.lives=20

  def displayMap(self):
    print("     1   2   3   4   5   6   7   8   9   10 ")
    print("   ╔═══╦═══╦═══╦═══╦═══╦═══╦═══╦═══╦═══╦═══╗")
    for i in range(1,11):
      print(str(i).rjust(2),"║",end="")
      for j in range(1,11):
        if self.table[i][j]==0:
          print("   ║",end="")
        elif self.table[i][j]==1:
          print(" ■ ║",end="")
        elif self.table[i][j]==2:
          print(" ~ ║",end="")
        elif self.table[i][j]==3 or self.table[i][j]==4:
          print(" X ║",end="")
      print("")
      if(i<10):
        print("   ╠═══╬═══╬═══╬═══╬═══╬═══╬═══╬═══╬═══╬═══╣")
    print("   ╚═══╩═══╩═══╩═══╩═══╩═══╩═══╩═══╩═══╩═══╝")

  def displayEnemyView(self):
    print("     1   2   3   4   5   6   7   8   9   10 ")
    print("   ╔═══╦═══╦═══╦═══╦═══╦═══╦═══╦═══╦═══╦═══╗")
    for i in range(1,11):
      print(str(i).rjust(2),"║",end="")
      for j in range(1,11):
        if self.table[i][j]==0 or self.table[i][j]==1:
          print("   ║",end="")
        elif self.table[i][j]==2:
          print(" ~ ║",end="")
        elif self.table[i][j]==3:
          print(" ■ ║",end="")
        elif self.table[i][j]==4:
          print(" X ║",end="")
      print("")
      if(i<10):
        print("   ╠═══╬═══╬═══╬═══╬═══╬═══╬═══╬═══╬═══╬═══╣")
    print("   ╚═══╩═══╩═══╩═══╩═══╩═══╩═══╩═══╩═══╩═══╝")

  def generateShipsPositions(self):
    for i in range(len(self.pieces)-1,-1,-1):
      while(self.pieces[i]):
        while(1):
          x=randint(1,10)
          y=randint(1,10)
          orientation=randint(0,1)
          height=orientation*(i+1+2)+(1-orientation)*3
          lenght=orientation*3+(1-orientation)*(i+1+2)
          placeable=True
          if x-1+height>12 or y-1+lenght>12:
            placeable=False
          else:
            for posx in range (x-1,x-1+height):
              for posy in range(y-1,y-1+lenght):
                if  self.table[posx][posy]==1:
                  placeable=False
          if placeable==True:
            for posx in range(x,x+height-2):
              for posy in range(y,y+lenght-2):
                self.table[posx][posy]=1;
            break;
        self.pieces[i]-=1;

  def placeShips(self):
    score=0
    while(score!=self.lives):
      answer=0
      correct_answer=False
      size=0
      orientation=0
      x=0
      y=0
        #while(correct_answer==False):
      while(answer!="Place"and answer!="Redo" and answer!="Random"):
        print("\n"*40)
        self.displayMap()
        print("""Place a ship?(Write "Place")""")
        #print("""Redo the previous placement?(Write "Redo")""")
        print("""Are you bored of placing ships?(Write "Random")""")
        answer=input()
        answer=answer.title()
      if answer=="Place":
        print("\n"*40)
        self.displayMap()
        print("What is the size of the ship ?")
        good_size=False
        size=0;
        while(not good_size):
          size=int(input())
          if len(self.pieces)>=size:
            if self.pieces[size-1]>0:
              good_size=True
          if good_size==False:
            print("You don't have a ship of that dimension .")
            for i in range(len(self.pieces)):
              if self.pieces[i]:
                print("You have",self.pieces[i],"pieces of dimension",i+1,".")
            print("Please write a valid size :",end='')
        print("""What is the orientation of the ship ?("Horizontal"/"Vertical")""")
        orientation=0
        good_orientation=False
        while(not good_orientation):
          orientation=input()
          orientation=orientation.title()
          good_orientation=True
          if orientation != 'Horizontal'and orientation != 'Vertical':
            print("""This is not a valid answer. Please choose between "Horizontal" and "Vertical" """)
            good_orientation=False
        if(orientation=='Horizontal'):
          orientation=0
        else: 
          orientation=1
        print("What is the position on the map of the ship ?(1 1 to 10 10)")
        pos=input()
        x=int(pos[:pos.find(" ")])
        y=int(pos[pos.find(" "):])
        height=orientation*(size+2)+(1-orientation)*3
        lenght=orientation*3+(1-orientation)*(size+2)
        placeable=False
        while(not placeable):
          placeable=True
          if x-1+height>12 or y-1+lenght>12:
                placeable=False
          else:
            for posx in range (x-1,x-1+height):
              for posy in range(y-1,y-1+lenght):
                if  self.table[posx][posy]==1:
                  placeable=False
          if(not placeable):
            print("That is not a placeable position. Try again another position.")
            pos=input()
            x=int(pos[:pos.find(" ")])
            y=int(pos[pos.find(" "):])
        for posx in range(x,x+height-2):
          for posy in range(y,y+lenght-2):
            self.table[posx][posy]=1;
        score+=size
        self.pieces[size-1]-=1
      if answer=='Random':
        score=20
        self.generateShipsPositions()
    
  def ShipDestroyed(self,x,y):
    row_Up=x
    row_Down=x
    collumn_Left=y
    collumn_Right=y
    while(self.table[x][collumn_Left-1]==3):
      collumn_Left-=1
      #print(0)
    while(self.table[x][collumn_Right+1]==3):
      collumn_Right+=1
      #print(1)
    while(self.table[row_Up-1][y]==3):
      row_Up-=1
      #print(2)
    while(self.table[row_Down+1][y]==3):
      row_Down+=1
      #print(3)
    ship_Destroyed=True
    #print(row_Up,row_Down)
    #print(collumn_Left,collumn_Right)
    for posx in range(row_Up,row_Down+1):
      for posy in range(collumn_Left,collumn_Right+1):
        if self.table[posx-1][posy]==1 or self.table[posx+1][posy]==1 or self.table[posx][posy-1]==1 or self.table[posx][posy+1]==1:
          ship_Destroyed=False
    if ship_Destroyed:
      row_Up-=1
      row_Down+=1
      collumn_Left-=1
      collumn_Right+=1
      for posx in range(row_Up,row_Down+1):
        for posy in range(collumn_Left,collumn_Right+1):
          if self.table[posx][posy]==0:
            self.table[posx][posy]=2
          elif self.table[posx][posy]==3:
            self.table[posx][posy]=4
    
  def findGoodLocation(self):
    x=0
    y=0
    n=0
    for x in range (1,11):
      for y in range(1,11):
        if(self.table[x][y]==0 or self.table[x][y]==1):
          if(self.table[x+1][y]==3or self.table[x-1][y]==3or self.table[x][y+1]==3or self.table[x][y-1]==3):
            n=100*x+y
            #print(n)
            #time.sleep(2)
            if x>2:
              if self.table[x-2][y]==3:
                return n
            if y>2:
              if self.table[x][y-2]==3:
                return n
            if x<9:
              if self.table[x+2][y]==3:
                return n
            if y<9:
              if self.table[x][y+2]==3:
                return n
    while(n==0):
      x=randint(1,11)
      y=randint(1,11)
      if(self.table[x][y]==0 or self.table[x][y]==1):
        n=100*x+y
    return n     
      
bot=entity()

player=entity()

print('BattleShips 0.5')
bot.generateShipsPositions()
print()
player.placeShips()
start=time.time()
last=0
while(1):
  now=time.time()
  if(5-now+start)<0:
    break
  if(int(now-start)>last):
    print("\n"*60)
    player.displayMap()
    print("You finished your map. Now you are ready to start the game.")
    print("The game starts in",5-int(now-start),"seconds!")
    last=int(now-start)
turn=randint(0,1)

while(player.lives>0 and bot.lives>0):
  x=0
  y=0
  print("\n"*60)
  player.displayMap()
  print("This is your map.")
  bot.displayEnemyView()
  print("Above is enemy's visible map.")
  if(turn==0):
    print("Now is your turn. Where do you want to fire?")
    pos=input()
    x=int(pos[:pos.find(" ")])
    y=int(pos[pos.find(" "):])
    good_location=False
    while(not good_location):
      if(x>=1 and x<=10 and y>=1 and y<=10 and(bot.table[x][y]==0 or bot.table[x][y]==1)):
        good_location=True
      if not good_location:
        print("You can't fire there. That location is known or you already shoot there.")
        pos=input()
        x=int(pos[:pos.find(" ")])
        y=int(pos[pos.find(" "):])
    if(bot.table[x][y]==1):
      bot.lives-=1
      bot.table[x][y]=3
      turn= not turn
      bot.ShipDestroyed(x,y)
    elif bot.table[x][y]==0:
      bot.table[x][y]=2
  elif(turn==1):
    print("Now is your enemy's turn.")
    time.sleep(0.5)
    n=player.findGoodLocation()
    x=int(n/100)
    y=n%100
    if(player.table[x][y]==1):
      player.lives-=1
      player.table[x][y]=3
      turn= not turn
      player.ShipDestroyed(x,y)
    elif player.table[x][y]==0:
      player.table[x][y]=2
  turn= not turn

print("\n"*60)
player.displayMap()
print("This is your map.")
bot.displayMap()
print("Above is enemy's  map.")
if player.lives==0:
  print("You lost!")
else:
  print("You won!")

