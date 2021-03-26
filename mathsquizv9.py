#mathsquizv8.py
#Howard Li

#import the tool kit interface (tkinter) modules
from tkinter import*
import tkinter.ttk as ttk
from random import*
import datetime

#parent class
class Mathquiz:
    def __init__ (self,parent):
        '''Widgets for welcome frame'''

        self.Welcome = Frame(parent)
        self.Welcome.grid(row=0, column=0)

        self.Titlelabel1 = Label(self.Welcome, text = "Welcome to Maths quiz", bg = "black", fg = "white", width = 30, padx = 30, pady = 10, font = ("Time", '14', "bold italic"))
        self.Titlelabel1.grid(columnspan = 2)

        self.IntroLabel = Label(self.Welcome, text = "The app helps primary stidents from 7-12 yrs")
        self.IntroLabel.grid(row = 1, columnspan = 2)

        self.Nextbutton = Button(self.Welcome, text = 'Next', command = lambda: self.show_Questions())
        self.Nextbutton.grid(row = 9, column = 1)
        self.Nextbutton.bind("<Return>", lambda event: self.show_Questions())
        root.bind("<Return>", lambda event: self.show_Questions())

        #Name and Age label
        self.NameLabel = Label(self.Welcome, text = 'Name', anchor = W, fg = "black", width= 10, padx = 30, pady = 10, font = ("Time", '12', "bold italic"))
        self.NameLabel.grid(row = 2, column = 0)
        
        self.AgeLabel = Label(self.Welcome, text = 'Age', anchor = W, fg = "black", width= 10, padx = 30, pady = 10, font = ("Time", "12", "bold italic"))
        self.AgeLabel.grid(row = 3, column = 0)
        
        #name and age entry
        self.name = StringVar()
        self.name.set("")
        self.NameEntry = ttk.Entry(self.Welcome, width = 20)
        self.NameEntry.grid(row = 2, column = 1, columnspan = 2)

        self.age = IntVar()
        self.age.set("")
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
            self.rb = Radiobutton(self.Welcome, variable = self.diff_lvl, value = i, text = self.difficulty[i], anchor = W, padx = 50, width = "5", height = "2")
            self.diff_btns.append(self.rb)
            self.rb.grid(row = i+6, column = 0, sticky = W)

        '''Widgets for Questions frame'''
        self.index = 0
        self.score = 0

        self.Questions = Frame(parent)
        #self.Questions.grid(row = 0, column = 1)

        '''update QuestionLabel configure method to print question number'''
        self.QuestionLabel = Label(self.Questions, text = "Quiz Questions", bg = "black", fg = "white", width = 30, padx = 30, pady = 10, font = ("Time", '14', "bold italic"))
        self.QuestionLabel.grid(columnspan = 3)

        self.Problems = Label(self.Questions, text = "", pady = 10)
        self.Problems.grid(row = 1, column = 0)

        self.AnswerEntry = ttk.Entry(self.Questions, width = 20)
        self.AnswerEntry.grid(row = 1, column = 1)
        
        #Create Scorelabel to display score
        self.ScoreLabel = Label(self.Questions, text = "")
        self.ScoreLabel.grid(row = 1, column = 2)

        self.feedback = Label(self.Questions, text = "")
        self.feedback.grid(row = 2, column = 1)

        self.HomeButton = ttk.Button(self.Questions, text = 'Home', command = self.show_Welcome)
        self.HomeButton.grid(row = 8, column = 0)

        self.check_button = ttk.Button(self.Questions, text = 'Check answer', command = lambda: self.check_answer())
        self.check_button.grid(row = 8, column = 1)

        #self.next_button = ttk.Button(self.Questions, text = "Next question", command = self.next_question)
        #self.next_button.grid(row=8, column=1)

        self.Report_frame = Frame(parent) 
        self.Report_frame.grid_propagate(4)

        Report_page = ["Name", "Age", "Score"]
        self.report_labels = []

        for i in range(len(Report_page)):
            ColumnHeading = Label(self.Report_frame, text = Report_page[i], width = "7", height = "2", font = ("Times", "2", "bold"))
            self.report_labels.append(ColumnHeading)
            ColumnHeading.grid(row = 0 , column = i +1)

        self.user_name = Label(self.Report_frame, textvariable = self.name)
        self.user_name.grid(row = 3, column = 1)

        self.user_age = Label(self.Report_frame, textvariable = self.age)
        self.user_age.grid(row = 3, column = 2)

        self.user_score = Label(self.Report_frame, text = "")
        self.user_score.grid(row = 3, column = 3)           

        self.Home = ttk.Button(self.Report_frame, text = 'Restart', command = self.Restart)
        self.Home.grid(row = 8, column = 1)

        self.Exit = ttk.Button(self.Report_frame, text = 'All records', command=self.show_Welcome)
        self.Exit.grid(row = 8, column = 2)

        self.Data_frame = Frame(parent)

        self.report_treeview = ttk.Treeview(self.Data_frame)

        self.report_treeview.configure(columns=("age", "score", "date"))

        self.report_treeview.heading('#0', text = "Name", anchor = 'w')
        self.report_treeview.column('#0', anchor = 'w')

        self.report_treeview.heading('age', text = "age")
        self.report_treeview.column('age', anchor = "center")

        self.report_treeview.heading('score', text = "score")
        self.report_treeview.column('score', anchor = "center")

        self.report_treeview.heading('date', text = "date")
        self.report_treeview.column('date', anchor = "center")
        

        self.DataHomeButton = ttk.Button(self.Data_frame, text= "home", command=self.Restart)

    """A method that removes Questions Frame"""

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
                self.name.set(self.NameEntry.get())
                self.age.set(self.AgeEntry.get())
                self.Welcome.grid_remove()
                self.Questions.grid()
                self.next_question()
                score_text = "Score = " + str(self.score)
                self.ScoreLabel.configure(text = score_text)

        except ValueError:
            self.WarningLabel.configure(text = "Please enter a number")
            self.AgeEntry.delete(0, END)  
            self.AgeEntry.focus()    

    def next_question(self):

        x = randrange(10)
        y = randrange(10)
    
        self.select = self.diff_lvl.get()

        if self.select == "0":
            easy_text = question_text = str(x) + " + " + str(y) + " = "
            self.answer = x + y 
            self.index += 1
            self.Problems.configure(text = easy_text)

            self.QuestionLabel.configure(text = "Quiz Question" + str(self.index) + "/5")

        elif self.select == "1":
            medium_text = question_text = str(x) + " - " + str(y) + " = "
            self.answer = x - y 
            self.index += 1
            self.Problems.configure(text = medium_text)

            self.QuestionLabel.configure(text = "Quiz Question" + str(self.index) + "/5")        

        else:
            hard_text = question_text = str(x) + " - " + str(y) + " = "
            self.answer = x * y 
            self.index += 1
            self.Problems.configure(text = hard_text)

            self.QuestionLabel.configure(text = "Quiz Question" + str(self.index) + "/5")

        if self.index >= 6:
            self.Questions.grid_remove()
            self.report_treeview.grid(row=0, column=0)
            self.DataHomeButton.grid(row=1, column=0, sticky="w")
            self.display_all_data()



    def check_answer(self):
        try:
            ans = int(self.AnswerEntry.get())

            if ans == self.answer:
                self.feedback.configure(text = "Correct")
                self.score += 1
                score_text = "Score = " + str(self.score)
                self.ScoreLabel.configure(text = score_text)
                self.user_score.configure(text = score_text)
                self.AnswerEntry.delete(0, END)
                self.AnswerEntry.focus()
                self.next_question()

            else:
                self.feedback.configure(text = "Incorrect", fg = "red") 
                self.AnswerEntry.delete(0, END)
                self.AnswerEntry.focus()
                self.next_question()

        except ValueError:
            self.feedback.configure(text = "Enter a number")
            self.AnswerEntry.delete(0, END)
            self.AnswerEntry.focus()    

        if self.score <= 5:
            self.user_score.configure(text = str(self.score))

    def display_all_data(self):
        self.Data_frame.grid()
        """Open and write user deatils to records.txt as data_file"""
        with open('records.txt', "a+") as data_file:
            self.this_is_important_data = (self.name.get() + ' ' + str(self.age.get()) + ' ' + str(self.score) + ' ' + str(datetime.date.today()) + '\n').split(' ')
            print(self.this_is_important_data)
            data_file.write(str(self.this_is_important_data))
            
        
        self.report_treeview.delete(*self.report_treeview.get_children())

        self.report_treeview.insert('', 'end', text=self.this_is_important_data[0], values=(self.this_is_important_data[1], self.this_is_important_data[2], self.this_is_important_data[3]))

        # pause

    def Restart(self):
        self.Report_frame.grid_remove()
        self.Data_frame.grid_remove()
        restart = Mathquiz(root)

#main rootine
if __name__ == "__main__":
    root = Tk()
    frames = Mathquiz(root)
    root.title("Quiz")
    root.mainloop()
    print(frames.this_is_important_data)