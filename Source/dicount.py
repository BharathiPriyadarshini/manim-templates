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

class conceptsofcomparingquantities(AbstractAnim):
    def construct(self):
        
        
        self.increaseordecrease()
        self.fadeOutCurrentScene()
        self.discount()
        self.fadeOutCurrentScene()
        self.estimationinpercentage()
    
    def increaseordecrease(self):
        self.colorChoice=[BLUE,WHITE,YELLOW,GREEN,ORANGE,RED ]
        p1=cvo.CVO().CreateCVO("increase or decrease percent","").setPosition([0,2.5,0])
        p2=cvo.CVO().CreateCVO("unitary method","").setPosition([4,2,0])
        p3=cvo.CVO().CreateCVO("normal method ","").setPosition([5,-2,0])
        p4=cvo.CVO().CreateCVO("example","").setPosition([-4,2,0]).setangle(-TAU/4)
        p4onamelist=["Price=34000","price increased=20\%"]
        p5=cvo.CVO().CreateCVO("answer using unitary","").setPosition([-4,0,0])
        p5onamelist=["$20\% of 100=120$","$rs.1=120/100$","$rs.3400=(120/100)*3400=40,800$"]
        p6=cvo.CVO().CreateCVO("answer using normal","").setPosition([-5,-2,0])
        p6onamelist=["$20\% of 34000=6800$","$increased price=34000+6800=40,800$"]
        p1.cvolist.append(p2)
        p1.cvolist.append(p3)
        
        p4.extendOname(p4onamelist)
        p4.cvolist.append(p5)
        p5.extendOname(p5onamelist)
        p4.cvolist.append(p6)
        p6.extendOname(p6onamelist)
        self.setNumberOfCirclePositions(6)
        self.construct1(p1, p1)
        self.construct1(p4,p4)
        
    def estimationinpercentage(self): 
        p1=cvo.CVO().CreateCVO("estimation in percentage","").setPosition([0,2.5,0]) 
        p2=cvo.CVO().CreateCVO("example","estimate 15\% of 477.80").setPosition([4,2,0])
        p3=cvo.CVO().CreateCVO("step 1","round of amount to nearest tens i.e 447.80=480s").setPosition([5,-2,0])
        p4=cvo.CVO().CreateCVO("step 2","$15\%=10\% + 5\%$").setPosition([2,-2.5,0])
        p5=cvo.CVO().CreateCVO("step 3","10\% of 480=48 ,5\%of 480=24").setPosition([0,-1,0])
        p6=cvo.CVO().CreateCVO("","48+24=72").setPosition([-4,0,0])
        p7=cvo.CVO().CreateCVO("amount to be paid approximately","480-72=408").setPosition([-4,2,0])
        p1.cvolist.append(p2)
        p2.cvolist.append(p3)
        p2.cvolist.append(p4)
        
        p2.cvolist.append(p5)
        p5.cvolist.append(p6)
        p6.cvolist.append(p7)
        self.setNumberOfCirclePositions(7)
        
        self.construct1(p1, p1)
        self.isFadeOutAtTheEndOfThisScene = False
        
    def discount(self):
        self.positionChoice = [[-4, -1, 0], [4, -1, 0], [0, 2, 0], [-4, 1, 0]]

        
        # self.angleChoice = [TAU/5,TAU/4,TAU/3,TAU/2]
        self.colorChoice=[BLUE,GREEN,PURPLE,ORANGE]
        self.isRandom = False
        
        p2 = cvo.CVO().CreateCVO("discount","it is price reduction")
        p3 = cvo.CVO().CreateCVO("formula","marked price-selling price")
        p4 = cvo.CVO().CreateCVO("discount percentage","(dicount/marked price) * 100")
        
        p11=cvo.CVO().CreateCVO("example","")
        p11onamelist=["MP=3600","SP=3312","discount is 3600-3312=288","discount percentage is (288/3600)*100 =8"]

    
        # p5 = cvo.CVO().CreateCVO("example", "MP=3600,SP=3312")
        # p6 = cvo.CVO().CreateCVO("discount","3600-3312=288") 
        # p7 = cvo.CVO().CreateCVO("discount percentage","(288/3600)*100 =8") 
        p2.cvolist.append(p3)
        p2.cvolist.append(p4)
        
        
        p2.cvolist.append(p11)
        p11.extendOname(p11onamelist)
        
        self.setNumberOfCirclePositions(4)
        self.setNumberOfAngleChoices(6)
        self.construct1(p2, p2)
        self.isFadeOutAtTheEndOfThisScene = False
        
     
        
        # Main execution
if __name__ == "__main__":
    scene = conceptsofcomparingquantities()
    scene.render()
        
        