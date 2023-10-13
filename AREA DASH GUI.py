#Area Dash 
from tkinter import * #import tkinter library
from tkinter import messagebox #import messagebox from the tkinter library
import random #import random library

class Start_Window: #class for the window of the start screen
    def __init__(self): #initialise the window
        self.root = Tk() #create the window
        self.root.title("Area Dash") #set the prorgam name
        self.root.geometry("650x400") #set the window size
        Label(self.root, text = "AREA DASH").pack() #create the title text
        Label(self.root, text = "").pack() #placeholder
        Label(self.root, text = "Choose the shape and number of questions below").pack() #create the instruction text
        Label(self.root, text = "").pack() #placeholder
        Label(self.root, text = "Shapes:").pack() #label for the dropdown menu
        options = ["Circle", "Rectangle"] #options for the dropdown menu
        self.selection = StringVar() #defining variable
        self.selection.set(options[0]) #setting default value for the dropdown menu
        OptionMenu(self.root, self.selection, *options).pack() #create the dropdown menu
        Label(self.root, text = "").pack() #placeholder
        Label(self.root, text = "Number of questions (Between 1 and 20):").pack() #label for the entry
        self.entry = Entry(self.root) #create the entry
        self.entry.pack() #display the entry
        Label(self.root, text = "").pack() #placeholder
        Button(self.root, text = "Start", command = self.start_clicked).pack() #create the start button
        self.root.mainloop()
    
    def start_clicked(self): #function for when the start button is clicked
        shape = self.selection.get() #get the selection from the dropdown
        num_of_question = 0 #initialise the number of question
        if self.entry.get().isnumeric(): #check if the text entered is a number
            num_of_question = int(self.entry.get()) #get the entry text as a number
            if 1 <= num_of_question and 20 >= num_of_question: #check if the number entered is in range
                Question_Window(shape, num_of_question) #open the question screen window
            else:
                messagebox.showinfo("Error", "The number is out of the accepted range.") #display an error
        else:
            messagebox.showwarning("Error", "The text entered is not a number.") #display an error

class Question_Window: #class for the window of the question screen
    def __init__(self, shape, num_of_question): #initialise the window
        self.shape = shape #get the shape
        self.num_of_question = num_of_question #get the number of questions
        self.widgets = [] #list for widgets
        self.question_num = 0 #number of current question
        self.correct = 0 #number of correct answers
        self.root = Tk() #create the window
        self.root.title("Area Dash") #set the prorgam name
        self.root.geometry("650x400") #set the window size
        Label(self.root, text = "AREA DASH").pack() #create the title text
        Label(self.root, text = "").pack() #placeholder
        self.new_question() #generate a new question
    
    def clear_window(self): #function for clearing the window
        for widget in self.widgets: #go through every widgets in the list
            widget.destroy() #destroy the widget
    
    def make_text(self, label_text): #function for creating text
        label = Label(self.root, text = label_text) #create a label
        self.widgets.append(label) #add the label to the widgets list
        label.pack() #display the label
    
    def new_question(self): #function for generating a new question
        self.clear_window() #clear the window
        self.question_num = self.question_num + 1 #increase question number by 1
        self.make_text("Question " + str(self.question_num)) #create the question number text
        self.make_text("What is the area of the " + self.shape.lower()) #create the instruction text
        formula = {"Circle": "3.14 × (Radius)²", "Rectangle": "(Width) × (Height)"} #dictionary for the formulas
        self.make_text("Formula: " + formula[self.shape]) #create the formula text
        self.make_text("") #placeholder
        canvas = Canvas(self.root, width = 200, height = 150,  background = "#FFFFFF") #create a canvas
        self.widgets.append(canvas) #add the canvas to the widgets list
        canvas.pack() #display the canvas
        self.make_text("") #placeholder
        self.make_text("Please enter your answer:") #create the instruction text
        self.entry = Entry(self.root) #create the entry
        self.widgets.append(self.entry) #add the entry to the widgets list
        self.entry.pack() #display the entry
        submit_button = Button(self.root, text = "Submit", command = self.submit) #create the submit button
        self.widgets.append(submit_button) #add the submit button to the widgets list
        submit_button.pack() #display the submit button
        if self.shape == "Circle": #check if the shape is circle
            self.radius = random.randrange(1, 51) #generate a random number as radius
            canvas.create_oval(100, 75, 100, 75, fill = "", outline = "#000000", width = 5) #draw the center of the circle
            canvas.create_oval(50, 25, 150, 125, fill = "", outline = "#000000", width = 1) #draw the outline of the circle
            canvas.create_line(100, 75, 150, 75, fill = "#000000", width = 1) #draw the radius
            canvas.create_text(125, 75, text = str(self.radius), anchor = "s") #display the radius
            self.answer = self.radius * self.radius * 3.14 #calculate the answer
        if self.shape == "Rectangle": #check if the shape is circle
            self.width = random.randrange(1, 51) #generate a random number as width
            self.height = random.randrange(1, 51) #generate a random number as height
            canvas.create_rectangle(50, 50, 150, 100, fill = "", outline = "#000000", width = 1) #draw the rectangle
            canvas.create_text(100, 48, text = str(self.width), anchor = "s") #display the width
            canvas.create_text(45, 75, text = str(self.height), anchor = "e") #display the height
            self.answer = self.width * self.height #calculate the answer
    
    def submit(self): #function for submitting the response
        if self.entry.get().replace(".", "").replace("-", "").isnumeric(): #check if the text entered is a number
            response = float(self.entry.get()) #get the text entered as a number
            if response == self.answer: #check if the answer is correct
                messagebox.showinfo("Correct", "Your answer is correct.") #display the result
                self.correct = self.correct + 1
            else:
                messagebox.showinfo("Wrong", "Your answer is wrong.") #display the result
            if self.question_num < self.num_of_question: #check if there is next question
                self.new_question() #generate a new question
            else:
                self.clear_window() #clear the window
                result = "You have answered " + str(self.num_of_question) + " questions\nThe questions is about finding the area of " + str(self.shape).lower() + "s\n\nYou have answered " + str(self.correct) + " questions correctly\nThere are " + str(self.num_of_question - self.correct) + " questions that you got it wrong" #text for the results
                txt_file = open("Results.txt", "w") #create a text file
                txt_file.write(result) #save the results into a text file
                txt_file.close() #close the text file
                self.make_text("You have answered {} questions".format(str(self.num_of_question))) #display total number of questions
                self.make_text("The questions is about finding the area of {}s".format(str(self.shape).lower())) #display the shape
                self.make_text("") #placeholder
                self.make_text("You have answered {} questions correctly".format(str(self.correct))) #display the number of correct answers
                self.make_text("There are {} questions that you got it wrong".format(str(self.num_of_question - self.correct))) #display the number of wrong answers
                self.make_text("") #placeholder
                self.make_text("Your results have been saved as Result.txt") #create the instructions text
                self.make_text("Click the button below to go back to the start screen") #create the instructions text
                self.make_text("") #placeholder
                Button(self.root, text = "Back", command = self.root.destroy).pack() #create the back button
        else:
            messagebox.showwarning("Error", "The text entered is not a number.") #display an error
    pass
    
    
    
    pass

Start_Window() #open the start screen window