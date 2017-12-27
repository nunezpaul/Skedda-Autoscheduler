# Skedda-Autoscheduler
Python work-around to schedule a recurring event 4 weeks in advance. Code here is used by Raspberry Pi 3B and executed every Tuesday at noon.

# Overview
This is a very hardcoded initial code to work around the Skedda scheduling system. Caltech does not allow for scheduling beyond 30 days in advance. Since Skedda does not have an option to have a recurring weekly booking and Caltech West Coast Swing uses the room every week (except 3 times a year) this is very annoying to do manually.

# Dependencies
Coming soon

# Setting Up Recurring Scheduling

In terminal:

```
sudo crontab -e
```

below all the commented information enter

```
0 12 * * 2 python ~/path/to/file/scheduleMon.py
5 12 * * 2 python ~/path/to/file/scheduleWed.py
```

Save changes and exit.

Now your system will use pre-determined settings to make the bookings on 27 days in advance for Monday and 29 days in advance for Wednesday.
