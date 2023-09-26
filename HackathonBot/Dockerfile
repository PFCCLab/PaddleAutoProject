FROM python:3.8

RUN pip install requests schedule

WORKDIR /home/code/HackathonBot

COPY . /home/code/HackathonBot

# 代理环境变量
ENV HTTP_PROXY=""  HTTPS_PROXY=""

# token环境变量
ENV ISSUSE_TOKEN=""  COMMENT_TOKEN=""

CMD ["python", "bot.py"]