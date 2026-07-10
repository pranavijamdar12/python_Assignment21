import threading

counter = 0
lock = threading.Lock()

def Increment():
    global counter

    for i in range(100000):
        lock.acquire()
        counter = counter + 1
        lock.release()

def main():
    t1 = threading.Thread(target=Increment)
    t2 = threading.Thread(target=Increment)

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print("Final Counter:", counter)

if __name__ == "__main__":
    main()
