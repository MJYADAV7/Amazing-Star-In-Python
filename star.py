from turtle import *
sc=Screen()
sc.setup(600,600)
sc.bgcolor("black")
speed(10)
c=["blue","yellow","white","green"]
j=0

for i in range(50):
    forward(i*10)
    right(144)
    color(c[j])
    if j==3:
        j=0
    else:
        j+=1
