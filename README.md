# wakelight

This is a small experiment where I tried to make my laptop work as a combined alarm and wakelight, while also showing an inspirational quote to start the day. It's not very good, but I think it's a cool thought that I want to come back to later. wakelight.py is horrible right now, but it *kind of* works.

Beepjs is installed as a git submodule as I couldn't find it in any CDN or package registry, and I don't want to check in that code in this repository.

Uses xbacklight, redshift, and xdotool to manipulate the screen as a source of light:
- xbacklight to adjust screen brightness from low to high.
- redshift to adjust screen gamma values in order to adjust color temperature from low to high.
- xdotool to move the mouse around a bit, in order to make the screen not fall asleep.