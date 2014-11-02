class Floor(object):

    def __init__(self, w, number, SH):
        self.number = number
        self.elevs = []
        if self.number<9:
            self.upb = Upbutton(w, self.number, SH)
        if self.number>0:
            self.dwb = Downbutton(w, self.number, SH)
        self.label = Floordisplay(w, self.number, SH)
        self.display = Optelevdisplay(w, self.number, SH)
        self.display.floor = self


class Upbutton(object):

    def __init__(self, w, number, SH):
        self.floor = None
        self.on = False

        self.body = w.create_polygon([520, 15+(2*(9-number)+1)*SH/24, 540, 
            15+(2*(9-number)+1)*SH/24, 530, 30+(9-number)*SH/12], outline="black", 
            fill="#666", activefill="#FF0000", width="2")

    def update(self, w, SH):
        """ Called each frame. """
        if self.on:
            w.itemconfigure(self.body, fill="#0f0")
        else:
            w.itemconfigure(self.body, fill="#666")
        w.update()

class Downbutton(object):

    def __init__(self, w, number, SH):
        self.floor = None
        self.on = False

        self.body = w.create_polygon([520, 25+(2*(9-number)+1)*SH/24, 540, 
            25+(2*(9-number)+1)*SH/24, 530, 10+((9-number)+1)*SH/12], outline="black", 
            fill="#666", activefill="#FF0000", width="2")

    def update(self, w, SH):
        """ Called each frame. """
        if self.on:
            w.itemconfigure(self.body, fill="#0f0")
        else:
            w.itemconfigure(self.body, fill="#666")
        w.update()



class Floordisplay(object):

    def __init__(self, w, floor, SH):
        self.floor = floor
        if self.floor==0:
            self.body = w.create_text(50, 20+(2*(9-self.floor)+1)*SH/24, text='Floor: G', fill='#258', font="Purisa 10 bold")
        else:
            self.body = w.create_text(50, 20+(2*(9-self.floor)+1)*SH/24, text='Floor: '+str(self.floor), fill='#258', font="Purisa 10 bold")


class Optelevdisplay(object):

    def __init__(self, w, num, SH):
        self.num = num
        self.floor = None
        self.body = w.create_rectangle(560, (2*(9-self.num)+1)*SH/24, 600, 
            40+(2*(9-self.num)+1)*SH/24, fill='#6af')
        self.bodytext = w.create_text(580, 20+(2*(9-self.num)+1)*SH/24, text='--')

    def update(self, w):
        if len(self.floor.elevs)>0:
            for e in self.floor.elevs:
                if e.overloaded:
                    return
            w.itemconfig(self.body, fill='#6fa')
            w.itemconfig(self.bodytext, text='--')
            for e in self.floor.elevs:
                if self.num in e.dest:
                    if self.num==0:
                        w.itemconfig(self.floor.display.bodytext, text='G')
                    else:
                        w.itemconfig(self.floor.display.bodytext, text=str(self.num))
                    break