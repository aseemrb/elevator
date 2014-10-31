class Panel(object):

    def __init__(self, w, number):
        self.num = number
        self.elev = None

        if self.num==1:
            self.body = w.create_rectangle(100, 50, 250, 250, 
                fill="#9bc")
        elif self.num==2:
            self.body = w.create_rectangle(350, 50, 500, 250, 
                fill="#9bc")
        elif self.num==3:
            self.body = w.create_rectangle(100, 350, 250, 550, 
                fill="#9bc")
        else:
            self.body = w.create_rectangle(350, 350, 500, 550, 
                fill="#9bc")
        self.x = w.coords(self.body)[0]
        self.y = w.coords(self.body)[1]
        self.label = w.create_text(self.x+80, self.y-10, text='Elevator'+str(self.num))
        self.makebuttons(w)
        self.makelabels(w)

    def makebuttons(self, w):
        self.b1 = w.create_rectangle(self.x, self.y+80, self.x+50, self.y+120, outline="black", 
            fill="#9bc", activefill="#fff", width=2)
        self.b2 = w.create_rectangle(self.x+50, self.y+80, self.x+100, self.y+120, outline="black", 
            fill="#9bc", activefill="#fff", width=2)
        self.b3 = w.create_rectangle(self.x+100, self.y+80, self.x+150, self.y+120, outline="black", 
            fill="#9bc", activefill="#fff", width=2)
        self.b4 = w.create_rectangle(self.x, self.y+40, self.x+50, self.y+80, outline="black", 
            fill="#9bc", activefill="#fff", width=2)
        self.b5 = w.create_rectangle(self.x+50, self.y+40, self.x+100, self.y+80, outline="black", 
            fill="#9bc", activefill="#fff", width=2)
        self.b6 = w.create_rectangle(self.x+100, self.y+40, self.x+150, self.y+80, outline="black", 
            fill="#9bc", activefill="#fff", width=2)
        self.b7 = w.create_rectangle(self.x, self.y, self.x+50, self.y+40, outline="black", 
            fill="#9bc", activefill="#fff", width=2)
        self.b8 = w.create_rectangle(self.x+50, self.y, self.x+100, self.y+40, outline="black", 
            fill="#9bc", activefill="#fff", width=2)
        self.b9 = w.create_rectangle(self.x+100, self.y, self.x+150, self.y+40, outline="black", 
            fill="#9bc", activefill="#fff", width=2)
        self.bopen = w.create_rectangle(self.x, self.y+120, self.x+50, self.y+160, outline="black", 
            fill="#9bc", activefill="#fff", width=2)
        self.bclose = w.create_rectangle(self.x+100, self.y+120, self.x+150, self.y+160, outline="black", 
            fill="#9bc", activefill="#fff", width=2)
        self.b0 = w.create_rectangle(self.x+50, self.y+120, self.x+100, self.y+160, outline="black", 
            fill="#9bc", activefill="#fff", width=2)
        self.bemergency = w.create_rectangle(self.x+50, self.y+160, self.x+100, self.y+200, outline="black", 
            fill="#9bc", activefill="#fff", width=2)

    def makelabels(self, w):
        self.b1label = w.create_text(w.coords(self.b1)[0]+25, w.coords(self.b1)[1]+20, 
            text='1')
        self.b2label = w.create_text(w.coords(self.b2)[0]+25, w.coords(self.b2)[1]+20, 
            text='2')
        self.b3label = w.create_text(w.coords(self.b3)[0]+25, w.coords(self.b3)[1]+20, 
            text='3')
        self.b4label = w.create_text(w.coords(self.b4)[0]+25, w.coords(self.b4)[1]+20, 
            text='4')
        self.b5label = w.create_text(w.coords(self.b5)[0]+25, w.coords(self.b5)[1]+20, 
            text='5')
        self.b6label = w.create_text(w.coords(self.b6)[0]+25, w.coords(self.b6)[1]+20, 
            text='6')
        self.b7label = w.create_text(w.coords(self.b7)[0]+25, w.coords(self.b7)[1]+20, 
            text='7')
        self.b8label = w.create_text(w.coords(self.b8)[0]+25, w.coords(self.b8)[1]+20, 
            text='8')
        self.b9label = w.create_text(w.coords(self.b9)[0]+25, w.coords(self.b9)[1]+20, 
            text='9')
        self.b0label = w.create_text(w.coords(self.b0)[0]+25, w.coords(self.b0)[1]+20, 
            text='G')
        self.bopenlabel = w.create_text(w.coords(self.bopen)[0]+25, w.coords(self.bopen)[1]+20, 
            text='<>')
        self.bcloselabel = w.create_text(w.coords(self.bclose)[0]+25, w.coords(self.bclose)[1]+20, 
            text='><')
        self.bemergencylabel = w.create_text(w.coords(self.bemergency)[0]+25, w.coords(self.bemergency)[1]+20, 
            text='EM')

    def update(self, w):
        """ Called each frame. """
        if self.on:
            w.itemconfigure(self.body, fill="#0f0")
        else:
            w.itemconfigure(self.body, fill="#666")
        w.update()
