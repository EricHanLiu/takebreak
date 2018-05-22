# Take Break
A small program to remind yourself to rest your eyes from the strain of staring at that terminal window (or from the strain of playing video games).

There is a script for both macOS and Linux. 

## Using Linux
  1. Clone this repository.
  2. Edit your crontab with `crontab -e` in terminal
  3. Add the following line, or the second one if necessary (honestly I'm not sure why this is required but the first line alone doesn't work for me on Ubuntu 16.04).

```
*/20 * * * * /usr/bin/python /path/to/repository/takebreak/takebreak.py
*/20 * * * * eval "export $(egrep -z DBUS_SESSION_BUS_ADDRESS /proc/$(pgrep -u $LOGNAME gnome-session)/environ)"; /usr/bin/python /path/to/repository/takebreak/takebreak.py
```

# Using macOS
If using a macOS system, you'll want to alter your crontab a little bit to something like this:
```
*/20 * * * * /usr/bin/osascript /path/to/script/takebreak.scpt
```

## What now?
Just wait! Every 20 minutes, a system notification will display telling you to rest your eyes.

This follows the recommended 20/20/20 rule, further explained [here](https://opto.ca/health-library/the-20-20-20-rule).
