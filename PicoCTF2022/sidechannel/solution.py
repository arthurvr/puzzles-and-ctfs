from time import *
from subprocess import *

# The program tells us itself that we're looking for an 8-digit pin.
pin = list("99999999")
times = []

# For every position in the pin... try every number.
for i in range(8):
    for num in range(10):
        pin[i] = str(num)
        execution = Popen("./pin_checker",
                        stdin=PIPE,
                        stdout=PIPE,
                        universal_newlines=True,
                        shell=True)

        start = time_ns()
        out = execution.communicate(input="".join(pin))[0]
        times.append(time_ns() - start)

    # Keep only the one with the max time
    pin[i] = str(times.index(max(times)))

    # Reset timing results
    times = []
    print("".join(pin))
