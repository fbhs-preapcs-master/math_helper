from tkinter import *
from math_helper import *
class Window(Frame):

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master
        self.init_window()
    
    # Create window
    def init_window(self):
        
        # set title of the master widget
        self.master.title("Math Helper")

        # allow the widget to take the full space of the root window
        self.pack(fill=BOTH, expand=1)

        # creating a menu instance
        menu = Menu(self.master)
        self.master.config(menu=menu)

        # create the file object
        file = Menu(menu)

        # adds a command to the menu option, calling it exit
        # the command it runs on event is client_exit
        file.add_command(label="Exit", command=self.client_exit)

        # added "file" to our menu
        menu.add_cascade(label="File",menu=file)

        # create the formula menu object
        formula = Menu(menu)

        # add formulas to formula menu
        # TODO
        # Change the labels
        formula.add_command(label="Formula1", command=self.show_formula1)
        formula.add_command(label="Formula2", command=self.show_formula2)
        formula.add_command(label="Formula3", command=self.show_formula3)
        formula.add_command(label="Formula4", command=self.show_formula4)
        formula.add_command(label="Formula5", command=self.show_formula5)

        # added "formula" to our menu
        menu.add_cascade(label="Formulas", menu=formula)

        # add instructions 
        self.text = Label(self, text="Select a formula from the drop-down")
        self.text.pack()

        # answer placeholder
        self.answer = Label(self,text="")

    def show_formula1(self):
        # TODO
        # change the text to match your first formula
        # change the number of parameters to match your first formula
        # change par1, par2, etc. to be more meaningful for your formula
        self.text['text'] = "Formula 1"
        self.parameter1 = Entry(self)
        self.parameter1.insert(1,"par1")
        self.parameter1.pack()
        self.parameter2 = Entry(self)
        self.parameter2.insert(1,"par2")
        self.parameter2.pack()
        self.parameter3 = Entry(self)
        self.parameter3.insert(1,"par3")
        self.parameter3.pack()
        self.parameter4 = Entry(self)
        self.parameter4.insert(1,"par4")
        self.parameter4.pack()
        self.calc_button = Button(self, text="Calculate",command=self.calc_formula1)
        self.calc_button.pack()

    def calc_formula1(self):
        # TODO
        # change the number of parameters to match your
        # first formula
        par1 = self.parameter1.get()
        par2 = self.parameter2.get()
        par3 = self.parameter3.get()
        par4 = self.parameter4.get()
        try:
            # change the function call to match yours
            ans = my_func1(float(par1),float(par2),float(par3),float(par4))
            self.answer['text'] = f"Answer: {ans}"
            self.answer.pack()
        except ValueError as e:
            print(e)
            
    def show_formula2(self):
        # TODO
        # look at show_formula1 for an example
        self.reset_formula()
        self.text['text'] = "Formula 2"
    
    def calc_formula2(self):
        # TODO
        # look at calc_formula1 for an example
        pass
        
    def show_formula3(self):
        # TODO
        # look at show_formula1 for an example
        self.reset_formula()
        self.text['text'] = "Formula 3"
    
    def calc_formula3(self):
        # TODO
        # look at calc_formula1 for an example
        pass
        
    def show_formula4(self):
        # TODO
        # look at show_formula1 for an example
        self.reset_formula()
        self.text['text'] = "Formula 4"
    
    def calc_formula4(self):
        # TODO
        # look at calc_formula1 for an example
        pass


    def show_formula5(self):
        # TODO
        # look at show_formula1 for an example
        self.reset_formula()
        self.text['text'] = "Formula 5"
    
    def calc_formula5(self):
        # TODO
        # look at calc_formula1 for an example
        pass
        
    def reset_formula(self):
        try:
            self.answer.forget()
            self.parameter1.forget()
            self.parameter2.forget()
            self.parameter3.forget()
            self.parameter4.forget()
            self.calc_button.forget()
        except AttributeError:
            # ignore if any of the parameters
            # answer or button aren't there
            pass

    def client_exit(self):
        exit()

def main():
    root = Tk()
    root.geometry("400x200")
    app = Window(root)
    root.mainloop()

if __name__ == "__main__":
    main()