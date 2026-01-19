'''
This is the main module.
This module is to simulete multiple page replacement algorithms.
FIFO or first in first out,
LRU or least recently used,
and LFU or least frequently used.

Cache memory is simulated by a list.
The size of the cache memory is defined in the variable 'cache_size'.
It will be 5 for now.

Eg. to to how this program works:
input: 8, 2, 6, 4, 7, 8, 9, 2, 0, 1, 6, 4, 0, 8, 5

FIFO output:
Cache state: [8]
Cache state: [8, 2]
Cache state: [8, 2, 6]
Cache state: [8, 2, 6, 4]
Cache state: [8, 2, 6, 4, 7]
Cache state: [2, 6, 4, 7, 8]
Cache state: [6, 4, 7, 8, 9]
ETC.

LRU output:
Cache state: [8]
Cache state: [8, 2]
Cache state: [8, 2, 6]
Cache state: [8, 2, 6, 4]
Cache state: [8, 2, 6, 4, 7]
Cache state: [2, 6, 4, 7, 8]
Cache state: [6, 4, 7, 8, 9]    
ETC.

LFU output:
Cache state: [8]
Cache state: [8, 2]
Cache state: [8, 2, 6]
Cache state: [8, 2, 6, 4]
Cache state: [8, 2, 6, 4, 7]
Cache state: [2, 6, 4, 7, 8]
Cache state: [6, 4, 7, 8, 9]
ETC.

'''
from time import sleep

CACHE_SIZE = 5
PAGES = [8, 2, 6, 4, 7, 8, 9, 2, 0, 1, 6, 4, 0, 8, 5]


def fifo(pages: list[int]) -> tuple[int, int]:
    '''
    This function simulates the FIFO page replacement algorithm.
    1. If the page is not in the cache, add it to the cache.
    2. If the cache is full, remove the oldest page (the first one added)
       and add the new page.
    3. Print the state of the cache after each page request.
    4. If the page is already in the cache, do nothing.
    5. it will count the faults and hits.
    6. Repeat for all pages in the input list.

    this fuction will print the state of the cache after each page request.

    Args:
        pages (list[int]): A list of page requests.
    Returns:
        tuple[int, int]
    '''
    cache = []
    fault_count = 0
    hit_count = 0
    for page in pages: # loop
        if page not in cache: # if not in cache
            fault_count += 1 # count fault
            if len(cache) < CACHE_SIZE: # and cache not full
                cache.append(page) # add page to cache
            else: # else if cache full
                cache.pop(0) # remove oldest page
                cache.append(page) # add new page
        else: # if page in cache
            hit_count += 1 # count hit
        sleep(0.5) # to simulate time delay
        print(f'Cache state: {cache}')
    print(f'Total page faults: {fault_count}')
    print(f'Total page hits: {hit_count}')
    return fault_count, hit_count

def lru(pages: list[int]) -> tuple[int, int]:
    '''
    This function simulates the LRU page replacement algorithm.
    1. If the page is not in the cache, add it to the cache.
    2. If the cache is full, remove the least recently used page
       and add the new page.
    3. Print the state of the cache after each page request.
    4. If the page is already in the cache, move it to the most recently used position.
    5. it will count the faults, and hits.
    6. Repeat for all pages in the input list.

    this fuction will print the state of the cache after each page request.

    Args:
        pages (list[int]): A list of page requests.
    Returns:
        tuple[int, int]
    '''
    cache = []
    fault_count = 0
    hit_count = 0
    for page in pages: # loop
        if page not in cache: # if not in cache
            fault_count += 1 # count fault
            if len(cache) < CACHE_SIZE: # and cache not full
                cache.append(page) # add page to cache
            else: # else if cache full
                cache.pop(0) # remove least recently used page
                cache.append(page) # add new page
        else: # if page in cache
            cache.remove(page) # remove page from current position
            cache.append(page) # move page to most recently used position
            hit_count += 1 # count hit
        sleep(0.5) # to simulate time delay
        print(f'Cache state: {cache}')
    print(f'Total page faults: {fault_count}')
    print(f'Total page hits: {hit_count}')
    return fault_count, hit_count

def lfu(pages: list[int]) -> tuple[int, int, dict[int, int]]:
    '''
    This function simulates the LFU page replacement algorithm.
    1. If the page is not in the cache, add it to the cache.
    2. If the cache is full, remove the least frequently used page
       and add the new page.
    3. Print the state of the cache after each page request.
    4. If the page is already in the cache, increment its hit count.
    5. it will count the faults.
    6. Repeat for all pages in the input list.

    this fuction will print the state of the cache after each page request.

    Args:
        pages (list[int]): A list of page requests.
    Returns:
        tuple[int, int, dict[int, int]]
    '''
    cache = []
    fault_count = 0
    hit_count = 0
    page_frequency = {}
    for page in pages: # loop
        if page not in cache: # if not in cache
            fault_count += 1 # count fault
            if len(cache) < CACHE_SIZE: # and cache not full
                cache.append(page) # add page to cache
            else: # else if cache full
                # find least frequently used page
                lfu_page = min(cache, key=lambda p: page_frequency.get(p, 0))
                cache.remove(lfu_page) # remove least frequently used page
                cache.append(page) # add new page
            page_frequency[page] = 1 # initialize frequency
        else: # if page in cache
            page_frequency[page] += 1 # increment frequency
            hit_count += 1 # count hit
        sleep(0.5) # to simulate time delay
        print(f'Cache state: {cache}')
    print(f'Total page faults: {fault_count}')
    print(f'Total page hits: {hit_count}')
    return fault_count, hit_count, page_frequency

if __name__ == '__main__':
    print('FIFO Page Replacement Algorithm Simulation:')
    fifo(PAGES)
    print('\nLRU Page Replacement Algorithm Simulation:')
    lru(PAGES)
    print('\nLFU Page Replacement Algorithm Simulation:')
    lfu(PAGES)