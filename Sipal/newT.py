from graphics import *
from ButtonClassV2 import *
from mygraphicsV2 import *
from pydub import AudioSegment
from pydub.playback import play
from Speechrectest import userguess
import time
import speech_recognition as sr
from Speechrectest import recognize_speech_from_mic

def main():
    state = 0
    speechprompt = False
    win0=Win0()
    quitbut=Quit(win0)
    book1= Book1(win0)
   # book2 = Book2(win0)
    Home(win0)

    while True:
        if state == 0:
            p  = win0.checkMouse( )
        if p and quitbut.clicked(p):
            win0.close()
            break

 #opens the homepage of book 1 
        elif p and book1.clicked(p):
            state = 11
            quitbut.deactivate()
            win0.close()
            win1 = Ewin()
            Emociones(win1)
            next0 = Nemo(win1)
            audibut = AudiE(win1)
      
        if state == 11 :
            p  = win1.checkMouse() 

 #creates first page of book and closes homepage window                 
            if p and next0.clicked(p):
                state = 12
                quitbut.deactivate()
                win1.close()
                win2 = Hwin()
                Hambre(win2)
                next1 = NextH(win2)
                audibut2 = AudiH(win2)
                enterbut1 = PracticeH(win2)
# plays "Level 1" audio recording
            if p and audibut.clicked(p):
                print(state)
                wav_file = AudioSegment.from_file(file = "Sipal/Level1.wav",format = "wav")
                play(wav_file)
            
        if state == 12:
            p  = win2.checkMouse( )
#allows the user to check their speech 
            if p and enterbut1.clicked(p):
                if speechprompt == False:
                    speechprompt = True
                    if userguess("tengo hambre") == True:
                        message = Text(Point(0,-80),"Correct!")
                        message.setTextColor("green")
                        message.setSize(35)
                        message.setStyle("bold")
                        message.draw(win2)
                    else :
                        message = Text(Point(0,-80),"Incorrect!")
                        message.setTextColor("red")
                        message.setSize(35)
                        message.setStyle("bold")
                        message.draw(win2)
# closes page 2 and creates page 3 
            if p and next1.clicked(p):
                speechprompt = False
                state = 13
                quitbut.deactivate()
                win2.close()

                win3 = Twin()
                Triste(win3)
                next2 =NextT(win3)
                audibut3 = AudiT(win3)
                enterbut2 = PracticeT(win3)
# plays "hambre" audio    
            if p and audibut2.clicked(p):
                print(state)
                wav_file = AudioSegment.from_file(file = "Sipal/hambre.wav",format = "wav")
                play(wav_file)
            
        if state == 13:
            p  = win3.checkMouse()
# allows user to check their speech
            if p and enterbut2.clicked(p):
                if speechprompt == False:
                    speechprompt = True
                    if userguess("estoy triste") == True:
                        message2 = Text(Point(0,-80),"Correct!")
                        message2.setTextColor("green")
                        message2.setSize(35)
                        message2.setStyle("bold")
                        message2.draw(win3)
                    else :
                        message2 = Text(Point(0,-80),"Incorrect!")
                        message2.setTextColor("red")
                        message2.setSize(35)
                        message2.setStyle("bold")
                        message2.draw(win3)
# closes page 3 and creates page 4                      
            if p and next2.clicked(p):
                speechprompt = False
                state = 14
                quitbut.deactivate()
                win3.close()
                win4 = Fwin()
                Feliz(win4)
                next3 = NextF(win4)
                audibut4=AudiF(win4)
                enterbut = PracticeF(win4)
#plays "triste" audio
            if p and audibut3.clicked(p):
                wav_file = AudioSegment.from_file(file = "Sipal/triste.wav",format = "wav")
                play(wav_file)

        if state == 14:
            p  = win4.checkMouse()
# allows user to check their speech 
            if p and enterbut.clicked(p):
                if speechprompt == False:
                    speechprompt = True
                    if userguess("estoy feliz") == True:
                        message3 = Text(Point(0,-80),"Correct!")
                        message3.setTextColor("green")
                        message3.setSize(35)
                        message3.setStyle("bold")
                        message3.draw(win4)
                    else :
                        message3 = Text(Point(0,-80),"Incorrect!")
                        message3.setTextColor("red")
                        message3.setSize(35)
                        message3.setStyle("bold")
                        message3.draw(win4)
# closes window the book ends 
            if p and next3.clicked(p):
                speechprompt = False
                win4.close()
                break
# plays "feliz" audio
            if p and audibut4.clicked(p):

                wav_file = AudioSegment.from_file(file = "Sipal/feliz.wav",format = "wav")
                play(wav_file)

def Ewin(): 
    """Creates the Title page of the first book
     and displays downloaded image as background"""            
    win1 = GraphWin('Emociones',500,500)
    print("we created a window")
    win1.setCoords( -100, -100, 100, 100 )
    emociones = Image(Point(0,0),"Sipal/emocciones.ppm")
    emociones.draw(win1)
    return win1 

def Nemo(win1):
    """Creates next button to allow user 
    to move to onto the next page of the book"""
    next0=Button(win1,75,-80,-20,-10,"LightPink","Next")
    next0.activate()
    return next0

def AudiE(win1):
    """Creates audio button to allow user 
    to listen to the text"""
    audibut = Button(win1, -75, -80, -20, -10, "LightBlue","Audio")
    audibut.activate()
    return audibut

