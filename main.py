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
    FIFO with fixed frames (matches the table/figure style).
    Replaces the oldest page by using a rotating pointer.
    1. If the page is not in the cache, add it to the cache.
    2. If the cache is full, remove the oldest page (the first one added)
         and add the new page.
    3. Print the state of the cache after each page request.
    4. If the page is already in the cache, do nothing.
    5. it will count the faults and hits.
    6. Repeat for all pages in the input list.

    Args:
        pages (list[int]): A list of page requests.
    Returns:
        tuple[int, int]
    '''
    cache = ['_'] * CACHE_SIZE               
    next_replace = 0                        
    fault_count = 0
    hit_count = 0

    for page in pages:                       
        if page in cache:                    
            hit_count += 1
        else:                               
            fault_count += 1
            cache[next_replace] = page              
            next_replace = (next_replace + 1) % CACHE_SIZE     

        sleep(0.5)                                          
        print(f'Cache state: {cache}')

    print(f'Total page faults: {fault_count}')
    print(f'Total page hits: {hit_count}')
    return fault_count, hit_count


def lru(pages: list[int]) -> tuple[int, int]:
    '''
    This function simulates the LRU page replacement algorithm.
    LRU here is shown like the figure: top is least-recently-used,
    bottom is most-recently-used (so hits will "move" pages down).
    1. If the page is not in the cache, add it to the cache.
    2. If the cache is full, remove the least recently used page
       and add the new page.
    3. Print the state of the cache after each page request.
    4. If the page is already in the cache, move it to the most recently used position.
    5. it will count the faults and hits.   
    6. Repeat for all pages in the input list.

    Args:
        pages (list[int]): A list of page requests.
    Returns:
        tuple[int, int]
    '''
    cache = []                              
    fault_count = 0
    hit_count = 0

    for page in pages:                      
        if page not in cache:               
            fault_count += 1                 

            if len(cache) < CACHE_SIZE:      
                cache.append(page)           
            else:                            
                cache.pop(0)                
                cache.append(page)           

        else:                                
            hit_count += 1                   
            cache.remove(page)               
            cache.append(page)               

        display_cache = cache.copy()
        while len(display_cache) < CACHE_SIZE:
            display_cache.append('-')

        sleep(0.5)                           
        print(f'Cache state: {display_cache}')

    print(f'Total page faults: {fault_count}')
    print(f'Total page hits: {hit_count}')
    return fault_count, hit_count


def lfu(pages: list[int], cache_size: int = 5) -> tuple[int, int]:
    '''
    This function simulates the LFU page replacement algorithm.
    1. If the page is not in the cache, add it to the cache.
    2. If the cache is full, remove the least frequently used page
       and add the new page.
    3. Print the state of the cache after each page request.
    4. If the page is already in the cache, increase its frequency count.
    5. it will count the faults and hits.
    6. Repeat for all pages in the input list.

    Args:
        pages (list[int]): A list of page requests.
        cache_size (int): The size of the cache memory.
    Returns:
        tuple[int, int]
    '''

    cache = ['-'] * cache_size
    frequency = {}
    faults = 0
    hits = 0

    for page in pages:
        if page in cache:
            hits += 1
            frequency[page] += 1
        else:
            faults += 1

            if '-' in cache:
                idx = cache.index('-')
                cache[idx] = page
                frequency[page] = 1
            else:
                min_freq = frequency[cache[0]]
                victim_index = 0

                for i in range(1, cache_size):
                    if frequency[cache[i]] < min_freq:
                        min_freq = frequency[cache[i]]
                        victim_index = i

                removed_page = cache[victim_index]
                cache[victim_index] = page

                frequency.pop(removed_page, None)
                frequency[page] = 1

        print(f"Cache state: {cache}")
        sleep(0.5)
              
    print("Total page faults:", faults)
    print("Total page hits:", hits)
    print("Page frequencies:", frequency)
    return faults, hits


if __name__ == '__main__':
    running = True
    while running:
        user_requested_page = input('Enter which page replacement algorithm to simulate (FIFO, LRU, LFU) or 0 to exit: ').strip().upper()
        if user_requested_page == 'FIFO':
            print('FIFO Page Replacement Algorithm Simulation:')
            print('Pages to be requested:', PAGES)
            fifo(PAGES)
        elif user_requested_page == 'LRU':
            print('LRU Page Replacement Algorithm Simulation:')
            print('Pages to be requested:', PAGES)
            lru(PAGES)
        elif user_requested_page == 'LFU':
            print('LFU Page Replacement Algorithm Simulation:')
            print('Pages to be requested:', PAGES)
            lfu(PAGES)
        elif user_requested_page != '0':
            print('Invalid input. Please enter FIFO, LRU, or LFU.')
        if user_requested_page == '0':
            running = False