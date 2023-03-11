class Rectangular:
    def __init__(self, x1, y1, x2, y2, x3, y3, x4, y4):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.x3 = x3
        self.y3 = y3
        self.x4 = x4
        self.y4 = y4

    def get_left_up(self):
        return self.x1, self.y1

    def get_right_up(self):
        return self.x2, self.y2

    def get_left_down(self):
        return self.x3, self.y3

    def get_right_down(self):
        return self.x4, self.y4

    def get_width(self):
        return self.x2 - self.x1 + 1

    def get_height(self):
        return self.y3 - self.y1 + 1
