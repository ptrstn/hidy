from hidy.configurator import Configurator
from hidy.monitor import Monitor


class TestHidy:
    def test_hidy_1_25(self):
        eDP1 = Monitor(2560, 1440, output="eDP1")
        HDMI1 = Monitor(1280, 1024, scale=1.25, output="HDMI1")

        hidy = Configurator()
        hidy.add_monitor(eDP1)
        hidy.add_monitor(HDMI1)

        expected_command = (
            "xrandr "
            "--output eDP1 --auto --mode 2560x1440 --pos 0x0 "
            "--output HDMI1 --auto --mode 1280x1024 "
            "--panning 1600x1280+2560+0 "
            "--scale 1.25x1.25 "
            "--pos 2560x0"
        )

        assert expected_command == hidy.xrandr_command()

    def test_hidy_resolution_change(self):
        eDP1 = Monitor(2560, 1440, output="eDP1")
        HDMI1 = Monitor(1280, 1024, scale=1.25, output="HDMI1")

        hidy = Configurator(eDP1, HDMI1)

        expected_command = (
            "xrandr "
            "--output eDP1 --auto --mode 2560x1440 --pos 0x0 "
            "--output HDMI1 --auto --mode 1280x1024 "
            "--panning 1600x1280+2560+0 "
            "--scale 1.25x1.25 "
            "--pos 2560x0"
        )

        assert expected_command == hidy.xrandr_command()

        HDMI1.width = 1920
        HDMI1.height = 1080

        expected_command = (
            "xrandr "
            "--output eDP1 --auto --mode 2560x1440 --pos 0x0 "
            "--output HDMI1 --auto --mode 1920x1080 "
            "--panning 2400x1350+2560+0 "
            "--scale 1.25x1.25 "
            "--pos 2560x0"
        )

        assert expected_command == hidy.xrandr_command()

    def test_hidy_1_25_flipped(self):
        eDP1 = Monitor(2560, 1440, output="eDP1")
        HDMI1 = Monitor(1280, 1024, scale=1.25, output="HDMI1")

        hidy = Configurator(HDMI1, eDP1)

        expected_command = (
            "xrandr "
            "--output HDMI1 --auto --mode 1280x1024 "
            "--panning 1600x1280+0+0 "
            "--scale 1.25x1.25 "
            "--pos 0x0 "
            "--output eDP1 --auto --mode 2560x1440 --pos 1600x0"
        )

        assert expected_command == hidy.xrandr_command()

    def test_hidy_2(self):
        eDP1 = Monitor(2560, 1440, output="eDP1")
        HDMI1 = Monitor(1280, 1024, scale=2, output="HDMI1")

        hidy = Configurator(eDP1, HDMI1)

        expected_command = (
            "xrandr "
            "--output eDP1 --auto --mode 2560x1440 --pos 0x0 "
            "--output HDMI1 --auto --mode 1280x1024 "
            "--panning 2560x2048+2560+0 "
            "--scale 2x2 "
            "--pos 2560x0"
        )

        assert expected_command == hidy.xrandr_command()

    def test_hidy_2_flipped(self):
        eDP1 = Monitor(2560, 1440, output="eDP1")
        HDMI1 = Monitor(1280, 1024, scale=2, output="HDMI1")

        hidy = Configurator(HDMI1, eDP1)

        expected_command = (
            "xrandr "
            "--output HDMI1 --auto --mode 1280x1024 "
            "--panning 2560x2048+0+0 "
            "--scale 2x2 "
            "--pos 0x0 "
            "--output eDP1 --auto --mode 2560x1440 --pos 2560x0"
        )

        assert expected_command == hidy.xrandr_command()

    def test_hidy_multiple_scales(self):
        eDP1 = Monitor(2560, 1440, scale=1.5, output="eDP1")
        HDMI1 = Monitor(1280, 1024, scale=2, output="HDMI1")

        hidy = Configurator(HDMI1, eDP1)

        expected_command = (
            "xrandr "
            "--output HDMI1 --auto --mode 1280x1024 "
            "--panning 2560x2048+0+0 "
            "--scale 2x2 "
            "--pos 0x0 "
            "--output eDP1 --auto --mode 2560x1440 "
            "--panning 3840x2160+2560+0 "
            "--scale 1.5x1.5 "
            "--pos 2560x0"
        )

        assert expected_command == hidy.xrandr_command()

    def test_three_monitors(self):
        eDP1 = Monitor(2560, 1440, scale=1.5, output="eDP1")
        HDMI1 = Monitor(1280, 1024, scale=2, output="HDMI1")
        HDMI2 = Monitor(1920, 1080, scale=1.25, output="HDMI2")

        hidy = Configurator(HDMI1, eDP1, HDMI2)

        expected_command = (
            "xrandr "
            "--output HDMI1 --auto --mode 1280x1024 "
            "--panning 2560x2048+0+0 "
            "--scale 2x2 "
            "--pos 0x0 "
            "--output eDP1 --auto --mode 2560x1440 "
            "--panning 3840x2160+2560+0 "
            "--scale 1.5x1.5 "
            "--pos 2560x0 "
            "--output HDMI2 --auto --mode 1920x1080 "
            "--panning 2400x1350+6400+0 "
            "--scale 1.25x1.25 "
            "--pos 6400x0"
        )

        assert expected_command == hidy.xrandr_command()

        HDMI2.scale = 1

        expected_command = (
            "xrandr "
            "--output HDMI1 --auto --mode 1280x1024 "
            "--panning 2560x2048+0+0 "
            "--scale 2x2 "
            "--pos 0x0 "
            "--output eDP1 --auto --mode 2560x1440 "
            "--panning 3840x2160+2560+0 "
            "--scale 1.5x1.5 "
            "--pos 2560x0 "
            "--output HDMI2 --auto --mode 1920x1080 "
            "--pos 6400x0"
        )

        assert expected_command == hidy.xrandr_command()

    def test_no_scale(self):
        eDP1 = Monitor(2560, 1440, output="eDP1")
        HDMI1 = Monitor(1280, 1024, output="HDMI1")

        hidy = Configurator(HDMI1, eDP1)

        expected_command = (
            "xrandr "
            "--output HDMI1 --auto --mode 1280x1024 "
            "--pos 0x0 "
            "--output eDP1 --auto --mode 2560x1440 "
            "--pos 1280x0"
        )

        assert expected_command == hidy.xrandr_command()
