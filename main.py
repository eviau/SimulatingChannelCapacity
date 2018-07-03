# Simulating Channel Capacity

# All the values in this code are taken from simulated examples.

# https://en.wikipedia.org/wiki/Channel_capacity
# https://en.wikipedia.org/wiki/Noisy-channel_coding_theorem

# goal : to implement a simulator that enables one to beter understand the concept of Shannon's limit.

# channel capacity : https://en.wikipedia.org/wiki/Shannon–Hartley_theorem

# c : the channel capacity in bits per second

# b : bandwith in hertz

# s : average received signal power over the bandwith, watts or volts squared
# n : average power of the noise measured in watts or volts squared
# s/n : signal to noise ratio
# we have the following: C = B log_2 (1 + S/N)

# We will work through the following example, taken from Wikpedia:
# If the SNR is 20 dB, and the bandwidth available is 4 kHz,
#  which is appropriate for telephone communications, 
# then C = 4000 log2(1 + 100) = 4000 log2 (101) = 26.63 kbit/s. 
# Note that the value of S/N = 100 is equivalent to the SNR of 
# 20 dB.

import math
import numpy as np

#  C = 4000 log2(1 + 100)
b = 4000
sn = 20
c = b * math.log(1+b,2)

# probability of bit error p
p = 0.02

# rate of transmission
h = - (p * math.log(p,2) + (1-p)*math.log(1-p))

r = c / (1 - h )


# now we want to explore the property : 
# For any p, rates greater than R(p) are not achievable.

# let's test this. using :
# https://en.wikipedia.org/wiki/Noisy-channel_coding_theorem#Achievability_for_discrete_memoryless_channels




for n in range(100):
    code = np.zeros(n)



