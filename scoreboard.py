from turtle import Turtle

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.current_score = 0
        with open('data.txt') as data:
            self.high_score = int(data.read())
        self.color('white')
        self.penup()
        self.goto(0, 260)
        self.hideturtle()
        self.write_scoreboard()

    
    def write_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.current_score} High Score: {self.high_score}", align='center', font=('Arial', 20, 'normal'))


    def increment_score(self):
        self.current_score += 1
        self.write_scoreboard()

    
    def reset(self):
        if self.current_score > self.high_score:
            self.high_score = self.current_score
            with open('data.txt', mode='w') as data:
                data.write(str(self.high_score))
        self.current_score = 0
        self.write_scoreboard()


    # def game_over(self):
    #     self.goto(0, 0)
    #     self.color('red')
    #     self.write(f"GAME OVER", align='center', font=('Arial', 20, 'normal'))