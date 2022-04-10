

import time


def counter(count):
    while True:
        print(f'Please wait {count}s ', end='\r')
        time.sleep(1)
        count -= 1
        if count == 0:
            print('\nDone😎')
            break


counter(20)