# -*- coding: utf-8 -*-
# Indentation: Visual Studio

'''
ddsd
'''

__version__ = 1.0
__author__ = "Sourav Raj"
__author_email__ = "souravraj.iitbbs@gmail.com"

import time
import multiprocessing as mp

def wait_for_second():
    print('wait for 1 sec.')
    time.sleep(1)
    print('wait time is finished.')


if __name__=="__main__":
    start_=time.perf_counter()
    processes=[]

    for _ in range(2):
        p=mp.Process(target=wait_for_second)
        p.start()
        processes.append(p)
    for process in processes:
        process.join()

    end_=time.perf_counter()
    print(f'it took {round(end_-start_, 2)} sec')
