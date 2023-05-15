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

def wait_for_second(sec, min):
    print(f'wait for {sec} {min}sec.')
    time.sleep(sec)
    return f'wait time of {sec} is finished.'


if __name__=="__main__":
    start_=time.perf_counter()
    processes=[]

    with cf.ProcessPoolExecutor() as executor:
        results=[executor.submit(wait_for_second, 1, 5) for _ in range(5)]
        for f in cf.as_completed(results):
            print(f.result())

    end_=time.perf_counter()
    print(f'it took {round(end_-start_, 2)} sec')
