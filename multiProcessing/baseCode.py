# -*- coding: utf-8 -*-
# Indentation: Visual Studio

'''
ddsd
'''

__version__ = 1.0
__author__ = "Sourav Raj"
__author_email__ = "souravraj.iitbbs@gmail.com"

import time
import multiProcessing as mp

def wait_for_second():
    print('wait for 1 sec.')
    time.sleep(1)
    print('wait time is finished.')

start_=time.perf_counter()
wait_for_second()
wait_for_second()
end_=time.perf_counter()
print(f'it took {round(end_-start_, 2)} sec')
