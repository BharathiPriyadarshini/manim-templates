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

class Simpleinterest(AbstractAnim):

    def construct(self):
        self.simpleinterest()
    
    def simpleinterest(self):
        self.positionChoice = [[-4, -1, 0], [4, -1, 0], [0, 2, 0], [-4, 1, 0]]
        self.angleChoice = [TAU/5,TAU/4,TAU/3,TAU/2]
        self.colorChoice=[BLUE,GREEN,PURPLE,ORANGE]
        self.isRandom = False
        
        p2 = cvo.CVO().CreateCVO("simple interest", "increase percent on principal")
        p3 = cvo.CVO().CreateCVO("formula", "(P*T*R)/100")
        # p6 = cvo.CVO().CreateCVO("example", "")
        # p7 = cvo.CVO().CreateCVO("P-principal amount", "2500")
        # p8 = cvo.CVO().CreateCVO("T-time", "3")
        # p9 = cvo.CVO().CreateCVO("R-rate of interest", "12%")
        # p10 = cvo.CVO().CreateCVO("S.I", "PTR/100=900")   
        p4=cvo.CVO().CreateCVO("example","")
        p4onamelist=["Principal amount=2500","time=3","rate of interest=12%"]
        p5 = cvo.CVO().CreateCVO("S.I", "PTR/100=900")   
        p2.cvolist.append(p3)
        p2.cvolist.append(p4)
        p4.extendOname(p4onamelist)
        p4.cvolist.append(p5)
        
        self.setNumberOfCirclePositions(4)
        self.setNumberOfAngleChoices(6)
        self.construct1(p2,p2)
        self.isFadeOutAtTheEndOfThisScene = False
       


        
# Main execution
if __name__ == "__main__":
    scene = Simpleinterest()
    scene.render()
