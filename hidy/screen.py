from hidy.panning import Panning


class Screen:
    def __init__(self):
        self.pannings = []

    def add_monitor(self, monitor):
        monitor.x_position = self.width
        self.pannings.append(Panning(monitor, self.width))

    @property
    def width(self):
        return sum(panning.width for panning in self.pannings) if self.pannings else 0

    @property
    def height(self):
        return max(panning.height for panning in self.pannings) if self.pannings else 0
