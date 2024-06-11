# Project: Manim-Templates
# Copyright(c) 2024 Skillbanc.com, Inc.
# License: MIT License
# Contributor(s):   
#   Sudhakar Moparthy
# Project: Manim-Templates
# Copyright(c) 2024 Skillbanc.com, Inc.
# License: MIT License
# Contributor(s):   
#   Sudhakar Moparthy
import random
from manim import *
from numpy import size
from AbstractAnim import AbstractAnim
import cvo

class chcomparingquantities(AbstractAnim):
    
    def construct(self):
        # Create and display the introduction CVO
        p1 = cvo.CVO().CreateCVO("comparing quantities using proportions", "ratios and percentages are used to compare quantities.")
        self.setNumberOfCirclePositions(1)
        self.construct1(p1, p1)
        self.isFadeOutAtTheEndOfThisScene = True

        # Transition through each concept section
        # self.play(AnimationGroup(*[FadeOut(obj) for obj in self.mobjects], lag_ratio=0))
        # self.wait(1)
        self.ratio()
        # self.wait(1)
        # self.clear()
        self.compoundratio()
        # self.wait(1)
        # self.clear()
        self.percentage()
        # self.wait(1)
        # self.clear()
        self.discount()
        # self.wait(1)
        # self.clear()
        self.profitorloss()
        # self.wait(1)
        # self.clear()
        self.salestaxorvat()
        # self.wait(1)
        # self.clear()
        self.GST()
        # self.wait(1)
        # self.clear()
        self.simpleinterest()
        # self.wait(1)
        # self.clear()
        self.compoundinterest()
        # self.wait(1)
        # self.clear()

    def ratio(self):
        self.positionChoice = [[-4,-2,0],[4,2,0]]
        self.angleChoice = [TAU/4]
        self.colorChoice=[ORANGE,YELLOW,PURPLE]
        self.isRandom = False
        p2 = cvo.CVO().CreateCVO("ratio", "")
        p3 = cvo.CVO().CreateCVO("example", "x = 24, y = 16")
        p4 = cvo.CVO().CreateCVO("x:y", "24:16 i.e 3:2")
        p2.cvolist.append(p3)
        p3.cvolist.append(p4)
        
        self.setNumberOfCirclePositions(3)
        
        self.construct1(p2, p2)
        self.isFadeOutAtTheEndOfThisScene = True
        
        # self.play(*[FadeOut(mobject) for mobject in self.mobjects])
        # self.wait(1)
        
    def compoundratio(self):
         self.positionChoice = [[-4,-2,0],[4,2,0]]
         self.angleChoice = [TAU/4]
         self.colorChoice=[ORANGE,YELLOW,PURPLE]
         self.isRandom = False
         p4 = cvo.CVO().CreateCVO("compound ratio", "two ratios are expressed as single ratio")
         p5 = cvo.CVO().CreateCVO("a:b , c:d", "a/b * c/d= ac/bd = ac:bd")
         p6 = cvo.CVO().CreateCVO("example", "4:5 and 4:5 , 4/5 * 4/5 = 16/25 =16:25") 
        
         p4.cvolist.append(p5)
         p5.cvolist.append(p6)

         self.setNumberOfCirclePositions(3)
         
         self.construct1(p4, p4)
         self.isFadeOutAtTheEndOfThisScene = True

        # self.play(*[FadeOut(mobject) for mobject in self.mobjects])
        # self.wait(1)

    def percentage(self):
        self.positionChoice = [[-4,-2,0],[4,2,0]]
        self.angleChoice = [TAU/4]
        self.colorChoice=[ORANGE,YELLOW,PURPLE]
        self.isRandom = False
        p7 = cvo.CVO().CreateCVO("percentage", "compares a number to 100")
        p8 = cvo.CVO().CreateCVO("example", "total=40, x=24")
        p9 = cvo.CVO().CreateCVO("percentage of x", "24/40 * 100= 60") 
        
        p7.cvolist.append(p8)
        p8.cvolist.append(p9)
        
        self.setNumberOfCirclePositions(3)
        
        self.construct1(p7, p7)
        self.isFadeOutAtTheEndOfThisScene = True  
        
        # self.play(*[FadeOut(mobject) for mobject in self.mobjects])
        # self.wait(1)
    
    def discount(self):
        self.positionChoice = [[-4,-2,0],[4,2,0]]
        self.angleChoice = [TAU/4]
        self.colorChoice=[ORANGE,YELLOW,PURPLE,LIGHT_PINK,WHITE,LIGHT_GRAY,LIGHT_BROWN,BLUE]
        self.isRandom = False
        p4 = cvo.CVO().CreateCVO("discount", "it is price reduction")
        p5 = cvo.CVO().CreateCVO("formula", "marked price - selling price")
        p6 = cvo.CVO().CreateCVO("discount percentage", "(discount / marked price) * 100")
        p7 = cvo.CVO().CreateCVO("example", "") 
        p8 = cvo.CVO().CreateCVO("MP", "3600")
        p9 = cvo.CVO().CreateCVO("SP", "3312")
        p10 = cvo.CVO().CreateCVO("DISCOUNT", "3600-3312=288")
        p11 = cvo.CVO().CreateCVO("DISCOUNT PERCENTAGE", "(288/3600)*100=8%")
        p4.cvolist.append(p5)
        p4.cvolist.append(p6)
        p4.cvolist.append(p7)
        p7.cvolist.append(p8)
        p7.cvolist.append(p9)
        p8.cvolist.append(p10)
        p9.cvolist.append(p10)
        p8.cvolist.append(p11)
        p9.cvolist.append(p11)

        self.setNumberOfCirclePositions(3)
        
        self.construct1(p4,p4)
        self.isFadeOutAtTheEndOfThisScene = True

        # self.play(*[FadeOut(mobject) for mobject in self.mobjects])
        # self.wait(1)

    def profitorloss(self):
        self.positionChoice = [[-4,-2,0],[4,2,0]]
        self.angleChoice = [TAU/4]
        self.colorChoice=[ORANGE,YELLOW,PURPLE,LIGHT_PINK,WHITE]
        self.isRandom = False
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
        # self.isFadeOutAtTheEndOfThisScene = False
        # self.wait(1)
    
        self.construct1(p8, p7)
        # self.wait(1)
    
        self.construct1(p9, p8)
        # self.wait(1)
    
        # self.play(FadeOut(p8), FadeOut(p9))
        # self.wait(1)
    
        self.construct1(p10, p7)
        # self.wait(1)
    
        self.construct1(p11, p10)
        # self.wait(1)
    
        # self.play(*[FadeOut(mobject) for mobject in self.mobjects])
        # self.wait(1)
        
    def salestaxorvat(self):
        self.positionChoice = [[-4,-2,0],[4,2,0]]
        self.angleChoice = [TAU/4]
        self.colorChoice=[ORANGE,YELLOW,PURPLE]
        self.isRandom = False
        
        p7 = cvo.CVO().CreateCVO("sales tax/VAT(value added tax)", "")
        p8 = cvo.CVO().CreateCVO("sales tax", "imposed when a product is sold to customer")
        p9 = cvo.CVO().CreateCVO("vat", "charged by govt for public welfare expenses")
        # p10 = cvo.CVO().CreateCVO("loss", "decrease percent of cost price")
        # p11 = cvo.CVO().CreateCVO("formula", "cost price - selling price")
        p7.cvolist.append(p8)
        p7.cvolist.append(p9)
        self.setNumberOfCirclePositions(3)
        self.construct1(p7, p7)
        self.isFadeOutAtTheEndOfThisScene = True  
        
        # self.play(*[FadeOut(mobject) for mobject in self.mobjects])
        # self.wait(1)
    
    def GST(self):
        self.positionChoice = [0,0,0]
        self.angleChoice = [TAU/4]
        self.colorChoice=[ORANGE]
        self.isRandom = False
        p7 = cvo.CVO().CreateCVO("gst", "charged on supply of goods and servies")
        self.construct1(p7, p7)
        self.isFadeOutAtTheEndOfThisScene = True  
        
        # self.play(*[FadeOut(mobject) for mobject in self.mobjects])
        # self.wait(1)
         
    def simpleinterest(self):
        self.positionChoice = [[-4,-2,0],[4,2,0]]
        self.angleChoice = [TAU/4]
        self.colorChoice=[ORANGE,YELLOW,PURPLE,LIGHT_PINK,WHITE,LIGHT_GRAY]
        self.isRandom = False
        p4 = cvo.CVO().CreateCVO("simple interest", "increase percent on principal")
        p5 = cvo.CVO().CreateCVO("formula", "(P*T*R)/100")
        p6 = cvo.CVO().CreateCVO("example", "")
        p7 = cvo.CVO().CreateCVO("P-principal amount", "2500")
        p8 = cvo.CVO().CreateCVO("T-time", "3")
        p9 = cvo.CVO().CreateCVO("R-rate of interest", "12%")
        p10 = cvo.CVO().CreateCVO("S.I", "PTR/100=900")
    
        p4.cvolist.append(p5)
        p5.cvolist.append(p6)
        p6.cvolist.append(p7)
        p6.cvolist.append(p8)
        p6.cvolist.append(p9)
        p7.cvolist.append(p10)
        p8.cvolist.append(p10)
        p9.cvolist.append(p10)
    
        self.setNumberOfCirclePositions(7)
    
        self.construct1(p4, p4)
        self.isFadeOutAtTheEndOfThisScene = False
    
        self.construct1(p5, p4)
        # self.wait(1)
      
        self.construct1(p6, p5)
        # self.wait(1)
    
        self.construct1(p7, p6)
        # self.wait(1)
        self.construct1(p8, p6)
        # self.wait(1)
        self.construct1(p9, p6)
        # self.wait(1)
    
        self.construct1(p10, p7)
        self.construct1(p10, p8)
        self.construct1(p10, p9)
        # self.wait(1)
    
        # self.play(*[FadeOut(mobject) for mobject in self.mobjects])
        # self.wait(1)

    def compoundinterest(self):
        self.positionChoice = [[-4,-2,0],[4,2,0]]
        self.angleChoice = [TAU/4]
        self.colorChoice=[ORANGE,YELLOW,PURPLE,LIGHT_PINK,WHITE,LIGHT_GRAY,LIGHT_BROWN,BLUE,RED]
        self.isRandom = False
        p7 = cvo.CVO().CreateCVO("compound interest", "")
        p8 = cvo.CVO().CreateCVO("formula", "Amount - principal")
        p9 = cvo.CVO().CreateCVO("amount", "p(1 + r/100)^n")
        p10 = cvo.CVO().CreateCVO("example", "")
        p11 = cvo.CVO().CreateCVO("Principal", "5000")
        p12 = cvo.CVO().CreateCVO("rate of interest", "8%")
        p13 = cvo.CVO().CreateCVO("time", "2")
        p14 = cvo.CVO().CreateCVO("Amount is", "5000(1 + 8/100)^2=5832")
        p15 = cvo.CVO().CreateCVO("C.I", "5832-5000=832")

        p7.cvolist.append(p8)
        p8.cvolist.append(p9)
        p10.cvolist.extend([p11, p12, p13])
        p11.cvolist.append(p14)
        p12.cvolist.append(p14)
        p13.cvolist.append(p14)
        p14.cvolist.append(p15)

        self.setNumberOfCirclePositions(9)

        self.construct1(p7, p7)
        # self.wait(1)
        self.construct1(p8, p7)
        # self.wait(1)
        self.construct1(p9, p8)
        # self.wait(1)
    
        # self.play(*[FadeOut(mobject) for mobject in self.mobjects])
        # self.wait(1)
    
        self.construct1(p10, p10)
        # self.wait(1)
        self.construct1(p11, p10)
        # self.wait(1)
        self.construct1(p12, p10)
        # self.wait(1)
        self.construct1(p13, p10)
        # self.wait(1)
        self.construct1(p14, p11)
        self.construct1(p14, p12)
        self.construct1(p14, p13)
        # self.wait(1)
        self.construct1(p15, p14)
        # self.wait(1)
    
        # self.play(*[FadeOut(mobject) for mobject in self.mobjects])
        # self.wait(1)

# Main execution
if __name__ == "__main__":
    scene = chcomparingquantities()
    scene.render()
