import time
from datetime import timedelta


def start_timer():
    return time.perf_counter()


def print_elapsed_time(start_time, *args):
    print("Elapsed time:", timedelta(seconds=time.perf_counter() - start_time), [(i) for i in args])
