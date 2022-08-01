from tkinter import *
from tkinter.messagebox import showinfo, showwarning
import webbrowser

root = Tk()
root.title("Psycho Countdown Timer")
root.geometry("600x250")
root.resizable(0,0)


# Font Name and Size to be used to show on timer
fontName = "Book Antiqua"
fontSize = 70
softwareVersion = "1.0"

# Github Profile Link
githubLink = "https://github.com/HussnainAhmad1606/"

# At started timer will be stop
isTimeStarted = False

# Function to add 0 to the left of hours, minutes & seconds
def addZero(value):
    if int(value) < 10:
        return f"0{int(value)}"
    else:
        return value

# Function that will change the count down timer
def changeTheTime():
    global hours, minutes, seconds
    if int(seconds.get()) > 0:
        seconds.set(addZero(int(seconds.get()) - 1))
        print("First")
    elif (int(seconds.get()) == 0):
        seconds.set("59")
        print("Elif")
        if int(minutes.get()) == 0:
            minutes.set("59")
            print("Third")
            if int(hours.get() != 0):
                print("Fourth")
                hours.set(addZero(int(hours.get()) - 1))
        else:
            minutes.set(addZero(int(minutes.get()) - 1))


# Function that will run when user click on start button
def startTimer():
    global isTimeStarted
    isTimeStarted = True
    if (int(hours.get()) == 0 and int(minutes.get()) == 0 and int(seconds.get()) == 0):
        showwarning("Time Up", "Time is up. Set the time again for next counting")
    else:
        if isTimeStarted:
            changeTheTime()
            root.after(1000, startTimer)


# Stop the timer
def stopTimer():
    global isTimeStarted
    isTimeStarted = False

# Reset the timer
def resetTimer():
    hours.set(0)
    minutes.set(0)
    seconds.set(0)


# Info About the software
def aboutSoftware():
    about = f"Software: Psycho Timer\nVersion: {softwareVersion}\nProgrammer: Psycho Coder"
    showinfo("About", about)

# Visiting the github profile when user clicks on visit website on about menu
def visitWebsite():
    webbrowser.open(githubLink)

# Window to set the timer for stopwatch
def setTimer():
    setTimer = Tk()
    setTimer.title("Set the timer")
    setTimer.geometry("500x200")
    setTimer.focus()

    def setTime():
        hours.set(hoursEntry.get())
        minutes.set(minutesEntry.get())
        seconds.set(secondsEntry.get())
        showinfo("Done!", f"Time Set {hoursEntry.get()}:{minutesEntry.get()}:{secondsEntry.get()} Successfully")
        setTimer.destroy()

    hoursLabel = Label(setTimer, text="Hours=")
    hoursLabel.pack()
    hoursEntry = Entry(setTimer)
    hoursEntry.pack()

    minutesLabel = Label(setTimer, text="Minutes=")
    minutesLabel.pack()
    minutesEntry = Entry(setTimer)
    minutesEntry.pack()

    secondsLabel = Label(setTimer, text="Seconds=")
    secondsLabel.pack()
    secondsEntry = Entry(setTimer, text="0")
    secondsEntry.pack()

 
    setBtn = Button(setTimer, text="Set Timer", command=setTime)
    setBtn.pack()
    setTimer.mainloop()


# Variables for storing the hours, minutes and seconds entered by the user.
hours = StringVar()
hours.set("01")
minutes = StringVar()
minutes.set("00")
seconds = StringVar()
seconds.set("05")

# Main Window
watchFrame = Frame(root)
hoursLabel = Label(watchFrame, textvariable=hours, font=(fontName, fontSize))
hoursLabel.pack(side=LEFT)
colon1 = Label(watchFrame, text=":", font=(fontName, fontSize))
colon1.pack(side=LEFT)
minutesLabel = Label(watchFrame, textvariable=minutes, font=(fontName, fontSize))
minutesLabel.pack(side=LEFT)
colon1 = Label(watchFrame, text=":", font=(fontName, fontSize))
colon1.pack(side=LEFT)
secondsLabel = Label(watchFrame, textvariable=seconds, font=(fontName, fontSize))
secondsLabel.pack(side=LEFT)
watchFrame.pack(side=TOP)

buttonsFrame = Frame(root)

setTimerBtn = Button(buttonsFrame, text="Set Timer", command=setTimer)
setTimerBtn.pack(side=LEFT, padx=50, pady=50)

setTimerBtn = Button(buttonsFrame, text="Start", command=startTimer)
setTimerBtn.pack(side=LEFT, padx=50, pady=50)

setTimerBtn = Button(buttonsFrame, text="Stop", command=stopTimer)
setTimerBtn.pack(side=LEFT, padx=50, pady=50)

setTimerBtn = Button(buttonsFrame, text="Reset", command=resetTimer)
setTimerBtn.pack(side=LEFT, padx=50, pady=50)

buttonsFrame.pack()

# Main Menu
mainMenu = Menu(root)

aboutMenu = Menu(mainMenu, tearoff=0)
aboutMenu.add_command(label="Quit", command=root.destroy)
aboutMenu.add_separator()
aboutMenu.add_command(label="About Software", command=aboutSoftware)
aboutMenu.add_separator()
aboutMenu.add_command(label="Visit Website", command=visitWebsite)
mainMenu.add_cascade(label="About", menu=aboutMenu)
root.config(menu=mainMenu)
root.mainloop()