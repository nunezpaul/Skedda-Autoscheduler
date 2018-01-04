# Skedda-Autoscheduler
Python work-around to schedule a recurring event 4 weeks in advance. Code here is used by Raspberry Pi 3B and executed every Tuesday at noon.

# Overview
This is a very hardcoded initial code to work around the Skedda scheduling system. Caltech does not allow for scheduling beyond 30 days in advance. Since Skedda does not have an option to have a recurring weekly booking and Caltech West Coast Swing uses the room every week (except 3 times a year) this is very annoying to do manually.  

# Dependencies
Mozilla Firefox == 52.5.2  
selenium == 3.8.0  
geckodriver == 0.17.0-arm7hf  
pyvirtualdisplay == 0.2.1  
xvfb == version as of 12/26/2017  


# Setting Up Recurring Scheduling

In terminal:

```
sudo crontab -e
```

below all the commented information about crontab enter

```
SKEDDA_UN={delete brackets. insert your username}
SKEDDA_PW={delete brackets. insert your password}
PATH={delete brackets. enter env into the CLI and copy-pasta the value you have on your machine}

0 12 * * 2 python ~/path/to/file/scheduleMon.py
5 12 * * 2 python ~/path/to/file/scheduleWed.py
```

Save changes and exit.

Now your system will use pre-determined settings to make the bookings every Tuesday at noon and 5 passed noon for Monday and Wednesday 27  and 29 days in advance, respectively. If you would like to change the time or how many weeks in advance the scheduling is suppose to happen then you can modify  AutoScheduler.py.
