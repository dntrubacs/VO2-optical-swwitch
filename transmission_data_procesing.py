import os
from agilent_connections import write_laser_amplitude
import numpy as np
from matplotlib import pyplot as plt
import time as time

def get_pd_data() -> float:
    exec(open('pico_Com.py').read())
    pd_data = np.mean(np.load('channel_A_data', allow_pickle=True))
    return pd_data


# laser powers used
laser_powers_list = []

# pd measuremesnts
pd_data_list = []

for laser_power in np.arange(5, 10):
    # write the laser power
    write_laser_amplitude(laser_power=laser_power)

    # get the pd data
    exec(open('pico_Com.py').read())
    pd_data = np.mean(np.load('channel_A_data', allow_pickle=True))

    # append the values
    laser_powers_list.append(laser_power)
    pd_data_list.append(pd_data)

    # plot the transimtted power vs laser power
    plt.figure(figsize=(12, 8))
    plt.plot(laser_powers_list, pd_data_list)
    plt.xlabel('Input Laser Power (mW)')
    plt.ylabel('Transmitted Power (mV)')
    plt.title('Transmitted Power vs Input Power')
    plt.ylim([0, 100])
    plt.show()

    time.sleep(1)


