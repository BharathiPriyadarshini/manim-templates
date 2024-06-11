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

class explanationofconcepts(AbstractAnim):

    def construct(self):
        self.intro()
        self.fadeOutCurrentScene()
        self.ratio()
        self.fadeOutCurrentScene()
        self.compoundratio()
        self.fadeOutCurrentScene()
        self.percentage()
    
    def intro(self):
         
        # Create CVO objects for the introduction
         p1 = cvo.CVO().CreateCVO("comparing quantities using proportions", "ratios and percentages are used to compare quantities.")
          
        
         self.setNumberOfCirclePositions(2)
         self.construct1(p1, p1 )
        
    def ratio(self):
        self.positionChoice = [[-4,-2,0],[4,2,0]]
        self.angleChoice = [TAU/4,TAU/5]
        self.colorChoice=[ORANGE,YELLOW]
        self.isRandom = False
        p2 = cvo.CVO().CreateCVO("ratio", "")
        p3 = cvo.CVO().CreateCVO("expressed as ", "x:y")
        # p4 = cvo.CVO().CreateCVO("x:y", "24:16 i.e 3:2")
        p2.cvolist.append(p3)
        # p3.cvolist.append(p4)
        
        self.setNumberOfCirclePositions(2)
        self.construct1(p2, p2)
        self.isFadeOutAtTheEndOfThisScene = True
        self.fadeOutCurrentScene()
        
    def compoundratio(self):
        self.positionChoice = [[-4,-2,0],[4,2,0],[6,2,0]]
        self.angleChoice = [TAU/4,TAU/5,TAU/6]
        self.colorChoice=[ORANGE,YELLOW,PURPLE]
        self.isRandom = False
        p4 = cvo.CVO().CreateCVO("compound ratio", "two ratios are expressed as single ratio")
        p5 = cvo.CVO().CreateCVO("a:b , c:d", "a/b * c/d= ac/bd = ac:bd")
        p6 = cvo.CVO().CreateCVO("example", "4:5 and 4:5 , 4/5 * 4/5 = 16/25 =16:25") 
        p4.cvolist.append(p5)
        p5.cvolist.append(p6)
        p5.setcircleradius(2)
        
        self.setNumberOfCirclePositions(3)
            
            # Construct the animation for the CVO objects
        self.construct1(p4, p4)
        self.isFadeOutAtTheEndOfThisScene = True
        
    
    def percentage(self):
        self.positionChoice = [[-4, -1, 0], [4, -1, 0], [0, 2, 0], [-4, 1, 0]]

        
        self.angleChoice = [TAU/5,TAU/4,TAU/3,TAU/2]
        self.colorChoice=[BLUE,GREEN,PURPLE,ORANGE]
        self.isRandom = False
        p7 = cvo.CVO().CreateCVO("percentage", "compares a number to 100")
        p8 = cvo.CVO().CreateCVO("formula", "value/total * 100")
        p9 = cvo.CVO().CreateCVO("example", "total=40, x=24")
        p10 = cvo.CVO().CreateCVO("percentage of x", "24/40 * 100= 60") 
        
        p7.cvolist.append(p8)
        p7.cvolist.append(p9)
        p9.cvolist.append(p10)
        
        self.setNumberOfCirclePositions(4)
        
        self.construct1(p7, p7)
        self.isFadeOutAtTheEndOfThisScene = True
# Main execution

if __name__ == "__main__":
    scene = explanationofconcepts()
    scene.render()
