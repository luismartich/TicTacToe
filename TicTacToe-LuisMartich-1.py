import turtle
import random
import sys
s = turtle.Screen()
turtle.setup(width=450, height=450, startx= 900, starty= -300)
s.setworldcoordinates(-10,-310,320,0)

s.bgcolor("gray")
s.title("Welcome to TicTacToe by LuisMartich")
t1 = turtle.Turtle() #blue turtle player 1
t2 = turtle.Turtle() #red turtle player 2
t3 = turtle.Turtle() #black board

def print_board(t): #function to draw the board
  t.color('black')
  t.speed(100)
  def square():
    for i in range(4):
      t.fd(100)
      t.rt(90)
  def set(square):
    for i in range(3):
      square()
      t.fd(100)
      square()
      t.fd(100)
      square()
      t.bk(200)
      t.goto(0,-100*(i+1))
  set(square)
  t.up()


def circle_move(t, index): #Function for every circle turn
  t.color('blue')
  #t.speed(100)
  t.up()
  t.goto(index)
  t.rt(90)
  t.fd(50)
  t.down()
  t.circle(50)
  t.up()
  t.goto(0,0)
  t.lt(90)
  
  
def cross_move(t, index): #Function for every cross move
  t.color('red')
  #t.speed(100)
  t.up()
  t.goto(index)
  t.down()
  t.rt(45)
  t.fd(141.42135)
  t.up()
  t.rt(135)
  t.fd(100)
  t.rt(135)
  t.down()
  t.fd(141.42135)
  t.up()
  t.goto(0,0)
  t.rt(45)

def checkwinner(nums, player):
  List = sorted(nums)
  if (1 in List and 2 in List and 3 in List) or (1 in List and 4 in List and 7 in List) or \
      (3 in List and 6 in List and 9 in List) or (7 in List and 8 in List and 9 in List) or \
      (1 in List and 5 in List and 9 in List) or (3 in List and 5 in List and 7 in List) or \
      (4 in List and 5 in List and 6 in List) or (2 in List and 5 in List and 8 in List):
      won = True
      print("Player " + player + " WON")
      sys.exit()

def draw(win, player, player2):
  if (win == False and len(player)== 4 and len(player2) == 5) or (win == False and len(player)== 5 and len(player2) == 4):
    print("Nobody won - There is a Draw")
    sys.exit()

#Position for every posible move used as index
position = [(0,0),    (100,0),    (200,0),     # 1 ---- 2 ---- 3
            (0,-100), (100,-100), (200,-100),  # 4 ---- 5 ---- 6
            (0,-200), (100,-200), (200,-200)]  # 7 ---- 8 ---- 9

print_board(t3)
print("Welcome to the TicTacToe game by LuisMartich")
print("TicTacToe has 9 positions to play." + '\n' + "Use numbers from 1 to 9 to play the desire position")
mode = input("To pay with the machine input number 1: " + '\n' + "To pay with another human input number 2: " + '\n' )

if mode == 1:
    p1 = []
    machine = []
    won = False
    while True:
        turn1 = int(input("Enter position for player 1 with circle: "))
        if turn1 in p1 or turn1 in machine:
            print("Position already selected, please select an available position")
            continue
        else:
            try:
                circle_move(t1, position[int(turn1)-1])
                p1.append(turn1)
            except:
                print("Wrong position selected. Try again")
                continue
        checkwinner(p1, "1")
        draw(won, p1, machine)
        

        while True:
            pc = random.randrange(1, 10)
            #print("Machine turn - Machine played position ", str(pc))
            if pc in p1 or pc in machine:
                continue
            else:
                print("Machine turn - Machine played position ", str(pc))
                cross_move(t2,position[int(pc)-1])
                machine.append(pc)
            checkwinner(machine, "Machine")
            draw(won, p1, machine)
            break
        if won == False:
            continue
        else:
            break
    
elif mode == 2:
    p1 = [0]
    p2 = [0]
    won = False
    while True:
        turn1 = int(input("Enter position for player 1 with circle: "))
        if turn1 in p1 or turn1 in p2:
            print("Position already selected, please select an available position")
            continue
        else:
            try:
                circle_move(t1, position[int(turn1)-1])
                p1.append(turn1)
            except:
                print("Wrong position selected. Try again")
                continue
        checkwinner(p1, "1")
        while True:
            turn2 = int(input("Enter position for player 2 with X: "))
            if turn2 in p1 or turn2 in p2:
                print("Position already selected, please select an available position")
                continue 
            else:
                try:
                    cross_move(t2,position[int(turn2)-1])
                    p2.append(turn2)
                except:
                    print("Wrong position selected. Try again")
                    continue
            checkwinner(p2, "2")
            break
        if won == False:
            continue
        else:
            break     
else:
    print("Your input is incorrect")

