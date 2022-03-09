import time
from threading import Thread
from multiprocessing import Process

from fibonacci import fibonacci


def synchronous_regime(n):
    start_time = time.time()

    for i in range(3):
        fibonacci(n)

    end_time = time.time() - start_time
    return end_time


def run_multithreading(elements):
    start_time = time.time()

    for elem in elements:
        elem.start()
    for elem in elements:
        elem.join()

    end_time = time.time() - start_time
    return end_time


def threads_regime(n):
    threads = [Thread(target=fibonacci, args=(n,)) for _ in range(3)]
    return run_multithreading(threads)


def processing_regime(n):
    processes = [Process(target=fibonacci, args=(n,)) for _ in range(3)]
    return run_multithreading(processes)


def main():
    n = 200_000

    synchronous_time = synchronous_regime(n)
    threads_time = threads_regime(n)
    processing_time = processing_regime(n)

    with open("../artifacts/easy_task.txt", "w") as file:
        file.write("Synchronous time: " + synchronous_time.__str__() + "s\n"
                   + "Threads time: " + threads_time.__str__() + "s\n"
                   + "Multiprocessing time: " + processing_time.__str__() + "s\n")


if __name__ == '__main__':
    main()
