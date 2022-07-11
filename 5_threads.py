from threading import Thread
import time


def timer(name, delay, repeat):
    print("Timer: {} started!".format(name))
    while repeat > 0:
        time.sleep(delay)
        actual_time = str(time.ctime(time.time()))
        print("{}: {}".format(name, actual_time))
        repeat -= 1
    print("Timer: {} completed!".format(name))


def main():
    t1 = Thread(target=timer, args=("Timer1", 1, 5))
    t2 = Thread(target=timer, args=("Timer2", 2, 3))
    t1.start()
    t2.start()
    print("Function 'main' completed!")


if __name__ == '__main__':
    main()