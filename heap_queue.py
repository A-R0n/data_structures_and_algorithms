## heap queue algorithm also known as a priority queue
import heapq
import numpy as np
from time import perf_counter

WIDTH_AND_HEIGHT_CHESSBOARD = 1000
N = 1000000

def timer(func): 
    def wrapper_function(*args, **kwargs):
        start = perf_counter() 
        func(*args,  **kwargs) 
        end = perf_counter()
        total_time = end - start
        print(f'{total_time} seconds to execute!') 
    return wrapper_function 

def get_random_spots_on_board():
    return np.random.randint(WIDTH_AND_HEIGHT_CHESSBOARD, size=N)

@timer
def heapsort(unsorted_list):
    ## python docs state this is not a stable implementation
    heap_sorted = []
    for value in unsorted_list:
        heapq.heappush(heap_sorted, value)
    ## pop returns the smallest item
    return [heapq.heappop(heap_sorted) for i in range(len(heap_sorted))]

@timer
def listsort(unsorted_list):
    return sorted(unsorted_list)

if __name__ == '__main__':
    unsorted_list = get_random_spots_on_board()
    list_sorted = listsort(unsorted_list)
    heap_sorted = heapsort(unsorted_list)