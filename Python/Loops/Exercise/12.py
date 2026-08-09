#Exponential Backoff
#This is used in network communication to manage retries after a failure. The wait time between retries increases exponentially, which helps to reduce the load on the server and increase the chances of a successful retry.

import time
wait_time=1
max_retries=5
attempts=0

while attempts<max_retries:
    print("Attempt",attempts+1,"-wait time:",wait_time)
    time.sleep(wait_time)
    wait_time*=2
    attempts+=1