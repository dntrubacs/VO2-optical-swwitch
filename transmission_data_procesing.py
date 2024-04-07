import os
from agilent_connections import write_laser_amplitude
import numpy as np
from matplotlib import pyplot as plt
import time as time
import pickle

os.chdir('C:/Users/dit1u20/PycharmProjects/N7714A')

def get_pd_data() -> float:
    exec(open('pico_Com.py').read())
    pd_data = np.mean(np.load('channel_A_data', allow_pickle=True))
    return pd_data


# laser powers used
laser_powers_list = []

# pd measuremesnts
pd_data_list = []

for laser_power in np.arange(5, 37, 0.3):
    # write the laser power
    write_laser_amplitude(laser_power=laser_power)

    # get the pd data
    exec(open('pico_Com.py').read())
    pd_data = np.mean(np.load('channel_A_data', allow_pickle=True))

    # transform to V
    pd_data = pd_data/1000

    # append the values
    laser_powers_list.append(laser_power)
    pd_data_list.append(pd_data)

    # plot the transimtted power vs laser power
    plt.figure(figsize=(12, 8))
    plt.plot(laser_powers_list, pd_data_list)
    plt.xlabel('Input Laser Power (mW)')
    plt.ylabel('Transmitted Power (V)')
    plt.title('Transmitted Power vs Input Power')
    plt.show()

    time.sleep(15)

    # save the data with pickle
    # Display status returns
    with open('gold_nano_antenas_on_vo2_sample_4/input_laser_power', 'wb') as handle:
        pickle.dump(np.array(laser_powers_list), handle)
    with open('gold_nano_antenas_on_vo2_sample_4/transmitted_laser_power', 'wb') as handle:
        pickle.dump(np.array(pd_data_list), handle)


