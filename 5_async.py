import threading
import time


class AsyncWrite(threading.Thread):
    
    
    def __init__(self, text, out):
        threading.Thread.__init__(self)
        self.text = text
        self.out = out

    
    def run(self):
        f = open(self.out, "a")
        f.write(self.text)
        f.write('\n')
        f.close()
        time.sleep(2)
        print("Finished writing to file {}!".format(self.out))


def main():
    message = input("Enter a string to store: ")
    background = AsyncWrite(message, "out.txt")
    background.start()
    print("Thread 'main' going on!")
    for i in range(5):
        print("Iteration {}...".format(i))
    background.join()
    print("Waited until background thread was completed!")


if __name__ == '__main__':
    main()