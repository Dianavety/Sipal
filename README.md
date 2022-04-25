# Sipal
CSC 151 final project (Ashley Luna y Diana Diaz)

Overview

Sipal is able to allow the user to follow through pages, each with a phrase, an image to aid in the understanding of the phrase and an audio button so that the user can understand how to say the phrase. After the user is able to play with the audio and is able to understand how to say the phrase, they can hit the enter button which will then prompt them to say the phrase. The user will have 2 tries in which our program will recognize if the user has said the phrase correctly or not. If the user has said the phrase correctly within one of the tries, the program will recognize it as correct. 

How to use

To run Sipal, one must have VS code installed, Python, Pydub, Simpleaudio, SpeechRecognition and Pyaudio. The rest of the code and files should be included in the zipfile. The user could go through each window or page of the book and check that every button functions. The user could also be able to speak and interact with our program which will then transcribe what is spoken to it and verify if it’s correct or not. The user is given two tries to say the text correctly. The audio button can be played multiple times while the practice button can only be played once. If the user has failed to pronounce correctly after two attempts, they'd move onto the following page. Once the practice button is clicked it gives the user two seconds before the microphone is activated and the user should wait a second before beginning to speak so that the program is able to capture everything. Once the practice button is clicked it cannot be clicked again. The user is unable to return to the previous page once the next button is clicked.  

Installations needed

Pydub and Simpleaudio installed which work together for our audio button. SpeechRecognition and Pyaudio installed which work together for our practice button. The application can be accessed in vscode. Tests can be run using pytest. 
