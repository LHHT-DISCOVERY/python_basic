import speech_recognition 
import pyttsx3
from datetime import date,datetime
robot_ear = speech_recognition.Recognizer()
robot_mouth = pyttsx3.init()
robot_brain = " "
while True:
    with speech_recognition.Microphone() as mic :
        
        print("Robot : is listening")
        audio = robot_ear.listen(mic)
        print("Robot...")
    try:
        you = robot_ear.recognize_google(audio)
    except:
        you = ""
    print("You : " + you )

    if you == "":
        robot_brain = " again"
    if you == "hello":
        robot_brain = "Hello Tri"
    elif "today" in you :
        today = date.today()
        robot_brain = today.strftime("%B %d, %Y")
    elif "time" in you:
        now = datetime.now()
        robot_brain=now.strftime("%H hours %M minutes %S second")
    elif "no" in you:
        robot_brain = "yes, you no girl friend"
    elif "robot" in you:
        robot_brain="fuck you"
    elif "game" in you:
        robot_brain = " i love you BUBG mobile "

    elif "again" in you:
        robot_brain = "okay bye bye you"
        
        robot_mouth.say(robot_brain)
        robot_mouth.runAndWait()
        break
    else :
        robot_brain = " Again "
    print("Robot : " + robot_brain)

    robot_mouth.say(robot_brain)
    robot_mouth.runAndWait()
    # code with Lý Huỳnh Hữu Trí
