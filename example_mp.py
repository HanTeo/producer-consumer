import multiprocessing as mp
from time import sleep
import random


def producer(queue, n):
    for x in range(1, n + 1):
        # produce an item
        print('producing {}/{}'.format(x, n))
        # simulate i/o operation using sleep
        sleep(random.random())
        item = str(x)
        # put the item in the queue
        queue.put(item)

    # indicate the producer is done
    queue.put(None)


def consumer(queue):
    while True:
        # wait for an item from the producer
        item = queue.get()
        if item is None:
            # the producer emits None to indicate that it is done
            break

        # process the item
        print('consuming item {}...'.format(item))
        # simulate i/o operation using sleep
        sleep(random.random())


with mp.Pool(3) as pool:
    data_q = mp.JoinableQueue()
    p = pool.Process(target=consumer, args=(data_q,))
    c = pool.Process(target=producer, args=(data_q,))
    c.start()
    p.start()
    p.join()
    c.join()
