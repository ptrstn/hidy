from hidy.screen import Screen


class Configurator:
    def __init__(self, *args):
        self.screen = Screen()
        for monitor in args:
            self.add_monitor(monitor)

    def add_monitor(self, monitor):
        self.screen.add_monitor(monitor)

    def xrandr_command(self):
        command = "xrandr"

        for panning in self.screen.pannings:
            monitor = panning.monitor

            command += " --output {}".format(monitor.output)
            command += " --auto"
            command += " --mode {}x{}".format(monitor.width, monitor.height)

            if panning.width != monitor.width:
                command += " --panning {}x{}+{}+{}".format(
                    panning.width,
                    panning.height,
                    panning.x_position,
                    panning.y_position,
                )
                command += " --scale {}x{}".format(monitor.scale, monitor.scale)

            command += " --pos {}x{}".format(panning.x_position, panning.y_position)

        return command
