import numpy as np


def linear(x, m, n):
    return m*x + n


def load_transmitted_power(file_path: str) -> tuple:
    """

    :param file_path:
    :return:
    """
    # load the data
    input_laser_power = np.load(
        f'{file_path}/input_laser_power', allow_pickle=True
    )
    transmitted_laser_power = np.load(
        f'{file_path}/transmitted_laser_power', allow_pickle=True
    )

    # load the background noise
    background_noise = np.load(
        f'{file_path}/background_noise', allow_pickle=True
    )
    # transform to V
    background_noise = np.array(background_noise)/1000

    # subtract the background noise
    transmitted_laser_power = (
            transmitted_laser_power - np.mean(background_noise))

    # return the processed values
    return input_laser_power, transmitted_laser_power
