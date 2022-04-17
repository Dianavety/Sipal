from graphics import *
from ButtonClassV2 import *
from mygraphicsV2 import *

def main():
   
   Emociones()

def Emociones(): 
    #homepage of Sipal 
    win = GraphWin('Sipal Home Page',500,500)
    win.setCoords( -100, -100, 100, 100 )
    nopal= Image(Point(0,0),"connopal.ppm")
    nopal.draw(win)
    #quit button 
    quitbut=Button(win,80,-80,-25,-20,"cornsilk","Quit")
    quitbut.activate()

    #Book 1 button
    book2=Button (win,0,-14,20,10,"LightBlue","Comida")
    book2.activate()

    #Book 2 button
    book1=Button (win,0,20,25,10,"LightBlue","Emociones")
    book1.activate()

    #level 1 message 
    message1 = Text(Point(-40,20),"Level 1")
    message1.setSize(20)
    message1.setStyle("bold")
    message1.setTextColor("white")
    message1.draw(win)
    
    #level 2 message
    message2 = Text(Point(-40,-12),"Level 2")
    message2.setSize(20)
    message2.setStyle("bold")
    message2.setTextColor("white")
    message2.draw(win)

    while True:
        p  = win.checkMouse( )
        if p and quitbut.clicked(p):
            win.close()
            break

        if p and book1.clicked(p):
            #emociones home page window
            win.close()
            win = GraphWin('Emociones',500,500)
            win.setCoords( -100, -100, 100, 100 )

            emociones = Image(Point(0,0),"emocciones.ppm")
            emociones.draw(win)

            next=Button(win,75,-80,-20,-10,"cornsilk","Next")
            next.activate()

            libro1=Text(Point(0,20),"Level 1")
            libro1.setSize(20)
            libro1.setStyle("bold")
            libro1.setTextColor("white")
            libro1.draw(win)

            libro=Text(Point(0,8),"Libro:")
            libro.setSize(30)
            libro.setStyle("bold")
            libro.setTextColor("white")
            libro.draw(win)

            Emociones =Text(Point(0,-10),"Emociones")
            Emociones.setSize(30)
            Emociones.setStyle("bold")
            Emociones.setTextColor("white")
            Emociones.draw(win)

            while True:
                r = win.checkMouse() 
                    
                if r and next.clicked(r):
                
                    win.close()
                    win = GraphWin('Page 1',500,500)
                    win.setCoords( -100, -100, 100, 100)

                    hungry = Image(Point(0,10),"hambre.ppm")
                    hungry.draw(win)

                    next=Button(win,75,-80,-20,-10,"cornsilk","Next")
                    next.activate()

                    aline = Line(Point(-100,-50),Point(100,-50))
                    aline.setWidth(6)
                    aline.draw(win)

                    
                    
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