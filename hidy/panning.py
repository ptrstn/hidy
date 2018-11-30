class Panning:
    def __init__(self, monitor, x_position=0, y_position=0):
        self.monitor = monitor
        self.x_position = x_position
        self.y_position = y_position

    @property
    def width(self):
        return self.monitor.panning_width

    @property
    def height(self):
        return self.monitor.panning_height
