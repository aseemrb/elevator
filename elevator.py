class Elevator(object):

    def __init__(self, w, number, SW, SH, floor=0, direc=''):
        self.num = number
        self.direc = direc
        self.dest = -1
        self.vel = 0
        self.floor = floor
        self.butt = None
        color = '#000000'
        self.body = w.create_rectangle(100*self.num, 20+(9-self.floor)*SH/12, 
                                        100*(self.num+1), 20+(10-self.floor)*SH/12, 
                                        fill="#333", activefill="#000")
        self.x = w.coords(self.body)[0]
        self.y = w.coords(self.body)[1]
        
    def update(self, w, SH):
        """ Called each frame. """
        if self.y>=20+9*SH/12:
            self.vel = -abs(self.vel)
        elif self.y<=20:
            self.vel = abs(self.vel)
        if self.y==20+self.dest*SH/12:
            self.vel=0
            self.butt.on = False
            self.floor = 9-self.butt.floor
            self.butt = None
            self.dest = -1
        w.move(self.body, 0, self.vel)
        # w.move(self.label, self.vel, 0)
        self.x = w.coords(self.body)[0]
        self.y = w.coords(self.body)[1]
        w.update()
