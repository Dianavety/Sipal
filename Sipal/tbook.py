from graphics import *
from ButtonClassV2 import *
from mygraphicsV2 import *

def main():
   
   Emociones()

def Emociones(): 

    win = GraphWin('Home Page',500,500)
    win.setCoords( -100, -100, 100, 100 )
    nopal= Image(Point(50,50),"connopal.ppm")
    nopal.draw(win)
    #quit button 
    quitbut=Button(win,80,-80,-25,-20,"cornsilk","Quit")
    quitbut.activate()

    #Book 1 button
    book2=Button (win,0,-14,20,10,"LightBlue","Comida")
    book2.activate()

    #Book 2 button
    book1=Button (win,0,20,20,10,"LightBlue","Emociones")
    book1.activate()
    while True:
        p  = win.checkMouse( )
        if p and quitbut.clicked(p):
            win.close()
            break

        if p and book1.clicked(p):
            win.close()
            win = GraphWin('Emociones',500,500)
            win.setBackground( 'LightPink' )
            win.setCoords( -100, -100, 100, 100 )

            next=Button(win,80,-80,-25,-20,"cornsilk","Next")
            next.activate()

            while True:
                r = win.checkMouse() 
                    
                if r and next.clicked(r):
                    win.close()
                    win = GraphWin('Page 1',500,500)
                    win.setBackground( 'LightGreen' )
                    win.setCoords( -100, -100, 100, 100 )
                    
                    while True:
                        a  = win.checkMouse( )
                        if a and next.clicked(a):
                            win.close()
            
        # if p and book2.clicked(p):
        #     win.close()
        #     win2= GraphWin("Book 2",500,500)
        #     win2.setBackground("LightBlue")
        #     win2.setCoords(-100,-100,100,100)
            
        #     qui=Button(win2,80,-80,-25,-20,"cornsilk","Quit")
        #     qui.activate()
        #     while True:
        #         q= win2.checkMouse()
        #         if q and qui.clicked(q):
        #             win2.close()
        #             break
          

main()