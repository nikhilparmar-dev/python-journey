# WAP to show the use Modules in python.
# Date: 11/03/2026
# Author: Nikhil    


# Modules 

import mymodule 
mymodule.say_hello("Nikhil")
mymodule.say_bye("Nikhil")

from mymodule import person
print(person["Age"])


import calc
# x = int(input("Enter first number: "))
# y = int(input("Enter second number: "))

# print("Addition: ", calc.add(x, y))
# print("Subtraction: ", calc.sub(x, y))
# print("Multiplication: ", calc.mult(x, y))
# print("Division: ", calc.div(x, y))


# Python Built-in Module Examples

import math
print(math.sqrt(25))
print(math.pi)  
print(math.factorial(4))



# Python External Libraries (PiP's)

import numpy
print("Module installed successfully")


# 1 :

import numpy as np

a = np.array([10, 20, 30, 40, 50])

print("Array= ", a)
print("Avarage= ", np.mean(a))
print("Sum= ", np.sum(a))




# 2 :
import pandas as pd

data = {
    "Name" : ["Nikhil", "Prem", "Tushar", "Zeeshan"],
    "Marks" : [90, 99, 91, 95]
}

df = pd.DataFrame(data)

# print(df)




# 3 :
import matplotlib.pyplot as plt

x=[1,2,3,4]
y=[10,20,25,30]

plt.plot(x, y)
plt.title("Graph showen")
# plt.show()




# 4 :

from colorama import Fore

print(Fore.RED + "This is Red Text")
print(Fore.GREEN + "This is Green Text")




# 5. 
import pyttsx3
engine = pyttsx3.init()
engine.say("Tata")
engine.runAndWait()


# 6 :
import gtts
import os

text = "good morning bhai"

tts = gtts.gTTS(text=text, lang='en')

# save temporary
# tts.save("temp.mp3")
nnj
# # play audio
# os.system("start temp.mp3")




# 7.
import turtle

colors = ["red","orange","yellow","green","blue","indigo","violet"]
t = turtle.Turtle()
t.speed(0)

# for i in range(200):
#     t.color(colors[i % 7])
#     t.circle(100)
#     t.left(10)

# # turtle.done()





# 8. 
import pygame
import random

pygame.init()

# screen = pygame.display.set_mode((600,400))
# clock = pygame.time.Clock()

# particles = []

# while True:
#     screen.fill((0,0,0))

#     if random.randint(1,10) == 1:
#         particles.append([300,200,random.randint(-5,5),random.randint(-5,5)])

#     for p in particles:
#         pygame.draw.circle(screen,(255,255,0),(p[0],p[1]),3)
#         p[0] += p[2]
#         p[1] += p[3]

#     pygame.display.update()
#     clock.tick(30)





# 9.
from PIL import Image, ImageDraw
import random

img = Image.new("RGB",(500,500),"white")
draw = ImageDraw.Draw(img)

# for i in range(100):
#     x1 = random.randint(0,500)
#     y1 = random.randint(0,500)
#     x2 = random.randint(0,500)
#     y2 = random.randint(0,500)

#     color = (random.randint(0,255),
#              random.randint(0,255),
#              random.randint(0,255))

#     draw.line((x1,y1,x2,y2),fill=color,width=3)

# img.show()





# 10.
import turtle

t = turtle.Turtle()
t.speed(0)

colors = ["red","blue","green","yellow","purple","cyan"]

# for i in range(300):
#     t.pencolor(colors[i % 6])
#     t.forward(i)
#     t.left(59)

# turtle.done()





# 11.
import pygame

pygame.init()

screen = pygame.display.set_mode((600,400))
ball_x = 300
ball_y = 200

speed_x = 4
speed_y = 4

# while True:
#     screen.fill((0,0,0))

#     ball_x += speed_x
#     ball_y += speed_y

#     if ball_x > 580 or ball_x < 20:
#         speed_x *= -1

#     if ball_y > 380 or ball_y < 20:
#         speed_y *= -1

#     pygame.draw.circle(screen,(255,0,0),(ball_x,ball_y),20)

#     pygame.display.update()





# 12.
import pygame
import random

pygame.init()

# screen size
width = 800
height = 500
screen = pygame.display.set_mode((width, height))

font = pygame.font.SysFont("consolas", 20)

letters = "01ABCDEFGHIJKLMNOPQRSTUVWXYZ"

drops = [random.randint(0, height) for i in range(width // 20)]

# while True:

#     screen.fill((0,0,0))

    # for i in range(len(drops)):

    #     char = random.choice(letters)
    #     text = font.render(char, True, (0,255,0))

    #     x = i * 20
    #     y = drops[i]

    #     screen.blit(text,(x,y))

    #     drops[i] += 20

    #     if drops[i] > height:
    #         drops[i] = 0

    # pygame.display.update()





# 13.
import pygame
import sys

pygame.init()

width = 600
height = 400

# screen = pygame.display.set_mode((width, height))
# clock = pygame.time.Clock()

# ripples = []

# while True:

#     screen.fill((0, 0, 30))

#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             pygame.quit()
#             sys.exit()

#         if event.type == pygame.MOUSEBUTTONDOWN:
#             ripples.append([event.pos[0], event.pos[1], 10])

#     for ripple in ripples:
#         pygame.draw.circle(screen, (0,150,255), (ripple[0], ripple[1]), ripple[2], 2)
#         ripple[2] += 2

#     pygame.display.update()
#     clock.tick(60)





# 14.
import turtle

t = turtle.Turtle()
t.speed(0)
t.width(3)

screen = turtle.Screen()
screen.bgcolor("white")

# face
t.penup()
t.goto(0,-100)
t.pendown()
t.color("blue")
t.begin_fill()
t.circle(120)
t.end_fill()

# face inner
t.penup()
t.goto(0,-80)
t.pendown()
t.color("white")
t.begin_fill()
t.circle(100)
t.end_fill()

# left eye
t.penup()
t.goto(-40,40)
t.pendown()
t.begin_fill()
t.circle(25)
t.end_fill()

# right eye
t.penup()
t.goto(40,40)
t.pendown()
t.begin_fill()
t.circle(25)
t.end_fill()

# nose
t.penup()
t.goto(0,20)
t.pendown()
t.color("red")
t.begin_fill()
t.circle(12)
t.end_fill()

# mouth
t.penup()
t.goto(-50,0)
t.pendown()
t.color("black")
t.circle(50,180)

turtle.done()