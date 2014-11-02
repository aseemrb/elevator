class Panel(object):

    def __init__(self, w, number):
        self.num = number
        self.elev = None
        self.b = []
        self.pushin = None
        self.pushout = None
        self.blabel = []
        if self.num==1:
            self.body = w.create_rectangle(100, 50, 250, 210, fill="#000")
        elif self.num==2:
            self.body = w.create_rectangle(350, 50, 500, 210, fill="#000")
        elif self.num==3:
            self.body = w.create_rectangle(100, 350, 250, 510, fill="#000")
        else:
            self.body = w.create_rectangle(350, 350, 500, 510, fill="#000")
        self.x = w.coords(self.body)[0]
        self.y = w.coords(self.body)[1]
        self.label = w.create_text(self.x+80, self.y-10, text='Elevator'+str(self.num))
        self.makebuttons(w)
        self.makelabels(w)

    def makebuttons(self, w):
        self.b.append(w.create_rectangle(self.x+50, self.y+120, self.x+100, self.y+160, outline="black", 
            fill="#9bc", activefill="#fff", width=2))
        self.b.append(w.create_rectangle(self.x, self.y+80, self.x+50, self.y+120, outline="black", 
            fill="#9bc", activefill="#fff", width=2))
        self.b.append(w.create_rectangle(self.x+50, self.y+80, self.x+100, self.y+120, outline="black", 
            fill="#9bc", activefill="#fff", width=2))
        self.b.append(w.create_rectangle(self.x+100, self.y+80, self.x+150, self.y+120, outline="black", 
            fill="#9bc", activefill="#fff", width=2))
        self.b.append(w.create_rectangle(self.x, self.y+40, self.x+50, self.y+80, outline="black", 
            fill="#9bc", activefill="#fff", width=2))
        self.b.append(w.create_rectangle(self.x+50, self.y+40, self.x+100, self.y+80, outline="black", 
            fill="#9bc", activefill="#fff", width=2))
        self.b.append(w.create_rectangle(self.x+100, self.y+40, self.x+150, self.y+80, outline="black", 
            fill="#9bc", activefill="#fff", width=2))
        self.b.append(w.create_rectangle(self.x, self.y, self.x+50, self.y+40, outline="black", 
            fill="#9bc", activefill="#fff", width=2))
        self.b.append(w.create_rectangle(self.x+50, self.y, self.x+100, self.y+40, outline="black", 
            fill="#9bc", activefill="#fff", width=2))
        self.b.append(w.create_rectangle(self.x+100, self.y, self.x+150, self.y+40, outline="black", 
            fill="#9bc", activefill="#fff", width=2))
        self.b.append(w.create_rectangle(self.x, self.y+120, self.x+50, self.y+160, outline="black", 
            fill="#9bc", activefill="#fff", width=2))
        self.b.append(w.create_rectangle(self.x+100, self.y+120, self.x+150, self.y+160, outline="black", 
            fill="#9bc", activefill="#fff", width=2))
        self.b.append(w.create_rectangle(self.x+50, self.y+160, self.x+100, self.y+200, outline="black", 
            fill="#9bc", activefill="#fff", width=2))
        self.pushin = w.create_rectangle(self.x, self.y+160, self.x+50, self.y+200, outline="black", 
            fill="#aaa", activefill="#fff", width=2)
        self.pushout = w.create_rectangle(self.x+100, self.y+160, self.x+150, self.y+200, outline="black", 
            fill="#aaa", activefill="#fff", width=2)

    def makelabels(self, w):
        self.blabel.append(w.create_text(w.coords(self.b[0])[0]+25, w.coords(self.b[0])[1]+20, text='G'))
        self.blabel.append(w.create_text(w.coords(self.b[1])[0]+25, w.coords(self.b[1])[1]+20, text='1'))
        self.blabel.append(w.create_text(w.coords(self.b[2])[0]+25, w.coords(self.b[2])[1]+20, text='2'))
        self.blabel.append(w.create_text(w.coords(self.b[3])[0]+25, w.coords(self.b[3])[1]+20, text='3'))
        self.blabel.append(w.create_text(w.coords(self.b[4])[0]+25, w.coords(self.b[4])[1]+20, text='4'))
        self.blabel.append(w.create_text(w.coords(self.b[5])[0]+25, w.coords(self.b[5])[1]+20, text='5'))
        self.blabel.append(w.create_text(w.coords(self.b[6])[0]+25, w.coords(self.b[6])[1]+20, text='6'))
        self.blabel.append(w.create_text(w.coords(self.b[7])[0]+25, w.coords(self.b[7])[1]+20, text='7'))
        self.blabel.append(w.create_text(w.coords(self.b[8])[0]+25, w.coords(self.b[8])[1]+20, text='8'))
        self.blabel.append(w.create_text(w.coords(self.b[9])[0]+25, w.coords(self.b[9])[1]+20, text='9'))
        self.blabel.append(w.create_text(w.coords(self.b[10])[0]+25, w.coords(self.b[10])[1]+20, text='<>'))
        self.blabel.append(w.create_text(w.coords(self.b[11])[0]+25, w.coords(self.b[11])[1]+20, text='><'))
        self.bemergencylabel = w.create_text(w.coords(self.b[12])[0]+25, w.coords(self.b[12])[1]+20, text='EM')
        self.pushinlabel = w.create_text(w.coords(self.pushin)[0]+25, w.coords(self.pushin)[1]+20, text='+')
        self.pushoutlabel = w.create_text(w.coords(self.pushout)[0]+25, w.coords(self.pushout)[1]+20, text='-')
