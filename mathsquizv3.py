#mathsquizv3.py
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
