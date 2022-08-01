from tkinter import *
from tkinter.messagebox import showinfo, showwarning
import webbrowser

root = Tk()
root.title("Psycho Countdown Timer")
root.geometry("600x250")
root.resizable(0,0)


# Font Name and Size to be used to show on timer
fontName = StringVar()
fontName.set("Book Antiqua")
fontSize = IntVar()
fontSize.set(50)

btnFontSize = IntVar()
btnFontSize.set(15)
softwareVersion = "1.0"

# Github Profile Link
githubLink = "https://github.com/HussnainAhmad1606/"

# At started timer will be stop
isTimeStarted = False

# Available fonts on GUI
fonts = ["Book Antiqua", "Stencil", "Rockwell", "Poppins", "New Athletic M54", "Molot", "Georgia", "Century Gothic"]

loopFunction = None


# Function to add 0 to the left of hours, minutes & seconds
def addZero(value):
    if int(value) < 10:
        return f"0{int(value)}"
    else:
        return value


def changeFont():
    font = Tk()
    font.title("Change Font")
    font.geometry("300x300")
    fontLabel = Label(font, text="Change Font", font=(fontName.get(), 12))
    fontLabel.pack(padx=10, pady=10)
    fontBox = Listbox(font, selectmode=SINGLE)
    for index,value in enumerate(fonts):
        fontBox.insert(index+1, value)
    fontBox.pack()

    def setFont():
        global fontName
        fontName.set(fontBox.get(ACTIVE))
        hoursLabel.configure(font=(fontName.get(), fontSize.get()))
        colon1.configure(font=(fontName.get(), fontSize.get()))
        colon2.configure(font=(fontName.get(), fontSize.get()))
        minutesLabel.configure(font=(fontName.get(), fontSize.get()))
        secondsLabel.configure(font=(fontName.get(), fontSize.get()))
        setTimerBtn.configure(font=(fontName.get(), btnFontSize.get()))
        startTimerBtn.configure(font=(fontName.get(), btnFontSize.get()))
        stopTimerBtn.configure(font=(fontName.get(), btnFontSize.get()))
        resetTimerBtn.configure(font=(fontName.get(), btnFontSize.get()))
        showinfo("Font Changed", f"Font Changed to {fontName.get()}")

        font.destroy()


    setFontBtn = Button(font, text="Set Font", command=setFont)
    setFontBtn.pack(padx=10, pady=10)

    font.mainloop()

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
        startTimerBtn["state"] = DISABLED
        stopTimerBtn["state"] = NORMAL
        if isTimeStarted:
            changeTheTime()
            global loopFunction
            loopFunction = root.after(1000, startTimer)


# Stop the timer
def stopTimer():
    global isTimeStarted
    global loopFunction
    isTimeStarted = False
    root.after_cancel(loopFunction)
    startTimerBtn["state"] = NORMAL
    stopTimerBtn["state"] = DISABLED

# Reset the timer
def resetTimer():
    startTimerBtn["state"] = NORMAL
    stopTimerBtn["state"] = DISABLED
    if loopFunction is not None:
        root.after_cancel(loopFunction)
    hours.set("00")
    minutes.set("00")
    seconds.set("00")


# Info About the software
def aboutSoftware():
    about = f"Software: Psycho Timer\nVersion: {softwareVersion}\nProgrammer: Psycho Coder\n Font Name: {fontName.get()}"
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
hoursLabel = Label(watchFrame, textvariable=hours, font=(fontName.get(),fontSize.get()))
hoursLabel.pack(side=LEFT)
colon1 = Label(watchFrame, text=":", font=(fontName.get(), fontSize.get()))
colon1.pack(side=LEFT)
minutesLabel = Label(watchFrame, textvariable=minutes, font=(fontName.get(), fontSize.get()))
minutesLabel.pack(side=LEFT)
colon2 = Label(watchFrame, text=":", font=(fontName.get(), fontSize.get()))
colon2.pack(side=LEFT)
secondsLabel = Label(watchFrame, textvariable=seconds, font=(fontName.get(), fontSize.get()))
secondsLabel.pack(side=LEFT)

watchFrame.pack(side=TOP)

buttonsFrame = Frame(root)

setTimerBtn = Button(buttonsFrame, text="Set Timer", command=setTimer, font=(fontName.get(), btnFontSize.get()))
setTimerBtn.pack(side=LEFT, padx=20, pady=20)

startTimerBtn = Button(buttonsFrame, text="Start", command=startTimer, font=(fontName.get(), btnFontSize.get()))
startTimerBtn.pack(side=LEFT, padx=20, pady=20)

stopTimerBtn = Button(buttonsFrame, text="Stop", command=stopTimer, font=(fontName.get(), btnFontSize.get()))
stopTimerBtn.pack(side=LEFT, padx=20, pady=20)

resetTimerBtn = Button(buttonsFrame, text="Reset", command=resetTimer, font=(fontName.get(), btnFontSize.get()))
resetTimerBtn.pack(side=LEFT, padx=20, pady=20)

buttonsFrame.pack()

# Main Menu
mainMenu = Menu(root)

preferencesMenu = Menu(root, tearoff=0)
preferencesMenu.add_command(label="Fonts", command=changeFont)

mainMenu.add_cascade(label="Preferences", menu=preferencesMenu)
aboutMenu = Menu(mainMenu, tearoff=0)
aboutMenu.add_command(label="Quit", command=root.destroy)
aboutMenu.add_separator()
aboutMenu.add_command(label="About Software", command=aboutSoftware)
aboutMenu.add_separator()
aboutMenu.add_command(label="Visit Website", command=visitWebsite)
mainMenu.add_cascade(label="About", menu=aboutMenu)

root.config(menu=mainMenu)
root.mainloop()