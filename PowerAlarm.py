__author__ = 'WingGao'
import power # https://github.com/Kentzo/Power
import time, sys

def get_power_name(t):
    return {
        0: 'POWER_TYPE_AC',
        1: 'POWER_TYPE_BATTERY',
        2: 'POWER_TYPE_UPS'
    }[t]

if __name__ == '__main__':
    while True:
        type = power.PowerManagement().get_providing_power_source_type()
        if type == power.POWER_TYPE_BATTERY:
            print '\n', time.strftime('[%m-%d %H:%M:%S]'), get_power_name(type), 'EXIT'
            break
        else:
            print '\r', time.strftime('[%m-%d %H:%M:%S]'), 'Power ok',
            time.sleep(30)

    input()
    input()