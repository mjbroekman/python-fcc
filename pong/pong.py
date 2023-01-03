"""A simple game of pong... in Python

From:
    https://www.freecodecamp.org/news/python-projects-for-beginners/#pong-python-project

Skills:
    - Python Turtle

Added items:
    - Parse command-line arguments
    - Customizable player settings (color, size, name)
    - Customizable game settings (background color, size, speed)
    - Object-oriented design
"""
import argparse
import turtle

class Pong():
    def __init__(self, width, height, bgcolor, fgcolor, speed):
        self.board = turtle.Screen()
        self.board.title("Pong")
        self.board.bgcolor(bgcolor)
        self.board.setup(width=width,height=height)
        self.board.tracer(0) # Force us to manually update the window instead of auto-updating
        self._speed = speed
        self.height = height // 2
        self.players = {}
        self.pen = turtle.Turtle()
        self.pen.speed(0)
        self.pen.color(fgcolor)
        self.pen.penup()
        self.pen.hideturtle()
        self.pen.goto(0, int(height*0.85))
    
    def set_player(self,player:'PongPlayer',moves:list):
        player_id = len(self.players.items())
        self.players[player_id] = player
        self.board.onkeypress(self.players[player_id].move_up,moves[0])
        self.board.onkeypress(self.players[player_id].move_down,moves[1])

    def drop_puck(self,pucksize:int,puckcolor:str):
        self.puck = PongPuck(pucksize,puckcolor,self.board.window_width(),self.board.window_height(),self._speed)

    def update_score(self):
        self.pen.clear()
        self.pen.write("{}: {}    {}: {}".format(self.players[0].get_name(),self.players[0].get_score(),self.players[1].get_name(),self.players[1].get_score()),align="center",font=("Courier",24,"normal"))
        self.pen.goto(0, int(self.height*0.85))

    def play(self):
        while(True):
            self.board.update()
            score = self.puck.move(self.players)

            if score == -2:
                # player A scored
                self.players[0].score()
            if score == 2:
                # player B scored
                self.players[1].score()

            self.update_score()
            for player_id in self.players.keys():
                if self.players[player_id].get_score() == "5":
                    print("{} has won!!".format(self.players[player_id].get_name()))
                    print("Final score: {}: {}    {}: {}".format(self.players[0].get_name(),self.players[0].get_score(),self.players[1].get_name(),self.players[1].get_score()))
                    return

    def listen(self):
        self.board.listen()

class PongPuck():
    def __init__(self,pucksize,puckcolor,width,height,speed=1):
        self.puck = turtle.Turtle()
        self.puck.speed(0) # Fastest animation speed
        self.puck.shape("square")
        self.puck.shapesize(stretch_wid=pucksize,stretch_len=pucksize)
        self.puck.color(puckcolor)
        self.puck.penup()
        self.puck.goto(0,0)
        self.dx = 2
        self.dy = 2
        self.speed = speed
        self.max_x = width // 2
        self.min_x = -width // 2
        self.max_y = height // 2
        self.min_y = -height // 2
    
    def move(self,players:dict) -> int:
        puck_x = self.puck.xcor()
        puck_y = self.puck.ycor()

        # Bounce off the ceiling or floor
        if puck_y >= self.max_y or puck_y <= self.min_y:
            self.dy *= -1

        # Bounce hit the left or right side
        if puck_x >= self.max_x or puck_x <= self.min_x:
            self.speed = 1
            self.puck.goto(0,0)
            self.dx *= -1
            # player A == -2, player B == 2
            return self.dx

        else:
            for (name,player) in players.items():
                (left,right) = player.get_x_range()
                (top,bottom) = player.get_y_range()
                if left < 0 and right < 0 and puck_x < 0:
                    # player A bounces
                    if left < (puck_x - 5) <= right and bottom <= puck_y <= top:
                        self.dx *= -1
                        self.speed *= 1.1

                    
                if left > 0 and right > 0 and puck_x > 0:
                    if left <= (puck_x + 5) < right and bottom <= puck_y <= top:
                        self.dx *= -1
                        self.speed *= 1.1

            self.puck.setx(puck_x + ( self.dx * self.speed))
            self.puck.sety(puck_y + ( self.dy * self.speed))

        return 0

        
