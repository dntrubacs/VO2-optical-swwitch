import numpy as np
from matplotlib import pyplot as plt
from utils import load_transmitted_power, linear
from scipy.optimize import curve_fit

# a list of all the processed data
input_laser_power_list = []
transmitted_laser_power_list = []


for i in [4, 5, 6, 7, 8, 9]:
    # load the values
    input_laser_power, transmitted_laser_power = load_transmitted_power(
        file_path=f'gold_nano_antenas_on_vo2_sample_{i}'
    )

    # append the values
    input_laser_power_list.append(input_laser_power)
    transmitted_laser_power_list.append(transmitted_laser_power)


# used for plotting only
# transmitted power
min_transmitted_power = 0.005
max_transmitted_power = 0.036

# input laser power
min_input_power = 5
max_input_power = 36.8


# plot the data
# show all the data in the same graph
plt.figure(figsize=(12, 8))
for i in range(len(input_laser_power_list)):
    plt.plot(input_laser_power_list[i], transmitted_laser_power_list[i],
             label=f'sample {i+1}', lw=0.7
             )

# put limits on the data
plt.xlim([min_input_power, max_input_power])
plt.ylim([min_transmitted_power, max_transmitted_power])


# labels
plt.xlabel('Input Laser Power (mW)')
plt.ylabel('Transmitted Power (V)')
plt.title('Transmitted Power vs Input Power')
plt.legend()
plt.show()


