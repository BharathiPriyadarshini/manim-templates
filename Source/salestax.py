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

class salestax(AbstractAnim):
    def construct(self):
      self.salestax()
      self.fadeOutCurrentScene()
      self.vat()
      self.fadeOutCurrentScene()
      self.gst()

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
      self.construct1(p2,p2)
      self.isFadeOutAtTheEndOfThisScene = False
    
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
       self.setNumberOfAngleChoices(5)
       self.construct1(p2,p2)
       self.isFadeOutAtTheEndOfThisScene = False
    
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
        self.setNumberOfAngleChoices(5)
        self.construct1(p2,p2)
        self.isFadeOutAtTheEndOfThisScene = False

# Main execution
if __name__ == "__main__":
    scene = salestax()
    scene.render()