class PongPlayer():
    def __init__(self,player_name,player_size,player_color,start,board_height,speed=1):
        self.player = turtle.Turtle()
        self.player.speed(0)
        self.player.shape("square")
        self.player.shapesize(stretch_wid=player_size,stretch_len=1)
        self.player.color(player_color)
        self.player.penup()
        self.player.goto(start,0)
        self.name = player_name
        self.length = 20 * player_size
        self.max_y = board_height // 2
        self.min_y = -board_height // 2
        self.speed = speed
        self._score = 0

    def move_up(self):
        y = self.player.ycor()
        y += 10 * self.speed
        if y < self.max_y:
            self.player.sety(y)

    def move_down(self):
        y = self.player.ycor()
        y -= 10 * self.speed
        if y > self.min_y:
            self.player.sety(y)

    def get_y_range(self):
        return ( self.player.ycor() + (self.length // 2), self.player.ycor() - (self.length // 2 ) )

    def get_x_range(self):
        return ( self.player.xcor() - 10, self.player.xcor() + 10 )

    def get_name(self) -> str:
        return str(self.name)

    def get_score(self) -> str:
        return str(self._score)

    def score(self):
        self._score += 1
        self.speed *= 1.1

parser = argparse.ArgumentParser(description="A 'simple' game of Pong... in Python.")
# Board options
parser.add_argument("--height","-y",action="store",type=int,help="Height (y dimension) of board.",default=600)
parser.add_argument("--width","-x",action="store",type=int,help="Width (x dimension) of the board",default=800)
parser.add_argument("--bgcolor","-b",action="store",help="Background color",default="black")
parser.add_argument("--fgcolor","-f",action="store",help="Color of the text on the screen",default="white")
# Player 1 options
parser.add_argument("--player1","-1",action="store",help="Name of Player 1", default="Player1")
parser.add_argument("--p1color","-p",action="store",help="Player 1 color",default="white")
parser.add_argument("--p1size","-s",action="store",type=int,help="Player 1 paddle size multiplier",default=5)
parser.add_argument("--p1up","-u",action="store",help="Key to move player 1 up",default="w")
parser.add_argument("--p1down","-l",action="store",help="Key to move player 1 down",default="s")
# Player 2 options
parser.add_argument("--player2","-2",action="store",help="Name of Player 1", default="Player2")
parser.add_argument("--p2color","-P",action="store",help="Player 2 color",default="white")
parser.add_argument("--p2size","-S",action="store",type=int,help="Player 2 paddle size multiplier",default=5)
parser.add_argument("--p2up","-U",action="store",help="Key to move player 1 up",default="i")
parser.add_argument("--p2down","-L",action="store",help="Key to move player 1 down",default="k")
# Puck options
parser.add_argument("--puck","-k",action="store",help="Puck color",default="white")
parser.add_argument("--pucksize","-z",action="store",type=int,help="Puck size multiplier",default=1)
parser.add_argument("--speed","-d",action="store",type=int,help="Speed of the puck",default=1)

args = parser.parse_args()

board = Pong(width=args.width,height=args.height,bgcolor=args.bgcolor,fgcolor=args.fgcolor,speed=args.speed)
board.listen()

try:
    board.set_player(PongPlayer(args.player1,args.p1size,args.p1color,((-args.width//2) + 10),args.height),[args.p1up,args.p1down])
    board.set_player(PongPlayer(args.player2,args.p2size,args.p2color,(( args.width//2) - 10),args.height),[args.p2up,args.p2down])
    board.drop_puck(args.pucksize,args.puck)
except Exception as e:
    print("Configuration error setting up the game." + str(e))
else:
    # Main game loop
    board.play()
