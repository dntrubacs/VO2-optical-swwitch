import numpy as np
from matplotlib import pyplot as plt
from utils import load_transmitted_power

# a list of all the processed data
input_laser_power_list = []
transmitted_laser_power_list = []

for i in [3, 4, 5, 6, 7]:
    # load the values
    input_laser_power, transmitted_laser_power = load_transmitted_power(
        file_path=f'pure_vo2_sample_{i}'
    )

    # append the values
    input_laser_power_list.append(input_laser_power)
    transmitted_laser_power_list.append(transmitted_laser_power)


# used for plotting only
# transmitted power
min_transmitted_power = 0.003
max_transmitted_power = 0.035

# the highlighted switching region
switching_region = np.arange(
    start=min_transmitted_power, stop=2*max_transmitted_power, step=0.01
)
switching_region_start = 15.5
switching_region_stop = 17

# input laser power
min_input_power = 5
max_input_power = 36.8

# plot the data
# show all the data in the same graph
plt.figure(figsize=(12, 8))
for i in range(len(input_laser_power_list)):
    plt.plot(input_laser_power_list[i], transmitted_laser_power_list[i],
             label=f'sample {i}')

# put limits on the data
plt.xlim([min_input_power, max_input_power])
plt.ylim([min_transmitted_power, max_transmitted_power])

# highlight the switching region
plt.fill_betweenx(
    switching_region, switching_region_start, switching_region_stop,
    color='red', alpha=0.3,
    label=f'switching region: {switching_region_start} - '
          f'{switching_region_stop} mW'
)

# labels
plt.xlabel('Input Laser Power (mW)')
plt.ylabel('Transmitted Power (V)')
plt.title('Transmitted Power vs Input Power')
plt.legend()
plt.show()


'''
# highlight the switching region
min_transmitted_power = min(transmitted_laser_power_list[2])
max_transmitted_power = max(transmitted_laser_power_list[2])
min_input_power = min(input_laser_power_list[2])
max_input_power = max(input_laser_power_list[2])

plt.figure(figsize=(12, 8))
plt.plot(input_laser_power_list[2], transmitted_laser_power_list[2])
plt.xlabel('Input Laser Power (mW)')
plt.ylabel('Transmitted Power (V)')
plt.title('Transmitted Power vs Input Power')
plt.fill_betweenx(
    y, 16.2, 17, color='red', alpha=0.5, label='switching region'
)
plt.ylim([min_transmitted_power, max_transmitted_power])
plt.xlim([min_input_power, max_input_power])
plt.legend()
plt.show()
'''