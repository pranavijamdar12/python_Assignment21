import threading

def Prime(data):
    print("Prime Numbers:")
    for no in data:
        if no > 1:
            flag = True
            for i in range(2, no):
                if no % i == 0:
                    flag = False
                    break
            if flag:
                print(no)

def NonPrime(data):
    print("Non Prime Numbers:")
    for no in data:
        if no <= 1:
            print(no)
        else:
            flag = False
            for i in range(2, no):
                if no % i == 0:
                    flag = True
                    break
            if flag:
                print(no)

def main():
    size = int(input("Enter number of elements: "))
    data = []

    print("Enter elements:")
    for i in range(size):
        data.append(int(input()))

    t1 = threading.Thread(target=Prime, args=(data,))
    t2 = threading.Thread(target=NonPrime, args=(data,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

if __name__ == "__main__":
    main()
