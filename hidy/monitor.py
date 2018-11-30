class Monitor:
    def __init__(self, width, height, scale=1, output=None):
        self.width = width
        self.height = height
        self.scale = scale
        self.output = output

    @property
    def panning_width(self):
        return int(self.width * self.scale)

    @property
    def panning_height(self):
        return int(self.height * self.scale)
