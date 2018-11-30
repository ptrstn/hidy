from hidy.monitor import Monitor


class TestMonitor:
    def test_init(self):
        monitor = Monitor(2560, 1440)
        assert monitor.width == 2560
        assert monitor.height == 1440
        assert monitor.output is None

    def test_example(self):
        eDP1 = Monitor(2560, 1440, output="eDP1")
        HDMI1 = Monitor(1280, 1024, output="HDMI1")

        HDMI1.scale = 2

        assert 2560 == eDP1.panning_width
        assert 1440 == eDP1.panning_height

        assert 2560 == HDMI1.panning_width
        assert 2048 == HDMI1.panning_height
