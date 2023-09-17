FROM python:3.8

RUN pip install requests schedule

WORKDIR /home/code/HackathonBot

COPY . /home/code/HackathonBot

# 代理环境变量
ENV HTTP_PROXY=http://127.0.0.1:7890  HTTPS_PROXY=http://127.0.0.1:7890

# token环境变量
ENV ISSUSE_TOKEN=""  COMMENT_TOKEN=""

# 是否为黑客松还是框架护航，True为黑客松
ENV HACKATHON=True

CMD ["python", "bot.py"]