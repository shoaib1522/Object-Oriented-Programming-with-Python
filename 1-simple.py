import tkinter as tk

class App(tk.Frame):
    def __init__(self, wnd):
        super().__init__(wnd)
        self.pack()
        self.grid(row= 0, column=0, padx=20, pady=20)
        # remove the above line and later self from below line
        self.entrybox = tk.Entry(self)
        self.entrybox.pack()

        # Create the application variable.
        self.contents = tk.StringVar()
        # Set it to some value.
        self.contents.set("this is a variable")
        # Tell the entry widget to watch this variable.
        self.entrybox["textvariable"] = self.contents

        # Define a callback for when the user hits return.
        # It prints the current value of the variable.
        self.entrybox.bind('<Key-Return>',
                             self.print_contents)
        
        self.entrybox.bind("<Enter>", self.turn_red)
        self.entrybox.bind("<Leave>", self.turn_blue)
    
    def turn_red(self, event):
        event.widget["foreground"] = "red"        
    def turn_blue(self, event):
        event.widget["foreground"] = "blue"        
        #event.widget.set("Done")        
        
    def print_contents(self, event):
        print("Hi. The current entry content is:",
              self.contents.get(), self.entrybox.get(), event.widget.get())

window = tk.Tk()
myapp = App(window)
myapp.master.title("My Do-Nothing Application")
myapp.mainloop()