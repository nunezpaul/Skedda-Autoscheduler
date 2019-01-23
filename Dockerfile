FROM debian:buster

USER root
COPY ./config.py ./skedda/config.py
COPY ./skedda_scheduler.py ./skedda/skedda_scheduler.py

RUN \
  apt-get update \
  && echo '**** Set up firefox *****' \
  && apt-get install -y firefox-esr \
  && apt-get install -y wget \
  && apt-get install -y xauth

RUN \
  echo '**** Set up geckodriver ****' \
  && wget https://github.com/mozilla/geckodriver/releases/download/v0.18.0/geckodriver-v0.18.0-linux64.tar.gz \
  && tar -xvzf geckodriver* \
  && chmod +x geckodriver \
  && mv geckodriver /usr/local/bin/ \
  && rm geckodriver*

RUN \
  echo '**** Set up python **** ' \
  && apt-get install -y python3 python3-pip

RUN \
  echo '**** Set up selenium **** ' \
  && pip3 install -U selenium==3.141.0


