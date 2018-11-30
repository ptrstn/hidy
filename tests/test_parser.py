from hidy.parser import parse_config


# TODO mock example config
class TestParser:
    def test_parser(self):
        config = "examples/eDP1.yml"
        monitor = parse_config(config)
        assert "eDP1" == monitor.output
        assert 2560 == monitor.width
        assert 1440 == monitor.height
