from hidy.monitor import Monitor
from hidy.panning import Panning


class TestPanning:
    def test_panning(self):
        monitor = Monitor(1280, 1024, 1.25)
        panning = Panning(monitor)
        assert 1600 == panning.width
        assert 1280 == panning.height
        assert 0 == panning.x_position
        assert 0 == panning.y_position

    def test_position(self):
        monitor = Monitor(1280, 1024, 1.25)
        panning = Panning(monitor, 2560, 0)
        assert 1600 == panning.width
        assert 1280 == panning.height
        assert 2560 == panning.x_position
        assert 0 == panning.y_position

        panning = Panning(monitor, 1920, 1080)
        assert 1600 == panning.width
        assert 1280 == panning.height
        assert 1920 == panning.x_position
        assert 1080 == panning.y_position

        panning = Panning(monitor, 1024)
        assert 1600 == panning.width
        assert 1280 == panning.height
        assert 1024 == panning.x_position
        assert 0 == panning.y_position
