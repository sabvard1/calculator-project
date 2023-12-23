from tkinter import *

class calculator:
    def __init__(self):
        self.win = Tk()
        self.win.geometry("310x470")
        self.win.title("CALCULATOR")
        self.input_text = StringVar()
        self.text = ""
        self.li = {7: (3, 0, 1, 8, 7), 8: (3, 1, 1, 8, 8), 9:(3, 2, 1, 8, 9), "×": (3, 3, 1, 8, "*"),
                   4: (4, 0, 1, 8, 4), 5: (4, 1, 1, 8, 5), 6: (4, 2, 1, 8, 6), "-":(4, 3, 1, 8, "-"),
                   1: (5, 0, 1, 8, 1), 2: (5, 1, 1, 8, 2), 3: (5, 2, 1, 8, 3), "+": (5, 3, 1, 8, "+"),
                   0: (6, 0, 2, 19, 0), ".": (6, 2, 1, 8, "."), "÷": (2, 3, 1, 8, "/")}

        self.lii = { "C": (1, 0, 3, 30, lambda : self.clear_button()), "Del":(1, 3, 1, 8, lambda : self.del_button()), "%": (2, 0, 1, 8, lambda : self.percent_button()), "X²": (2, 1, 1, 8, lambda : self.power_button()), "√X": (2, 2, 1, 8, lambda : self.root_button()), "=": (6, 3, 1, 8, lambda : self.equal_button())}
        self.display = self.create_display()
        
        self.keys1 = ["%" , "CE", "C", "DEL"]
        self.keys2 = ["1/x", "X²", "√X", "÷"]
        self.create_buttons()

        self.create_func_buttons()

        
        
    def create_display(self):
        h = Entry(self.win,textvariable = self.input_text, font = ("Times New Roman", 20), bd = 3).grid(row = 0, column = 0, columnspan = 4, padx = 10, pady = 10, ipady = 10)
        return h
    
    def get_num(self, num):
        textt = str(self.text)
        self.text = textt + str(num)
        self.renew_display()



    def create_buttons(self):
        for nn, vv in self.li.items():
            button = Button(self.win, text = str(nn), width = vv[3], height = 3, command = lambda  x = vv[4] : self.get_num(x)).grid(row = vv[0], column = vv[1],columnspan = vv[2], padx = 2, pady = 2)


    def create_func_buttons(self):
        for nn, vv in self.lii.items():
            button = Button(self.win, text = str(nn), width = vv[3], height = 3, command = vv[4]).grid(row = vv[0], column = vv[1],columnspan = vv[2], padx = 2, pady = 2)
    def clear_button(self):
        self.text = ""
        self.input_text.set(self.text)


    def del_button(self):
        len_text = len(self.text)
        self.text = self.text[0:int(len_text)-1]
        self.input_text.set(self.text)

    def power_button(self):
        if self.text != "" :
            self.text = int(self.text)**2
            self.input_text.set(self.text)
        else :
            pass

    def root_button(self):
        if self.text != "" :
            textt = self.text
            result = int(textt)**(1/2)
            self.text = result
            self.input_text.set(self.text)
        else :
            pass

    def percent_button(self):
        textt = self.text
        find_x = textt.find("*")
        secound_part = (int(textt[find_x+1:]))/100
        if "*" in textt :
            result = secound_part * int(textt[0:find_x])
            self.input_text.set(str(result))
        else :
            pass
        

    def equal_button(self):
        if "+" in self.text or "-" in self.text or "*" in self.text or "/" in self.text :
            textt = self.text
            result = str(eval(textt))
            self.text = result
            self.input_text.set(self.text)
            self.text = ""
        else :
            pass

    def renew_display(self):
        self.input_text.set(self.text)



    
    def run(self):
        self.win.mainloop()
        
    



if __name__ == "__main__" :
    calc = calculator()
    calc.run()

    

