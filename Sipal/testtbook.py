from graphics import *
from ButtonClassV2 import *
from mygraphicsV2 import *
from pydub import AudioSegment
from pydub.playback import play

def main():
   
   Emociones()

def Emociones(): 
    #homepage of Sipal 
    state = 0

    win = GraphWin('Sipal Home Page',500,500)
    win.setCoords( -100, -100, 100, 100 )
    nopal= Image(Point(0,0),"Sipal/convnopal.ppm")
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
        if state ==0:

            p  = win.checkMouse( )
            if p and quitbut.clicked(p):
                win.close()
                break


            elif p and book1.clicked(p):
                state = 11
                #emociones book home page window
                win.close()
                quitbut.deactivate()
                win1 = GraphWin('Emociones',500,500)
                win1.setCoords( -100, -100, 100, 100 )

                emociones = Image(Point(0,0),"Sipal/emocciones.ppm")
                emociones.draw(win1)

                next0=Button(win1,75,-80,-20,-10,"cornsilk","Next")
                next0.activate()
                # next=Button(win,75,40,20,10,"cornsilk","Next")
                # next.activate()

                audibut = Button(win1, -75, -80, -20, -10, "cornsilk","Audio")
                audibut.activate()


                libro1=Text(Point(0,20),"Level 1")
                libro1.setSize(20)
                libro1.setStyle("bold")
                libro1.setTextColor("white")
                libro1.draw(win1)

                libro=Text(Point(0,8),"Libro:")
                libro.setSize(30)
                libro.setStyle("bold")
                libro.setTextColor("white")
                libro.draw(win1)

                Emociones =Text(Point(0,-10),"Emociones")
                Emociones.setSize(30)
                Emociones.setStyle("bold")
                Emociones.setTextColor("white")
                Emociones.draw(win1)

            if p and audibut.clicked(p):

                wav_file = AudioSegment.from_file(file = "Sipal/Level1.wav",format = "wav")
                play(wav_file)
    
        if state == 11 :
            p  = win1.checkMouse( )        
            if p and next0.clicked(p):
                state = 12
            #first page of the book emociones
                quitbut.deactivate()
                print('second page')
                win1.close()
                win = GraphWin('Page 1',500,500)
                win.setCoords( -100, -100, 100, 100)


                hungry = Image(Point(0,18),"Sipal/hambrep.ppm")

                hungry.draw(win)

                brect= Rectangle(Point(-100,-50), Point(100,-100))
                brect.setFill("white")
                brect.draw(win)

                hambre=Text(Point(0,-60),"Tengo hambre")
                hambre.setSize(30)
                hambre.setStyle("bold")
                hambre.setTextColor("black")
                hambre.draw(win)

                userin = Entry(Point(0,-80),10)
                txt = userin.getText()
                userin.draw(win)

                enterbut = Button(win,-75,-80,-20,-10,"cornsilk","Enter")
                enterbut.activate()

                next1=Button(win,75,-80,-20,-10,"cornsilk","Next")
                next1.activate()

                audibut = Button(win, 75, -35, -20, -10, "cornsilk","Audio")
                audibut.activate()

                aline = Line(Point(-100,-50),Point(100,-50))
                aline.setWidth(6)
                aline.draw(win)
                        
            if p and audibut.clicked(p):
                wav_file = AudioSegment.from_file(file = "Sipal/hambre.wav",format = "wav")
                play(wav_file)

        
        if state == 12:
            if p and next1.clicked(p):
                state = 13
                quitbut.deactivate()
                win.close()
                win = GraphWin('Page 2',500,500)
                win.setCoords( -100, -100, 100, 100)

                sad = Image(Point(0,18),"Sipal/tristeg.ppm")

                sad.draw(win)

                crect= Rectangle(Point(-100,-50), Point(100,-100))
                crect.setFill("white")
                crect.draw(win)

                triste=Text(Point(0,-60),"Estoy triste")
                triste.setSize(30)
                triste.setStyle("bold")
                triste.setTextColor("black")
                triste.draw(win)

                useri = Entry(Point(0,-80),10)
                txt1 = useri.getText()
                useri.draw(win)

                enterbut = Button(win,-75,-80,-20,-10,"cornsilk","Enter")
                enterbut.activate()

                next2=Button(win,75,-80,-20,-10,"cornsilk","Next")
                next2.activate()


                audibut = Button(win, 75, -35, -20, -10, "cornsilk","Audio")
                audibut.activate()

                bline = Line(Point(-100,-50),Point(100,-50))
                bline.setWidth(6)
                bline.draw(win)

            if p and audibut.clicked(p):
                wav_file = AudioSegment.from_file(file = "Sipal/triste.wav",format = "wav")
                play(wav_file)

        if state == 13:
            if p and next2.clicked(p):
                state = 14
                quitbut.deactivate()
                win.close()
                win = GraphWin('Page 3',500,500)
                win.setCoords( -100, -100, 100, 100)


                happy = Image(Point(0,30),"Sipal/felize.ppm")


                happy.draw(win)

                drect= Rectangle(Point(-100,-50), Point(100,-100))
                drect.setFill("white")
                drect.draw(win)
                
                feliz=Text(Point(0,-60),"Estoy feliz")
                feliz.setSize(30)
                feliz.setStyle("bold")
                feliz.setTextColor("black")
                feliz.draw(win)

                user = Entry(Point(0,-80),10)
                txt2 = user.getText()
                user.draw(win)

                enterbut = Button(win,-75,-80,-20,-10,"cornsilk","Enter")
                enterbut.activate()

                next3=Button(win,75,-80,-20,-10,"cornsilk","Next")
                next3.activate()


                audibut = Button(win, 75, -35, -20, -10, "cornsilk","Audio")
                audibut.activate()

                cline = Line(Point(-100,-50),Point(100,-50))
                cline.setWidth(6)
                cline.draw(win)


            if p and audibut.clicked(p):
                wav_file = AudioSegment.from_file(file = "Sipal/feliz.wav",format = "wav")
                play(wav_file)

                                
        
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