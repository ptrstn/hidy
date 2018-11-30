[![Build Status](https://travis-ci.com/ptrstn/hidy.svg?branch=master)](https://travis-ci.com/ptrstn/hidy)
[![codecov](https://codecov.io/gh/ptrstn/hidy/branch/master/graph/badge.svg)](https://codecov.io/gh/ptrstn/hidy)

# Hidy

A high dpi multi monitor display configurator.

## Install

```bash
pip install git+https://github.com/ptrstn/hidy
```

## Usage

### Configuration files

First specify the monitors you want to use in configuration files such as:

```yaml
# HDMI1-work.yml
output: HDMI1
width: 1920
height: 1200
scale: 1.25
```

```yaml
# eDP1.yml
output: eDP1
width: 2560
height: 1440
```

More examples can be found in the ```examples``` directory.

### Apply configuration

Following command configures 2 monitors ```HDMI1``` and ```eDP1``` in the order left to right:

```bash
hidy HDMI1-work.yml eDP1.yml 
```

This causes the following ```xrandr``` command to be executed internally:

```bash
xrandr --output HDMI1 --auto --mode 1920x1200 --panning 2400x1500+0+0 --scale 1.25x1.25 --pos 0x0 --output eDP1 --auto --mode 2560x1440 --pos 2400x0
```