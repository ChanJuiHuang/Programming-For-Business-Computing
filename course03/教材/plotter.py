import tkinter as tk
import tkinter.font as tkFont
import matplotlib.pyplot as pyplot
from PIL import ImageTk
import os


class Plotter(tk.Frame):

    def __init__(self):
        tk.Frame.__init__(self)
        self.createWidgets()
        self.grid()

    def createWidgets(self):
        f = tkFont.Font(size=16)

        self.lblX = tk.Label(self, text="x:", height=1, width=3, font=f)
        self.lblY = tk.Label(self, text="y:", height=1, width=3, font=f)

        self.txtX = tk.Text(self, height=1, width=40, font=f)
        self.txtY = tk.Text(self, height=1, width=40, font=f)

        self.btnLoad = tk.Button(self, text="plot!", height=1, width=5, command=self.clickBtnLoad, font=f)
        self.cvsMain = tk.Canvas(self, width=800, height=600, bg="white")

        self.lblX.grid(row=0, column=0, sticky=tk.E)
        self.lblY.grid(row=1, column=0, sticky=tk.E)
        self.txtX.grid(row=0, column=1, sticky=tk.NE + tk.SW)
        self.txtY.grid(row=1, column=1, sticky=tk.NE + tk.SW)
        self.btnLoad.grid(row=0, rowspan=2, column=2, sticky=tk.NE + tk.SW)
        self.cvsMain.grid(row=2, column=0, columnspan=3, sticky=tk.NE + tk.SW)

    def clickBtnLoad(self):
        x = self.txtX.get("1.0", tk.END).split(",")  # 1.0: the first line,
        for i in range(len(x)):  # the 0th character
            x[i] = float(x[i])  # tk.END: until the last character
        y = self.txtY.get("1.0", tk.END).split(",")
        for i in range(len(y)):
            y[i] = float(y[i])
        
        self.makeScatter(x, y)
        self.imageMain = ImageTk.PhotoImage(file="temp.png")
        self.cvsMain.create_image(400, 300, image=self.imageMain, anchor=tk.CENTER)
        os.system('rm temp.png')

        # pyplot.plot(x, y, 'bo')
        # pyplot.show()

    def makeScatter(self, x, y):
        pyplot.figure()  # to create a new figure
        pyplot.plot(x, y, 'bo')
        rangeX = max(x) - min(x)
        pyplot.xlim(min(x) - rangeX * 0.1, max(x) + rangeX * 0.1)
        rangeY = max(y) - min(y)
        pyplot.ylim(min(y) - rangeY * 0.1, max(y) + rangeY * 0.1)

        for i, j in zip(x, y):
            pyplot.annotate(f'({i}, {j})', xy=(i, j))
        pyplot.savefig("temp.png")


pl = Plotter()
pl.master.title("My Plotter")
pl.mainloop()
