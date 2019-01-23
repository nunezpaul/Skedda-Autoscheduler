# Skedda-Autoscheduler
Python work-around to schedule a recurring events X weeks + Y days in advance. 
Code here is used by Raspberry Pi 3B and executed when scheduled by crontab.

# Overview
This is a refactored code to work around the Skedda scheduling system. Some elements are hardcoded but should be fairly
easy to change and modify. The point of this project is to avoid having a person schedule Caltech Ballroom Dance Club's 
weekly swing social. The limits to scheduling are that it must be between 2 to 30 days in advance. Anything outside of 
this range is rejected. Since we're a student run club, we aren't that disciplined to take care of it weekly so I made
this!

I've updated this such that it should be fairly simple to have up and running with docker.

# Set up
- Install docker.
- From terminal, go to the directory containing the Dockerfile
- Run docker build . -t skedda 

# Setting Up Recurring Scheduling

In terminal:

```
sudo crontab -e
```

below all the commented information about crontab enter

```
SKEDDA_UN={delete brackets. insert your username}
SKEDDA_PW={delete brackets. insert your password}
PATH={delete brackets. enter env into the CLI and copy-pasta the value for PATH you have on your machine}

0 12 * * 2 python ~/path/to/file/scheduleMon.py
5 12 * * 2 python ~/path/to/file/scheduleWed.py
```

Save changes and exit.

Now your system will use pre-determined settings to make the bookings every Tuesday at noon and 5 passed noon for Monday
 and Wednesday 27  and 29 days in advance, respectively. If you would like to change the time or how many weeks in 
 advance the scheduling is suppose to happen then you can modify skedda_scheduler.py.