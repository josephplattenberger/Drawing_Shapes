from tkinter import *

class MyPaint:
    def __init__(self):
        window = Tk()
        window.title("MyPaint")
        frame0 = Frame(window)
        frame0.pack()
        frame1 = Frame(window)
        frame1.pack()

        self.xStart = 0
        self.yStart = 0
        self.xEnd = 0
        self.yEnd = 0
        self.currentShape = "line"
        self.color = ""
        self.lastColor = "black"
        self.recent = ""
        self.i = 0

        menubar = Menu(window)
        window.config(menu = menubar)
        drawMenu = Menu(menubar, tearoff = 0)
        menubar.add_cascade(label = "Draw", menu = drawMenu)
        drawMenu.add_command(label = "Line", command = self.processLineButton)
        drawMenu.add_command(label = "Oval", command = self.processOvalButton)
        drawMenu.add_command(label = "Rectangle", \
                             command = self.processRectangleButton)
        drawMenu.add_command(label = "Arc", command = self.processArcButton)
        editMenu = Menu(menubar, tearoff = 0)
        menubar.add_cascade(label = "Edit", menu = editMenu)
        editMenu.add_command(label = "Clear Most Recent", command \
                             = self.clearRecent)
        editMenu.add_command(label = "Clear All", command = self.clearAll)
        colorMenu = Menu(editMenu, tearoff = 0)
        editMenu.add_cascade(label = "Colors", menu = colorMenu)
        colorMenu.add_command(label = "black", command = self.colorBlack)
        colorMenu.add_command(label = "blue", command = self.colorBlue)
        colorMenu.add_command(label = "green", command = self.colorGreen)
        colorMenu.add_command(label = "yellow", command = self.colorYellow)
        colorMenu.add_command(label = "orange", command = self.colorOrange)
        colorMenu.add_command(label = "red", command = self.colorRed)
        colorMenu.add_command(label = "pink", command = self.colorPink)
        colorMenu.add_command(label = "purple", command = self.colorPurple)



        Button(frame0, text = "Line", command = \
               self.processLineButton).grid(row = 1, column = 1)
        Button(frame0, text = "Oval", command = \
               self.processOvalButton).grid(row = 1, column = 2)
        Button(frame0, text = "Rectangle", command = \
               self.processRectangleButton).grid(row = 1, column = 3)
        Button(frame0, text = "Arc", command = \
               self.processArcButton).grid(row = 1, column = 4)
        self.rb = IntVar()
        self.rb.set(2)
        Radiobutton(frame0, text = "Fill", variable = self.rb, value = 1, \
                    command = self.processRadioButton).grid(row = 1, column = 5)
        Radiobutton(frame0, text = "No Fill", variable = self.rb, value = 2, \
                    command = self.processRadioButton).grid(row = 1, column = 6)

        self.canvas = Canvas(frame1, width = 400, height = 300, bg = 'white')
        self.canvas.pack()
        self.canvas.bind('<Button-1>', self.startShape)
        self.canvas.bind('<B1-Motion>', self.drawShapeTemp)
        self.canvas.bind('<ButtonRelease-1>', self.drawShape)

        window.mainloop()

    def colorBlack(self):
        self.lastColor = self.color = "black"
        self.rb.set(1)

    def colorBlue(self):
        self.lastColor = self.color = "blue"
        self.rb.set(1)

    def colorGreen(self):
        self.lastColor = self.color = "green"
        self.rb.set(1)

    def colorYellow(self):
        self.lastColor = self.color = "yellow"
        self.rb.set(1)

    def colorOrange(self):
        self.lastColor = self.color = "orange"
        self.rb.set(1)

    def colorRed(self):
        self.lastColor = self.color = "red"
        self.rb.set(1)

    def colorPink(self):
        self.lastColor = self.color = "pink"
        self.rb.set(1)

    def colorPurple(self):
        self.lastColor = self.color = "purple"
        self.rb.set(1)

    def processLineButton(self):
        self.currentShape = "line"
        
    def processOvalButton(self):
        self.currentShape = "oval"
        
    def processRectangleButton(self):
        self.currentShape = "rectangle"
        
    def processArcButton(self):
        self.currentShape = "arc"

    def processRadioButton(self):
        if self.rb.get() == 2:
            self.color = ""
        else:
            self.color = self.lastColor

    def startShape(self, event):
        self.xStart = event.x
        self.yStart = event.y

    def drawShapeTemp(self, event):
        self.xEnd = event.x
        self.yEnd = event.y
        if self.currentShape == "line":
            self.canvas.delete("lineTag")
            self.canvas.create_line(self.xStart, self.yStart, self.xEnd, \
                                    self.yEnd, fill = self.lastColor, \
                                    tags = "lineTag")
        elif self.currentShape == "oval":
            self.canvas.delete("ovalTag")
            self.canvas.create_oval(self.xStart, self.yStart, self.xEnd, \
                                    self.yEnd, fill = self.color, \
                                    tags = "ovalTag")
        elif self.currentShape == "rectangle":
            self.canvas.delete("rectTag")
            self.canvas.create_rectangle(self.xStart, self.yStart, self.xEnd, \
                                         self.yEnd, fill = self.color, \
                                         tags = "rectTag")
        elif self.currentShape == "arc":
            self.canvas.delete("arcTag")
            self.canvas.create_arc(self.xStart, self.yStart, self.xEnd, \
                                   self.yEnd, fill = self.color, \
                                   tags = "arcTag")
        
    def drawShape(self, event):
        self.xEnd = event.x
        self.yEnd = event.y
        if self.currentShape == "line":
            self.canvas.delete("lineTag")
            recent = self.canvas.create_line(self.xStart, self.yStart, \
                                             self.xEnd, self.yEnd, \
                                             fill = self.lastColor, \
                                             tags = "lineTag" + str(self.i))
            self.recent = self.canvas.gettags(recent)
            self.i += 1
        elif self.currentShape == "oval":
            self.canvas.delete("ovalTag")
            recent = self.canvas.create_oval(self.xStart, self.yStart, \
                                             self.xEnd, self.yEnd, \
                                             fill = self.color, \
                                             tags = "ovalTag" + str(self.i))
            self.recent = self.canvas.gettags(recent)
            self.i += 1
        elif self.currentShape == "rectangle":
            self.canvas.delete("rectTag")
            recent = self.canvas.create_rectangle(self.xStart, self.yStart, \
                                                  self.xEnd, self.yEnd, \
                                                  fill = self.color, \
                                                  tags = "rectTag" + str(self.i))
            self.recent = self.canvas.gettags(recent)
            self.i += 1
        elif self.currentShape == "arc":
            self.canvas.delete("arcTag")
            recent = self.canvas.create_arc(self.xStart, self.yStart, \
                                            self.xEnd, self.yEnd, \
                                            fill = self.color, \
                                            tags = "arcTag" + str(self.i))
            self.recent = self.canvas.gettags(recent)
            self.i += 1

    def clearRecent(self):
        self.canvas.delete(self.recent)

    def clearAll(self):
        for i in self.canvas.find_all():
            self.canvas.delete(i)


MyPaint()
