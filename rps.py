from tkinter import *
import random

class Game(Frame):
    def __init__(self, master=None):
        self.wins = IntVar()
        self.winsNum = 0
        self.losses = IntVar()
        self.lossesNum = 0

        Frame.__init__(self, master)
        self.grid(padx=20, pady=20)
        self.createWidgets()

    def chooseWinner(self):
        self.robot_choice = random.choice(["rock","paper","scissors"])
        print(self.robot_choice)
        if self.user_choice == self.robot_choice:
            self.resultText.set("Tie!")

        elif self.user_choice == "rock":
            if self.robot_choice == "paper":
                self.lossesNum += 1
                self.losses.set(self.lossesNum)
                self.resultText.set("You lose to robot... {} covers {}".format(self.robot_choice, self.user_choice))
            else:
                self.winsNum += 1
                self.wins.set(self.winsNum)
                self.resultText.set("You win! {} smashes {}".format(self.user_choice, self.robot_choice))

        elif self.user_choice == "paper":
            if self.robot_choice == "scissors":
                self.lossesNum += 1
                self.losses.set(self.lossesNum)
                self.resultText.set("You lose to robot... {} cut {}".format(self.robot_choice, self.user_choice))
            else:
                self.winsNum += 1
                self.wins.set(self.winsNum)
                self.resultText.set("You win! {} covers {}".format(self.user_choice, self.robot_choice))

        elif self.user_choice == "scissors":
            if self.robot_choice == "rock":
                self.lossesNum += 1
                self.losses.set(self.lossesNum)
                self.resultText.set("You lose to robot... {} smashes".format(self.robot_choice, self.user_choice))
            else:
                self.winsNum += 1
                self.wins.set(self.winsNum)
                self.resultText.set("You win! {} cut {}".format(self.user_choice, self.robot_choice))

    def chooseAction(self, action):
        self.user_choice = action
        print(action)
        self.chooseWinner()

    def createWidgets(self):
        self.winsLabel = Label(self, text="You")
        self.winsLabel.grid(row=0, column=0, stick=W)
        self.winsCount = Label(self, textvariable=self.wins)
        self.winsCount["fg"] = "#673AB7"
        self.winsCount["font"] = ("Droid Sans", 13)
        self.winsCount.grid(row=1, column=0, sticky=W)

        self.lossesLabel = Label(self, text="Robot")
        self.lossesLabel.grid(row=0, column=3, stick=E)
        self.lossesCount = Label(self, textvariable=self.losses)
        self.lossesCount["fg"] = "#673AB7"
        self.lossesCount["font"] = ("Droid Sans", 13)
        self.lossesCount.grid(row=1, column=3, sticky=E)

        self.rock = Button(self)
        self.rock["command"] =  lambda: self.chooseAction("rock")
        self.rockPhoto=PhotoImage(file="rock.png")
        self.rock.config(image=self.rockPhoto,width="263",height="263", justify='center')

        self.paper = Button(self)
        self.paper["text"] = "Paper"
        self.paper["command"] =  lambda: self.chooseAction("paper")
        self.paperPhoto=PhotoImage(file="paper.png")
        self.paper.config(image=self.paperPhoto,width="263",height="263", justify='center')

        self.scissors = Button(self)
        self.scissors["text"] = "Scissors"
        self.scissors["command"] =  lambda: self.chooseAction("scissors")
        self.scissorsPhoto=PhotoImage(file="scissors.png")
        self.scissors.config(image=self.scissorsPhoto,width="263",height="263", justify='center')

        self.rock.grid(row=2, column=0)
        self.paper.grid(row=2, column=1)
        self.scissors.grid(row=2, column=2)

        self.resultText = StringVar()
        self.result = Label(self, textvariable=self.resultText, justify="center")
        self.result["font"] = ("Droid Sans", 16)
        self.result["fg"] = "green"
        self.result.grid(row=5, sticky=W, columnspan=5)


root = Tk()
root.wm_title("Rock Paper Scissors")
app = Game(master=root)
app.mainloop()
root.destroy()
