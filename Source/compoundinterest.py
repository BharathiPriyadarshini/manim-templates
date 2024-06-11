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

class  compoundinterest(AbstractAnim):
    def construct(self):
        self.compoundinterest()
        
    def compoundinterest(self):
        # self.positionChoice = [[-6,-2,0],[-6,2,0],[0,3,0],[6,-2,0],[6,2,0],[0,-3,0]]
        # self.angleChoice = [TAU/5,TAU/4,TAU/3,TAU/2,-TAU/5,-TAU/4]
        self.colorChoice=[RED,BLUE,GREEN,PURPLE,ORANGE,YELLOW,WHITE]
        self.isRandom = False
        p3 = cvo.CVO().CreateCVO("compound interest", "").setPosition([0,2.5,0])
        p4 = cvo.CVO().CreateCVO("FORMULA", "Amount - principal").setPosition([4,2,0])
        p5 = cvo.CVO().CreateCVO("amount(anually)", "$p(1 + r/100)^t$").setPosition([5,-2,0])
        p9 = cvo.CVO().CreateCVO("amount(half yearly)", "$p(1 + (r/2)/100)^{2t}$")
        
        
        
        p6 = cvo.CVO().CreateCVO("example", "").setPosition([-4,2,0]).setangle(-TAU/4)
        p6onamelist=["PRINCIPAL=5000","TIME=3","RATE OF INTEREST=12%"]
        # p7 = cvo.CVO().CreateCVO("Principal", "5000")
        # p8 = cvo.CVO().CreateCVO("rate of interest", "8%")
        # p9 = cvo.CVO().CreateCVO("time", "2")
        p7 = cvo.CVO().CreateCVO("Amount is", "$5000(1 + 8/100)^2=5832$").setPosition([-4,0,0]).setangle(-TAU/4)
        p8 = cvo.CVO().CreateCVO("C.I", "$5832-5000=832$")
        
        
        p3.cvolist.append(p4)
        p4.cvolist.append(p5)
        p4.cvolist.append(p9)
        p3.cvolist.append(p6)
        p6.extendOname(p6onamelist)
        p6.cvolist.append(p7)
        p6.cvolist.append(p8)
        self.setNumberOfCirclePositions(7)
        self.setNumberOfAngleChoices(9)
        self.construct1(p3,p3)
        self.isFadeOutAtTheEndOfThisScene = False


# Main execution
if __name__ == "__main__":
    scene = compoundinterest()
    scene.render()
