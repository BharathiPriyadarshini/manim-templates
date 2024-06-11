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

class comparingquantities(AbstractAnim):

    def construct(self):
        # self.RenderSkillbancLogo()
        # self.intro()
        # self.fadeOutCurrentScene()
        # self.ratio()
        # self.fadeOutCurrentScene()
        # self.compoundratio()
        # self.fadeOutCurrentScene()
        # self.percentage()
        # self.fadeOutCurrentScene()
        # self.increaseordecrease()
        # self.fadeOutCurrentScene()
        # self.exampleid()
        # self.fadeOutCurrentScene()
        # self.discount()
        # self.fadeOutCurrentScene()
        # self.estimationinpercentage()
        # self.fadeOutCurrentScene()
        # self.profitorloss() 
        # self.fadeOutCurrentScene()
        # self.salestax()
        # self.fadeOutCurrentScene()
        # self.vat()
        # self.fadeOutCurrentScene()
        # self.gst()
        # self.fadeOutCurrentScene()
        # self.compoundinterest()
        # self.fadeOutCurrentScene()
        # self.exampleci()
        # self.fadeOutCurrentScene()
        self.GithubSourceCodeReference()

        
    def intro(self):
         
        # Create CVO objects for the introduction
         p1 = cvo.CVO().CreateCVO("comparing quantities using proportions", "ratios and percentages .").setPosition([0,0,0])
          
        
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
        # self.isFadeOutAtTheEndOfThisScene = True
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
        p6.setcircleradius(2)
        self.setNumberOfCirclePositions(3)
            
            # Construct the animation for the CVO objects
        self.construct1(p4, p4)
        # self.isFadeOutAtTheEndOfThisScene = True
        
    
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
        p7.setcircleradius(2)
        p8.setcircleradius(1.5)
        p9.setcircleradius(1.5)
        p10.setcircleradius(1.5)
        self.setNumberOfCirclePositions(4)
        
        self.construct1(p7, p7)
        # self.isFadeOutAtTheEndOfThisScene = True
        
    def increaseordecrease(self):
        self.colorChoice=[BLUE,WHITE,YELLOW,GREEN,ORANGE,RED ]
        p1=cvo.CVO().CreateCVO("finding increase or decrease percent","").setPosition([0,2.5,0])
        p2=cvo.CVO().CreateCVO("unitary method","").setPosition([4,2,0])
        p3=cvo.CVO().CreateCVO("normal method ","").setPosition([5,-2,0])
        # p4=cvo.CVO().CreateCVO("example","").setPosition([-4,2,0]).setangle(-TAU/4)
        # p4onamelist=["Price=34000","price increased=20\%"]
        # p5=cvo.CVO().CreateCVO("answer using unitary","").setPosition([-4,0,0])
        # p5onamelist=["$20\% of 100=120$","$rs.1=120/100$","$rs.3400=(120/100)*3400=40,800$"]
        # p6=cvo.CVO().CreateCVO("answer using normal","").setPosition([-5,-2,0])
        # p6onamelist=["$20\% of 34000=6800$","$increased price=34000+6800=40,800$"]
        p1.cvolist.append(p2)
        p1.cvolist.append(p3)
        # p1.cvolist.append(p4)
        # p4.extendOname(p4onamelist)
        # p4.cvolist.append(p5)
        # p5.extendOname(p5onamelist)
        # p4.cvolist.append(p6)
        # p6.extendOname(p6onamelist)
        self.setNumberOfCirclePositions(3)
        self.construct1(p1, p1)
        
    def exampleid(self):
        p3=cvo.CVO().CreateCVO("example","").setPosition([0,2.5,0])
        p4=cvo.CVO().CreateCVO("","").setPosition([4,2,0])
        p4onamelist=["Price=34000","price increased=20\%"]
        p5=cvo.CVO().CreateCVO("answer using unitary","")
        p5onamelist=["$20\% of 100=120$","$rs.1=120/100$","$rs.3400=(120/100)*3400=40,800$"]
        p6=cvo.CVO().CreateCVO("answer using normal","")
        p6onamelist=["$20\% of 34000=6800$","$increased price=34000+6800=40,800$"]
        p3.cvolist.append(p4)
        p4.extendOname(p4onamelist)
        p4.cvolist.append(p5)
        p5.extendOname(p5onamelist)
        p4.cvolist.append(p6)
        p6.extendOname(p6onamelist)
        self.setNumberOfCirclePositions(4)
        p4.setcircleradius(1.5)
        p5.setcircleradius(2)
        p6.setcircleradius(2)
        self.construct1(p3, p3)
        
    def estimationinpercentage(self): 
        p1=cvo.CVO().CreateCVO("estimation in percentage","").setPosition([0,2.5,0]) 
        p2=cvo.CVO().CreateCVO("example","estimate 15\% of 477.80").setPosition([4,2,0])
        p3=cvo.CVO().CreateCVO("step 1","round of amount to nearest tens i.e 447.80=480s").setPosition([4.5,-2.5,0])
        p4=cvo.CVO().CreateCVO("step 2","$15\%=10\% + 5\%$").setPosition([1,-2.5,0])
        p5=cvo.CVO().CreateCVO("step 3","10\% of 480=48 ,5\%of 480=24").setPosition([-1,-1,0])
        p6=cvo.CVO().CreateCVO("","48+24=72").setPosition([-4,0,0])
        p7=cvo.CVO().CreateCVO("amount to be paid approximately","480-72=408").setPosition([-4,2,0])
        p1.cvolist.append(p2)
        p2.cvolist.append(p3)
        p2.cvolist.append(p4)
        
        p2.cvolist.append(p5)
        p5.cvolist.append(p6)
        p6.cvolist.append(p7)
        self.setNumberOfCirclePositions(7)
        p2.setcircleradius(2)
        p4.setcircleradius(1.5)
        p5.setcircleradius(1.5)
        self.construct1(p1, p1)
        # self.isFadeOutAtTheEndOfThisScene = False
        
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
        p2.setcircleradius(1.5)
        p3.setcircleradius(2)
        p4.setcircleradius(2)
        self.setNumberOfAngleChoices(6)
        self.construct1(p2, p2)
        # self.isFadeOutAtTheEndOfThisScene = False   
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
        p8.setcircleradius(2)
        p10.setcircleradius(2)
        p9.setcircleradius(2)
        p11.setcircleradius(2)
        self.construct1(p7, p7)
        # self.isFadeOutAtTheEndOfThisScene = True
    def compoundinterest(self):
        # self.positionChoice = [[-6,-2,0],[-6,2,0],[0,3,0],[6,-2,0],[6,2,0],[0,-3,0]]
        # self.angleChoice = [TAU/5,TAU/4,TAU/3,TAU/2,-TAU/5,-TAU/4]
        self.colorChoice=[RED,BLUE,GREEN,PURPLE,ORANGE,YELLOW,WHITE]
        self.isRandom = False
        p3 = cvo.CVO().CreateCVO("compound interest", "").setPosition([0,2.5,0])
        p4 = cvo.CVO().CreateCVO("FORMULA", "Amount - principal").setPosition([4,2,0])
        p5 = cvo.CVO().CreateCVO("amount(annually)", "$p(1 + r/100)^t$").setPosition([5,-2,0])
        p9 = cvo.CVO().CreateCVO("amount(half yearly)", "$p(1 + (r/2)/100)^{2t}$")
        
        
        
        # p6 = cvo.CVO().CreateCVO("example", "").setPosition([-4,2,0]).setangle(-TAU/4)
        # p6onamelist=["PRINCIPAL=5000","TIME=3","RATE OF INTEREST=12%"]
        # # p7 = cvo.CVO().CreateCVO("Principal", "5000")
        # # p8 = cvo.CVO().CreateCVO("rate of interest", "8%")
        # # p9 = cvo.CVO().CreateCVO("time", "2")
        # p7 = cvo.CVO().CreateCVO("Amount is", "$5000(1 + 8/100)^2=5832$").setPosition([-4,0,0]).setangle(-TAU/4)
        # p8 = cvo.CVO().CreateCVO("C.I", "$5832-5000=832$")
        
        
        p3.cvolist.append(p4)
        p4.cvolist.append(p5)
        p4.cvolist.append(p9)
        # p3.cvolist.append(p6)
        # p6.extendOname(p6onamelist)
        # p6.cvolist.append(p7)
        # p6.cvolist.append(p8)
        self.setNumberOfCirclePositions(4)
        p4.setcircleradius(2)
        p9.setcircleradius(2)
        # self.setNumberOfAngleChoices(9)
        self.construct1(p3,p3)
        # self.isFadeOutAtTheEndOfThisScene = False
    def exampleci(self):
        p5 = cvo.CVO().CreateCVO("example", "")
        p6 = cvo.CVO().CreateCVO("", "")
        p6onamelist=["PRINCIPAL=5000","TIME=3","RATE OF INTEREST=12%"]
        p7 = cvo.CVO().CreateCVO("Amount is", "$5000(1 + 8/100)^2=5832$")
        p8 = cvo.CVO().CreateCVO("C.I", "$5832-5000=832$")
        p5.cvolist.append(p6)
        p6.extendOname(p6onamelist)
        p6.cvolist.append(p7)
        p6.cvolist.append(p8)
        self.setNumberOfCirclePositions(4)
        p6.setcircleradius(2)
        p8.setcircleradius(1.5)
        p7.setcircleradius(2)
        
        
        
        self.construct1(p5,p5)
        
        
        
    def salestax(self):
      p2 = cvo.CVO().CreateCVO("sales tax", "levied on sale of goods")
      p3 = cvo.CVO().CreateCVO("", "tax\% of bill amount")
      p4 = cvo.CVO().CreateCVO("total bill", "item cost+sales tax")
      p5 = cvo.CVO().CreateCVO("example", "x=450,S.T=5\%")
      p6 = cvo.CVO().CreateCVO("tax charged", "$5/100 * 450=22.50$")
      p7 = cvo.CVO().CreateCVO("bill", "472.50")
      
      p2.cvolist.append(p3)
      p3.cvolist.append(p4)
      p2.cvolist.append(p5)
      p5.cvolist.append(p6)
      p6.cvolist.append(p7)
      
      self.setNumberOfCirclePositions(6)
      p3.setcircleradius(1.5)
      p5.setcircleradius(1.5)
      p6.setcircleradius(1.5)
      self.construct1(p2,p2)
    #   self.isFadeOutAtTheEndOfThisScene = False
    
    def vat(self):  
       p2 = cvo.CVO().CreateCVO("value added tax ", "charged on selling price of item")
       p3 = cvo.CVO().CreateCVO("example", "")
       p3onamelist=["bill amount=372.18","vat=5\%"]
       p4 = cvo.CVO().CreateCVO("", "$5\% of 372.18=17.72$")
       p5 = cvo.CVO().CreateCVO("actual bill amount", "$372.18-17.72=354.45$") 
       
       p2.cvolist.append(p3)
       p3.extendOname(p3onamelist)
       p3.cvolist.append(p4)
       p4.cvolist.append(p5)
       self.setNumberOfCirclePositions(4)
       p2.setcircleradius(2)
       p3.setcircleradius(2)
       p4.setcircleradius(1.5)
       p5.setcircleradius(1.5)
       self.setNumberOfAngleChoices(5)
       self.construct1(p2,p2)
    #    self.isFadeOutAtTheEndOfThisScene = False
    
    def gst(self): 
        p2 = cvo.CVO().CreateCVO("good and service tax", "single indirect tax on goods and services")
        p3 = cvo.CVO().CreateCVO("example", "")
        p3onamelist=["bill amount=2200","gst=18\%"]
        p4 = cvo.CVO().CreateCVO("gst paid","$18\% of 2200=396$")
        p5 = cvo.CVO().CreateCVO("bill amount without gst", "$2200-396=1804$")
        
        p2.cvolist.append(p3)
        p3.extendOname(p3onamelist)
        p3.cvolist.append(p4)
        p4.cvolist.append(p5)
        self.setNumberOfCirclePositions(4)
        p3.setcircleradius(1.5)  
        p4.setcircleradius(1.5)
        p5.setcircleradius(1.5)
        self.setNumberOfAngleChoices(5)
        self.construct1(p2,p2)
        # self.isFadeOutAtTheEndOfThisScene = False
    
        
if __name__ == "__main__":
    scene = comparingquantities()
    scene.render()








    
  