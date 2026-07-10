import threading

def Maximum(data):
    print("Maximum Element:", max(data))

def Minimum(data):
    print("Minimum Element:", min(data))

def main():
    size = int(input("Enter number of elements: "))
    data = []

    print("Enter elements:")
    for i in range(size):
        data.append(int(input()))

    t1 = threading.Thread(target=Maximum, args=(data,))
    t2 = threading.Thread(target=Minimum, args=(data,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

if __name__ == "__main__":
    main()
