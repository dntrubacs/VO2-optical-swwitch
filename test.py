import os
import numpy as np
from matplotlib import pyplot as plt


os.chdir('C:/Users/dit1u20/PycharmProjects/N7714A/gold_nano_antenas_on_vo2_sample_3')
for laser_power in np.arange(5, 37, 0.3):
    print(laser_power)

input_laser_power = np.load('input_laser_power', allow_pickle=True)
transmitted_laser_power = np.load('transmitted_laser_power', allow_pickle=True)
background_noise = np.load('background_noise', allow_pickle=True)
print(len(background_noise), np.mean(background_noise))


plt.plot(input_laser_power, transmitted_laser_power)
plt.show()
