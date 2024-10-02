# from turtle import Turtle,Screen
#
# t = Turtle()
#
# t.shape("turtle")
# t.fillcolor("DarkOrange")
#
# t.forward(100)
#
#
# screen = Screen()
# screen.exitonclick()
from prettytable import PrettyTable

table = PrettyTable()

table.add_column("City Name",["Bagani","Bavchi","Ashta","Dhavali"])
table.add_column("Population",[10000,4000,25000,1000])
table.align = "r"
print(table)

