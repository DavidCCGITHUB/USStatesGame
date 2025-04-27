from turtle import Turtle
import pandas

FONT = ("Ariel", 8, "bold")

class States(Turtle):
    def __init__(self):
        super().__init__()
        self.successful_list = []
        self.penup()
        self.hideturtle()
        self.data = pandas.read_csv("50_states.csv")
        self.states_list = self.data["state"].to_list()


    def check_state(self,state):
        if state not in self.successful_list:
            if state in self.states_list:
                coordinates = self.data[self.data.state == state]
                cor_x = int(coordinates.x.item())
                cor_y = int(coordinates.y.item())
                self.goto(cor_x,cor_y)
                self.write(f"{state}",False,"center",FONT)
                self.successful_list.append(state)
        else:
            pass





