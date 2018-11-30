from hidy.monitor import Monitor
from hidy.screen import Screen


class TestScreen:
    def test_init(self):
        screen = Screen()
        assert 0 == screen.width
        assert 0 == screen.height

    def test_total_resolution(self):
        screen = Screen()

        screen.add_monitor(Monitor(2560, 1440))

        assert 2560 == screen.width
        assert 1440 == screen.height

        screen.add_monitor(Monitor(1280, 1024, 1.25))

        assert 4160 == screen.width
        assert 1440 == screen.height

        screen.pannings.clear()

        assert 0 == screen.width
        assert 0 == screen.height

        screen.add_monitor(Monitor(1280, 1024, 1.25))

        assert 1600 == screen.width
        assert 1280 == screen.height

    def test_position(self):
        screen = Screen()

        screen.add_monitor(Monitor(2560, 1440))
        assert 0 == screen.pannings[0].x_position
        assert 0 == screen.pannings[0].y_position

        screen.add_monitor(Monitor(1280, 1024, 1.25))
        assert 2560 == screen.pannings[1].x_position
        assert 0 == screen.pannings[1].y_position
