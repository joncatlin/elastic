# Use a decent datetime library like arrow as default lib has issues
import arrow
import time
import random
import os

# Define the loglevel
loglevel = 'INF'

# Initialize the counter
count = 0

# The total number of msgs to send
total_msgs = int(os.environ['TOTAL_MSGS'])
total_msgs -= 1

# Get the frequency of multi line messges to generate
multiline_frequency = int(os.environ['MULTILINE_FREQUENCY'])

# Get the environment variables
low_sleep_period = int(os.environ['LOW_SLEEP_PERIOD'])
high_sleep_period = int(os.environ['HIGH_SLEEP_PERIOD'])
low_msgs_to_generate = int(os.environ['LOW_MSGS_TO_GENERATE'])
high_msgs_to_generate = int(os.environ['HIGH_MSGS_TO_GENERATE'])

while (count < total_msgs):
    # Determine the number of log messages to generate
    num_msgs = random.randint(low_msgs_to_generate,high_msgs_to_generate) - 1

    for x in range(0, num_msgs):
        # Generate the number of messages specified
        # Check the multi line frequency and if the count is divisible then print multi line message
        # otherwise send a normal msg
        if (count % multiline_frequency == 0):
            print ("%s [%s] Message number - %d\nLine 2 for message number - %d\nLine 3 for message number - %d\nLine 4 for message number - %d" % (arrow.now('local').isoformat(), loglevel, count, count, count, count))
        else:
            print ("%s [%s] Message number - %d" % (arrow.now('local').isoformat(), loglevel, count))
        count += 1
    
    # Determine how long to sleep before sending more messages
    sleep_period = random.randint(low_sleep_period,high_sleep_period)
    time.sleep(sleep_period)
