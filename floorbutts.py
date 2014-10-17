class Floorbutt(object):

    def __init__(self, w, floor, direc, SH):
        self.floor = floor
        self.direc = direc # 0 = UP, 1 = DOWN
        self.on = False

        if self.direc==0:
            self.body = w.create_polygon([520, 15+(2*self.floor+1)*SH/24, 540, 
                15+(2*self.floor+1)*SH/24, 530, 30+self.floor*SH/12], outline="black", 
                fill="#666", activefill="#0d0", width="2")

        else:
            self.body = w.create_polygon([520, 25+(2*self.floor+1)*SH/24, 540, 
                25+(2*self.floor+1)*SH/24, 530, 10+(self.floor+1)*SH/12], outline="black", 
                fill="#666", activefill="#0d0", width="2")

    def update(self, w, SH):
        """ Called each frame. """
        if self.on:
            w.itemconfigure(self.body, fill="#0f0")
        else:
            w.itemconfigure(self.body, fill="#666")
        w.update()
