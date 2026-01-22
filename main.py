'''
This is the main module.
This module is to simulete multiple page replacement algorithms.
FIFO or first in first out,
LRU or least recently used,
and LFU or least frequently used.

Cache memory is simulated by a list.
The size of the cache memory is defined in the variable 'cache_size'.
It will be 5.

input: 8, 2, 6, 4, 7, 8, 9, 2, 0, 1, 6, 4, 0, 8, 5

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
    cache = ['_'] * CACHE_SIZE                # too lazy to add comments, fifo is simple lol
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

    for page in pages:         # iterate through each page request              
        if page not in cache:          # if the page is not in the cache      
            fault_count += 1       # increment fault count           

            if len(cache) < CACHE_SIZE:       # if there is space in the cache
                cache.append(page)           # add the new page
            else:                            
                cache.pop(0)            # else remove the least recently used page 
                cache.append(page)     # add the new page         

        else:                                
            hit_count += 1          # increment hit count            
            cache.remove(page)        # remove the page from its current position       
            cache.append(page)             # add it to the most recently used position  

        display_cache = cache.copy() # create a copy of the current cache state
        while len(display_cache) < CACHE_SIZE: # fill the rest with '-' for displaying it in a nice way
            display_cache.append('-') # add '-' to the end of the display cache

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
    
    Note: in case of a tie in frequency, FIFO is used to break the tie.

    Args:
        pages (list[int]): A list of page requests.
        cache_size (int): The size of the cache memory.
    Returns:
        tuple[int, int]
    '''


    cache = ['-'] * cache_size
    frequency = {} 
    loaded_time = {}    # for tie-breaking with FIFO
    time = 0             

    faults = 0
    hits = 0

    for page in pages:# iterate through each page request
        time += 1         # increment time for each page request

        if page in cache: # if the page is already in the cache
            hits += 1        # increment hits
            frequency[page] += 1  # increase its frequency count
        else:
            faults += 1      # increment faults

            if '-' in cache: # if there is space in cache
                idx = cache.index('-') # find the first empty slot
                cache[idx] = page # add the new page
                frequency[page] = 1 # initialize its frequency to 1 since it's newly added
                loaded_time[page] = time      # record the time it was loaded for tie-breaking
            else:
                
                min_freq = frequency[cache[0]]  # find the minimum frequency in the cache
                for i in range(1, cache_size): # iterate through the cache
                    if frequency[cache[i]] < min_freq: # if found a page with lower frequency
                        min_freq = frequency[cache[i]] # update the minimum frequency

                
                index_of_out_page = 0 # index of the page to be removed is initialized to 0
                for i in range(1, cache_size): # look for the least frequently used page
                    if frequency[cache[i]] < frequency[cache[index_of_out_page]]: # if found a page with lower frequency
                        index_of_out_page = i # update the index
                    elif frequency[cache[i]] == frequency[cache[index_of_out_page]]: # if tie in frequency
                        
                        if loaded_time[cache[i]] < loaded_time[cache[index_of_out_page]]: # if page i was loaded earlier
                            index_of_out_page = i # update the index

                removed_page = cache[index_of_out_page] # page to be removed from cache

                
                frequency.pop(removed_page, None) # just pop it from frequency dict
                loaded_time.pop(removed_page, None) # just pop it from loaded_time dict

                
                cache[index_of_out_page] = page # add the new page
                frequency[page] = 1 # initialize its frequency to 1 since it's newly added
                loaded_time[page] = time     # record the time it was loaded for tie-breaking

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