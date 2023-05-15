# -*- coding: utf-8 -*-
# Indentation: Visual Studio

'''
ddsd
'''

__version__ = 1.0
__author__ = "Sourav Raj"
__author_email__ = "souravraj.iitbbs@gmail.com"

import time
import concurrent.futures as cf

def wait_for_second(sec):
    print(f'wait for {sec} sec.')
    time.sleep(sec)
    return f'wait time of {sec} is finished.'


if __name__=="__main__":
    start_=time.perf_counter()
    processes=[]

    with cf.ProcessPoolExecutor() as executor:
        seconds=[1,2,3,5,4]
        results=[executor.submit(wait_for_second, sec) for sec in seconds]
        for f in cf.as_completed(results):
            print(f.result())

    end_=time.perf_counter()
    print(f'it took {round(end_-start_, 2)} sec')
