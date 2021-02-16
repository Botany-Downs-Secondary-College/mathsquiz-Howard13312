#mathsquizv4.py
#Howard Li

#import the tool kit interface (tkinter) modules
from tkinter import*
from tkinter import ttk

#parent class
class Mathquiz:
    def __init__ (self,parent):

        '''Widgets for welcome frame'''

        self.Welcome = Frame(parent)
        self.Welcome.grid(row=0, column=0)

        self.Titlelabel1 = Label(self.Welcome, text = "Welcome to Maths quiz", bg = "black", fg = "white", width = 20, padx = 30, pady = 10, font = ("Time", '14', "bold italic"))
        self.Titlelabel1.grid(columnspan = 2)

        self.Nextbutton = ttk.Button(self.Welcome, text = 'Next', command = self.show_Questions)
        self.Nextbutton.grid(row = 8, column = 1)

        #Name and Age label
        self.NameLabel = Label(self.Welcome, text = 'Name', anchor = W, fg = "black", width= 10, padx = 30, pady = 10, font = ("Time", "12", "bold italic"))
        self.NameLabel.grid(row = 2, column = 0)
        
        self.NameLabel = Label(self.Welcome, text = 'Age', anchor = W, fg = "black", width= 10, padx = 30, pady = 10, font = ("Time", "12", "bold italic"))
        self.NameLabel.grid(row = 3, column = 0)
        
        #name and age entry
        self.NameEntry = ttk.Entry(self.Welcome, width = 20)
        self.NameEntry.grid(row = 2, column = 1, columnspan = 2)
        
        self.AgeEntry = ttk.Entry(self.Welcome, width = 20)
        self.AgeEntry.grid(row = 3, column = 1)
        
        #Difficulty level label and radio buttons
        self.DifficultyLabel = Label(self.Welcome, text = 'Choose difficulty', anchor = W, fg = "black", width= 10, padx = 30, pady = 10, font = ("Time", "12", "bold italic"))
        self.DifficultyLabel.grid(row = 4, column = 0)
        
        self.difficulty = ["Easy", "Medium", "Hard"]
        self.diff_lvl = StringVar()
        self.diff_lvl.set(0)
        self.diff_btns = []

        for i in range(len(self.difficulty)):
            rb = Radiobutton(self.Welcome, variable = self.diff_lvl, value = i, text = self.difficulty[i], anchor = W, padx = 50, width = "5", height = "2")
            self.diff_btns.append(rb)
            rb.grid(row = i+5, column = 0, sticky = W)

        '''Widgets for question frame'''
        
        self.Questions = Frame(parent)
        #self.Questions.grid(row = 0, column = 1)

        self.QuestionLabel = Label(self.Questions, text = "Quiz Questions", bg = "black", fg = "white", width = 20, padx = 30, pady = 10, font = ("Time", '14', "bold italic"))
        self.QuestionLabel.grid(columnspan = 2)

        self.HomeButton = ttk.Button(self.Questions, text = 'Home', command = self.show_Welcome)
        self.HomeButton.grid(row = 8, column = 1)        
    
    def show_Welcome(self):
        self.Questions.grid_remove()
        self.Welcome.grid()

    def show_Questions(self):
        self.Welcome.grid_remove()
        self.Questions.grid()    




#main rootine
if __name__ == "__main__":
    root = Tk()
    frames = Mathquiz(root)
    root.title("Quiz")
    root.mainloop() 
