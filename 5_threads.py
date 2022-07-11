import threading
import time


t_lock = threading.Lock()


def timer(name, delay, repeat):
    print("Timer: {} started!".format(name))
    t_lock.acquire()
    print("Thread {} acquired the lock!".format(name))
    while repeat > 0:
        time.sleep(delay)
        actual_time = str(time.ctime(time.time()))
        print("{}: {}".format(name, actual_time))
        repeat -= 1
    print("Thread {} releasing the lock!".format(name))
    t_lock.release()
    print("Timer: {} completed!".format(name))


def main():
    t1 = threading.Thread(target=timer, args=("Timer1", 1, 5))
    t2 = threading.Thread(target=timer, args=("Timer2", 2, 3))
    t1.start()
    t2.start()
    print("Function 'main' completed!")


if __name__ == '__main__':
    main()