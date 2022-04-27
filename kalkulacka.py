import tkinter as tk
from tkinter import Listbox, END
from os.path import basename, splitext

class Application(tk.Tk):
    name = basename(splitext(basename(__file__.capitalize()))[0])
    name = "Kalkulacka"
    
    def __init__(self):
        super().__init__(className=self.name)
        self.title(self.name)        
        self.bind("<Return>", self.vepsani)

        self.var_field = tk.Variable()

        self.entry_field = tk.Entry(self, textvariable = self.var_field)
        self.entry_field.grid(row = 0)
        
        self.listbox = Listbox(self)
        self.listbox.grid(row = 1)

        self.btn_quit = tk.Button(self, text = "Zavřít", command = self.quit)
        self.btn_quit.grid()

        self.cisla = []
        self.priklad = {}
        self.priklad["+"] = lambda a, b: a + b
        self.priklad["-"] = lambda a, b: a - b
        self.priklad["*"] = lambda a, b: a * b
        self.priklad["/"] = lambda a, b: a / b
        self.priklad["//"] = lambda a, b: a // b
        self.priklad["**"] = lambda a, b: a ** b

    def vepsani(self, event = None):
        raw = self.var_field.get().split()
        if len(raw) == 0:
            pocet = 1

        else:
            pocet = len(raw)

        for i in range(0, pocet):
                item = raw[i]
                
                try:
                    self.cisla.append(float(item))
                except:
                    pass

                if item in self.priklad.keys():
                    if len(self.cisla) >= 2:
                        b = self.cisla.pop()
                        a = self.cisla.pop()
                        self.cisla.append(self.priklad[item](a, b))
                        self.listbox.insert(END, self.priklad[item](a, b))
                
                self.vysledek()

    def vysledek(self):
        self.var_field.set("")
        self.listbox.delete(0, END)
        for item in self.cisla:
            self.listbox.insert(END, item)

    def quit(self, event = None):
        super().quit()

app = Application()
app.mainloop()
