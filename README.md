#Take Break
A small program to remind yourself to rest your eyes from the strain of staring at that terminal window (or from the strain of playing video games).

##How to use
  1. Clone the repository
  2. Edit your crontab with `crontab -e` in terminal
    - NOTE: If you're unsure how, take a look at my Motivation-SMS repository's README file or read [this guide] (https://help.ubuntu.com/community/CronHowto)
  3. Add the following lines
```
*/20 * * * * export DISPLAY=:0; /usr/bin/python /pathto/therepository/takebreak/takebreak.py
```

##What now?
Just wait! Every 20 minutes, a system notification will display telling you to rest your eyes.

This follows the recommended 20/20/20 rule, further explained [here] (https://opto.ca/health-library/the-20-20-20-rule).

#NOTE: In the case that crontab doesn't work properly with notify-send (like in my case):
I've uploaded a separate file called nocronbreak.py

Running this file in terminal will provide the same results as the previous crontab method
###However
The terminal will need to be left open to run the script, since nocronbreak uses a sleep function to work.
A minor inconvenience, but hopefully the first method will work for you.
