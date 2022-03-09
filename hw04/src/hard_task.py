import time
import random
from datetime import datetime
from codecs import encode
from multiprocessing import Queue, Process


def a_process(main_q: Queue, a_q: Queue):
    while True:
        while not main_q.empty():
            time.sleep(5)
            a_q.put(main_q.get().lower())


def b_process(a_q: Queue, b_q: Queue):
    while True:
        while not a_q.empty():
            b_q.put(encode(a_q.get(), "rot_13"))


def main():
    # main -> a -> b -> main
    main_q = Queue()
    a_q = Queue()
    b_q = Queue()

    Process(target=a_process, args=(main_q, a_q), daemon=True).start()
    Process(target=b_process, args=(a_q, b_q), daemon=True).start()

    words = ['book', 'note', 'sun', 'piece', 'world', 'green', 'love']
    while True:
        # generate random word
        main_q.put(random.choice(words))
        out = b_q.get()
        time_now = datetime.now().strftime("time: %H:%M:%S")
        print(f"{time_now} --> {out}")


if __name__ == '__main__':
    main()
