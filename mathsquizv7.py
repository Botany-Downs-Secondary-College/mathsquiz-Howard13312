#mathsquizv7.py
#Howard Li

#import the tool kit interface (tkinter) modules
from tkinter import*
from tkinter import ttk
from random import*

#parent class
class Mathquiz:
    def __init__ (self,parent):

        '''Widgets for welcome frame'''

        self.Welcome = Frame(parent)
        self.Welcome.grid(row=0, column=0)

        self.Titlelabel1 = Label(self.Welcome, text = "Welcome to Maths quiz", bg = "black", fg = "white", width = 30, padx = 30, pady = 10, font = ("Time", '14', "bold italic"))
        self.Titlelabel1.grid(columnspan = 2)

        self.Nextbutton = ttk.Button(self.Welcome, text = 'Next', command = self.show_Questions)
        self.Nextbutton.grid(row = 8, column = 1)

        #Name and Age label
        self.NameLabel = Label(self.Welcome, text = 'Name', anchor = W, fg = "black", width= 10, padx = 30, pady = 10, font = ("Time", '12', "bold italic"))
        self.NameLabel.grid(row = 2, column = 0)
        
        self.NameLabel = Label(self.Welcome, text = 'Age', anchor = W, fg = "black", width= 10, padx = 30, pady = 10, font = ("Time", "12", "bold italic"))
        self.NameLabel.grid(row = 3, column = 0)
        
        #name and age entry
        self.NameEntry = ttk.Entry(self.Welcome, width = 20)
        self.NameEntry.grid(row = 2, column = 1, columnspan = 2)
        
        self.AgeEntry = ttk.Entry(self.Welcome, width = 20)
        self.AgeEntry.grid(row = 3, column = 1)
        
        #Warning, Difficulty level label and radio buttons
        self.WarningLabel = Label(self.Welcome, text = '', anchor = W, fg = "red", width= 20, padx = 30, pady = 10)
        self.WarningLabel.grid(row = 4, columnspan = 2)

        self.DifficultyLabel = Label(self.Welcome, text = 'Choose diffculity', anchor = W, fg = "black", width= 14, padx = 30, pady = 20, font = ("Time", "12", "bold italic"))
        self.DifficultyLabel.grid(row = 5, column = 0)
        
        self.difficulty = ["Easy", "Medium", "Hard"]
        self.diff_lvl = StringVar()
        self.diff_lvl.set(0)
        self.diff_btns = []

        for i in range(len(self.difficulty)):
            rb = Radiobutton(self.Welcome, variable = self.diff_lvl, value = i, text = self.difficulty[i], anchor = W, padx = 50, width = "5", height = "2")
            self.diff_btns.append(rb)
            rb.grid(row = i+6, column = 0, sticky = W)

        '''Widgets for Questions frame'''
        
        self.Questions = Frame(parent)
        #self.Questions.grid(row = 0, column = 1)

        self.QuestionLabel = Label(self.Questions, text = "Quiz Questions", bg = "black", fg = "white", width = 20, padx = 30, pady = 10, font = ("Time", '14', "bold italic"))
        self.QuestionLabel.grid(columnspan = 2)

        self.Problems = Label(self.Questions, text = "")
        self.Problems.grid(row = 1, column = 0)

        self.AnswerEntry = ttk.Entry(self.Questions, width = 20)
        self.AnswerEntry.grid(row = 1, column = 1)

        self.feedback = Label(self.Questions, text = "")
        self.feedback.grid(row = 2, column = 0)

        self.HomeButton = ttk.Button(self.Questions, text = 'Home', command = self.show_Welcome)
        self.HomeButton.grid(row = 8, column = 0)

        self.check_button = ttk.Button(self.Questions, text = 'Check answer', command = self.check_answer)
        self.check_button.grid(row = 8, column = 0)

        self.next_button = ttk.Button(self.Questions, text = "Next question", command = self.next_question)
        self.next_button.grid(row=8, column=1)        
    
    def show_Welcome(self):
        self.Questions.grid_remove()
        self.Welcome.grid()

    def show_Questions(self):
#Error checking for empty or non-text user entries for Name
        try:
            if self.NameEntry.get() == "":
              self.WarningLabel.configure(text = "Please enter name")
              self.NameEntry.focus()

            elif self.NameEntry.get().isalpha() == False:
                self.WarningLabel.configure(text = "Please enter text")
                self.NameEntry.delete(0, END)
                self.NameEntry.focus()   
#Error for checking for empty and age limit cases
            elif self.AgeEntry.get() == "":
                self.WarningLabel.configure(text = "Please enter age")
                self.AgeEntry.focus()

            elif int(self.AgeEntry.get()) > 12:
                 self.WarningLabel.configure(text = "You are too old!")
                 self.AgeEntry.delete(0, END)  
                 self.AgeEntry.focus()
             
            elif int(self.AgeEntry.get()) < 0:
                 self.WarningLabel.configure(text = "You can't be smaller than 0?")
                 self.AgeEntry.delete(0, END)  
                 self.AgeEntry.focus()
             
            elif int(self.AgeEntry.get()) < 7:
                 self.WarningLabel.configure(text = "You are too young!")
                 self.AgeEntry.delete(0, END)  
                 self.AgeEntry.focus()       

            else:
                self.Welcome.grid_remove()
                self.Questions.grid()

        except ValueError:
            self.WarningLabel.configure(text = "Please enter a number")
            self.AgeEntry.delete(0, END)  
            self.AgeEntry.focus()    

    def next_question(self):
        x = randrange(10)
        y = randrange(10)
        self.answer = x + y 

        question_text = str(x) + " + " + str(y) + " = "
        self.Problems.configure(text = question_text)

    def check_answer(self):
        try:
            ans = int(self.AnswerEntry.get())

            if ans == self.answer:
                self.feedback.configure(text = "Correct")
                self.AnswerEntry.delete(0, END)
                self.AnswerEntry.focus()
                self.next_question()

            else:
                self.feedback.configure(text = "Incorrect") 
                self.AnswerEntry.delete(0, END)
                self.AnswerEntry.focus()
                self.next_question()

        except ValueError:
            self.feedback.configure(text = "Enter a number")
            self.AnswerEntry.delete(0, END)
            self.AnswerEntry.focus()       
#main rootine
if __name__ == "__main__":
    root = Tk()
    frames = Mathquiz(root)
    root.title("Quiz")
    root.mainloop()