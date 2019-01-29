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
- Install docker. (https://docs.docker.com/install/)
- Clone this repo (`git clone https://github.com/nunezpaul/Skedda-Autoscheduler.git`)
- Build the base and final docker images by `bash path/to/build_docker_images.sh`

Any updates will be to the final docker image so that all images do not need to be rebuilt. The building process for the 
intermediate docker image can take a while.

# Run
`docker run -it -rm skedda python3 skedda/skedda_scheduler.py \
--username $SKEDDA_UN --password $SKEDDA_PW --submit --num_days_away 0 --num_weeks_away 4 --debug`

Explanation of the args:
- `-it` creates an interactive session that attaches to your terminal. This way you can observe the outputs. I send the 
the outputs to an email so that I can double check that it's working.
- `-rm` removes the container associated container from an image. If not removed then you will continue to create new 
containers. In the future, I will attempt to re-use the last created container.
- `--username` email that is associated with the skedda account
- `--password` password that is associated with skedda account
- `--submit` is the boolean flag that will determine if the results are to be submitted or not. Useful for debugging
- `--num_days_away` how many offset days from the current day will the event be scheduled. (This is added to the offset
weeks. Default is 1.) 
- `--num_weeks_away` how many offset weeks from the current day will the event be scheduled. (This is added to the 
offset days. Default is 4.)
- `--debug` will take screenshots of the scheduling process at select key points. This is currently necessary since some
elements will not show unless a screenshot is taken. To recover the screenshots for debugging purposes then you must 
remove `-rm` to keep the resulting container and files. To transfer to the host find the id of the container. Create the 
env CONTAINER to contain the ID then run:

`for i in {1..13}; do docker container cp $CONTAINER\:/test$i\.png ./; done` 

You will find that there are 13 files called test(1-13).png which are the screenshots. You can change the location where 
they are sent by replacing the `./` with `path/to/desired/directory`

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
```

Save changes and exit.

Now your system will use pre-determined settings to make the bookings every Tuesday at noon and 5 passed noon for Monday
 and Wednesday 27  and 29 days in advance, respectively. If you would like to change the time or how many weeks in 
 advance the scheduling is suppose to happen then you can modify skedda_scheduler.py.