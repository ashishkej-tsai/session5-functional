
from time import perf_counter
import sys
import math

def squared_power_list(num,*,start,end):
    if start < 0 or end < 0 or end < start:
        raise ValueError(f'start:{start} and end:{end} should be greater than zero and end should be greater than start')
    return [num**x for x in range(int(start),int(end)+1)]

def polygon_area(side_length,*,sides):
    if sides < 3 or sides > 6:
        raise ValueError(f'sides:{sides}  can be between [3,6]')
    return ((side_length**2) * sides)/(4*math.tan(math.pi/sides))

def temp_converter(temp,*,temp_given_in):
    if temp_given_in not in ['f', 'c']:
        raise ValueError(f'temp_given_in:{temp_given_in}  can be f or c')
    if temp_given_in == 'f':
        return (temp - 32) * 5/9
    elif temp_given_in == 'c':
        return (temp * 9/5) + 32

def speed_converter(speed,*,dist, time):
    #dist can be km/m/ft/yrd, time can be ms/s/min/hr/day
    if speed < 0:
        raise ValueError(f'speed:{speed}  can be greater than 0')
    if dist not in ['km', 'm', 'ft', 'yrd']:
        raise ValueError(f'dist:{dist}  can be km/m/ft/yrd')
    if time not in ['ms','s', 'min', 'hr', 'day']:
        raise ValueError(f'time:{time}  can be ms/s/min/hr/day')
    if dist == 'km':
        distance = 1.0
    elif dist == 'm':
        distance = 1000.0
    elif dist == 'ft':
        distance = 3280.84
    elif dist == 'yrd':
        distance = 1093.61

    if time == 'ms':
        time_conv = 60.0*60.0*1000.0
    elif time == 's':
        time_conv = 60.0*60.0
    elif time == 'min':
        time_conv = 60.0
    elif time == 'hr':
        time_conv = 1.0
    elif time == 'day':
        time_conv = 1.0/24.0

    return (speed * distance)/time_conv

def time_it(fn, *args, repetitions=1, **kwargs):
    if repetitions < 1:
        raise ValueError(f'repetitions:{repetitions}  can not be less than 1')
    if fn != print:
        if len(args) != 1:
            raise ValueError(f'Function:{fn} other than print can not have other than 1 positional argument')
        else:
            output = fn(*args,**kwargs)
            start_time = perf_counter()
            for _ in range(repetitions):
                fn(*args,**kwargs)
            tot_time = perf_counter() - start_time
            avg_time = tot_time/repetitions
    else:
        output = fn(*args,**kwargs)
        start_time = perf_counter()
        for _ in range(repetitions):
            fn(*args,**kwargs)
        tot_time = perf_counter() - start_time
        avg_time = tot_time/repetitions

    return output, avg_time

