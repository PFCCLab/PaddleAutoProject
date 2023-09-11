FROM python:3.8

RUN pip install requests schedule

COPY . /home/code/PaddleAutoProject

RUN cd /home/code/PaddleAutoProject/HackathonBot && python bot.py