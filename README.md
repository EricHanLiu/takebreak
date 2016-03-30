#Take Break
A small program to remind yourself to rest your eyes from the strain of staring at that terminal window (or from the strain of playing video games).

##How to use
  1. Clone the repository
  2. Edit your crontab with `crontab -e` in terminal
    - NOTE: If you're unsure how, take a look at my Motivation-SMS repository's README file or read [this guide] (https://help.ubuntu.com/community/CronHowto)
  3. Add the following lines
```
0 * * * * /usr/bin/python /pathto/therepository/takebreak/takebreak.py
20 * * * * /usr/bin/python /pathto/therepository/takebreak/takebreak.py
40 * * * * /usr/bin/python /pathto/therepository/takebreak/takebreak.py
```

##What now?
Just wait! Every 20 minutes, a system notification will display telling you to rest your eyes.

This follows the recommended 20/20/20 rule, further explained [here] (https://opto.ca/health-library/the-20-20-20-rule).