def Emociones(win1): 
    """ Creates the graphics displayed on the homepage window"""

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

    
def Hwin():
    """creates hambre window and sets image as background"""
    win2 = GraphWin('Page 1',500,500)
    win2.setCoords( -100, -100, 100, 100)
    hungry = Image(Point(0,18),"Sipal/hambrep.ppm")
    hungry.draw(win2)
    return win2 

def NextH(win2):
    """Creates next button to allow user 
    to move to onto the next page of the book"""
    next1=Button(win2,75,-80,-20,-10,"LightPink","Next")
    next1.activate()
    return next1

def AudiH(win2):
    """creates audio button that plays hambre audio"""
    audibut2 = Button(win2, 75, -35, -20, -10, "LightBLue","Audio")
    audibut2.activate()
    return audibut2

def PracticeH(win2):
    """creates practice button that allows user to use speech recognition"""
    enterbut1 = Button(win2,-75,-80,-20,-10,"LightGreen","Practice")
    enterbut1.activate()
    return enterbut1

def Hambre(win2):
    """creates graphics that display on win2"""
    brect= Rectangle(Point(-100,-50), Point(100,-100))
    brect.setFill("white")
    brect.draw(win2)

    hambre=Text(Point(0,-60),"Tengo hambre")
    hambre.setSize(30)
    hambre.setStyle("bold")
    hambre.setTextColor("black")
    hambre.draw(win2)


    aline = Line(Point(-100,-50),Point(100,-50))
    aline.setWidth(6)
    aline.draw(win2)

def Twin():
    """creates page 2 and uses image file as background"""
    win3 = GraphWin('Page 2',500,500)
    win3.setCoords( -100, -100, 100, 100)
    sad = Image(Point(0,18),"Sipal/tristeg.ppm")
    sad.draw(win3)
    return win3   
def NextT(win3):
    """Creates next button to allow user 
    to move to onto the next page of the book"""
    next2=Button(win3,75,-80,-20,-10,"LightPink","Next")
    next2.activate()
    return next2
def AudiT(win3):
    """Creates audio button that plays triste audio"""
    audibut3 = Button(win3, 75, -35, -20, -10, "LightBLue","Audio")
    audibut3.activate()
    return audibut3
def PracticeT(win3):
    """creates practice button that allows user to use speech recognition"""
    enterbut2 = Button(win3,-75,-80,-20,-10,"LightGreen","Practice")
    enterbut2.activate()
    return enterbut2
def Triste(win3):     
    """Creates graphics that are displayed on win3"""    
    crect= Rectangle(Point(-100,-50), Point(100,-100))
    crect.setFill("white")
    crect.draw(win3)

    triste=Text(Point(0,-60),"Estoy triste")
    triste.setSize(30)
    triste.setStyle("bold")
    triste.setTextColor("black")
    triste.draw(win3)

    bline = Line(Point(-100,-50),Point(100,-50))
    bline.setWidth(6)
    bline.draw(win3)

def Fwin():
    """Creates page 3 and displays the image file as background"""
    win4 = GraphWin('Page 3',500,500)
    win4.setCoords( -100, -100, 100, 100)
    happy = Image(Point(0,30),"Sipal/felize.ppm")
    happy.draw(win4)
    return win4

def NextF(win4):
    """Creates next button to allow user 
    to move to onto the next page of the book"""
    next3=Button(win4,75,-80,-20,-10,"LightPink","Quit")
    next3.activate()
    return next3

def AudiF(win4):
    """Creates audio button that plays feliz audio"""
    audibut4 = Button(win4, 75, -35, -20, -10, "LightBlue","Audio")
    audibut4.activate()
    return audibut4

def PracticeF(win4):
    """creates practice button that allows user to use speech recognition"""
    enterbut = Button(win4,-75,-80,-20,-10,"LightGreen","Practice")
    enterbut.activate()
    return enterbut

def Feliz(win4):
    """Creates graphics that are displays on win4 """
    drect= Rectangle(Point(-100,-50), Point(100,-100))
    drect.setFill("white")
    drect.draw(win4)
    
    feliz=Text(Point(0,-60),"Estoy feliz")
    feliz.setSize(30)
    feliz.setStyle("bold")
    feliz.setTextColor("black")
    feliz.draw(win4)

    cline = Line(Point(-100,-50),Point(100,-50))
    cline.setWidth(6)
    cline.draw(win4)

def Win0():
    """Creates beginning window that displays the image file as background"""
    win0 = GraphWin('Sipal Home Page',500,500)
    win0.setCoords( -100, -100, 100, 100 )
    nopal= Image(Point(0,0),"Sipal/convnopal.ppm")
    nopal.draw(win0)
    return win0

def Quit(win0):
    """Creates a quit button that allows user to exit out of the program"""
    quitbut=Button(win0,80,-80,-25,-20,"cornsilk","Quit")
    quitbut.activate()
    return quitbut

def Book1(win0):
    """Creates a button that gives access to user to the first book"""
    book1=Button (win0,0,20,30,10,"LightBlue","Emociones")
    book1.activate()
    return book1

# def Book2(win0):
#     book2=Button (win0,0,30,25,10,"LightBlue","Emociones")
#     book2.activate()
#     return book2

def Home(win0):
    """Creates graphics to display on win0"""
    #level 1 message 
    message1 = Text(Point(-50,20),"Level 1")
    message1.setSize(20)
    message1.setStyle("bold")
    message1.setTextColor("white")
    message1.draw(win0)
    
    #level 2 message
    # message2 = Text(Point(-50,-12),"Level 2")
    # message2.setSize(20)
    # message2.setStyle("bold")
    # message2.setTextColor("white")
    # message2.draw(win0)
          

main()