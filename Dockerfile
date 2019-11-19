FROM python:3
ADD bot.py /
ADD SMS.py /
ADD secret.json /
RUN pip install pystrich
RUN pip install tweepy
RUN pip install discord
RUN pip install twilio
CMD [ "python", "./bot.py" ]