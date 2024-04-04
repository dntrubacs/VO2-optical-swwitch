import pyvisa
rm = pyvisa.ResourceManager()
import time
import numpy as np
import sys



def write_laser_amplitude(laser_power) -> float:
    """

    :param laser_instrument:
    :param laser_power:
    :return: the value in mW
    """
    response_received = False
    while response_received is False:
        try:
            laser_instrument = rm.open_resource('USB0::0x0957::0x3718::MY50701120::INSTR')
            laser_instrument.write(f':SOURce:CHANnel1:POWer:LEVel:IMMediate:AMPLitude {laser_power} MW')
            response = float(laser_instrument.query(':SOURce:CHANnel:POWer:LEVel:IMMediate:AMPLitude?'))
            print(1000*response)
            response_received = True
        except Exception as e:
            print(e)
            time.sleep(1)

    return response * 1000

if __name__ == '__main__':
    # agilent laser

    for power in np.arange(5, 10):
        time_now = time.time()
        response = write_laser_amplitude(laser_power=power)
        print('laser power:', response, ' mW at time: ', time_now)
        time.sleep(1)