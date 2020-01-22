FROM python:3.6-alpine

# Install a decent datetime formatter the default Python one is problematic
RUN pip install arrow

# Copy the code to be run
COPY ./random-logger/random-logger.py /

# The total number of messags to create before finishing
ENV TOTAL_MSGS 100

# The number of msgs after which to generate a multi line one
ENV MULTILINE_FREQUENCY 10

# The period to sleep, between LOW and HIGH in seconds. Can be fraction such as 0.5 seconds
ENV LOW_SLEEP_PERIOD 1000
ENV HIGH_SLEEP_PERIOD 5000

# The number of log messages to generate, between LOW and HIGH
ENV LOW_MSGS_TO_GENERATE 10
ENV HIGH_MSGS_TO_GENERATE 20

CMD ["python","-u","./random-logger.py"]




