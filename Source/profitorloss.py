# Project: Manim-Templates
# Copyright(c) 2024 Skillbanc.com, Inc.
# License: MIT License
# Contributor(s):   
#   Sudhakar Moparthy
import random  # Import the random module
from manim import *
from numpy import size
from AbstractAnim import AbstractAnim
import cvo

class profitorloss(AbstractAnim):
    def construct(self):
        self.profitorloss()
        self.fadeOutCurrentScene()
        self.end()
    def profitorloss(self):
        p7 = cvo.CVO().CreateCVO("profit or loss", "")
        p8 = cvo.CVO().CreateCVO("profit", "increase percent of cost price")
        p9 = cvo.CVO().CreateCVO("formula", "selling price - total cost price")
        p10 = cvo.CVO().CreateCVO("loss", "decrease percent of cost price")
        p11 = cvo.CVO().CreateCVO("formula", "cost price - selling price")
        
        p7.cvolist.append(p8)
        p8.cvolist.append(p9)
        p7.cvolist.append(p10)
        p10.cvolist.append(p11)  
        
        self.setNumberOfCirclePositions(5)
        self.construct1(p7, p7)
        self.isFadeOutAtTheEndOfThisScene = True
    def end(self): 
        self.colorChoice=[PURPLE,WHITE,LIGHT_GRAY]
        p2 = cvo.CVO().CreateCVO("SOURCE CODE REFERENCE", "").setPosition([0,2.5,0])
        p4 = cvo.CVO().CreateCVO("Github URL", "https://github.com/Skillbanc/manim-templates")
        p5 = cvo.CVO().CreateCVO("File Name", "comparingquantities.py")
        p2.cvolist.append(p4)
        p2.cvolist.append(p5)
        self.setNumberOfCirclePositions(3)
        p4.setcircleradius(2)
        p5.setcircleradius(2)
        self.construct1(p2,p2)
        # Main execution
if __name__ == "__main__":
    scene = profitorloss()
    scene.render()