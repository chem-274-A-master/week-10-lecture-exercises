"""
Create a decorator called `timer` that times how long it takes a function to execute.

You can get the current time by importing time and calling time.time(). 
You can store the time when the function starts executing and when the function stops. 
We did this during the bootcamp. 
Your decorator should print "elapsed time: {value}"

Reminder, to time Python code, you can do:
```
start = time.time()
**CODE**
end = time.time()

elapsed = end - start
print(f"elapsed time: {elapsed}")
```
"""

import time

@timer
def my_function(n):
  for i in range(n):
    i = i **2

if __name__ == "__main__":
  my_function(100000)