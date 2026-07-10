import threading

Sum = 0
Product = 1

def Addition(data):
    global Sum

    for i in data:
        Sum = Sum + i

def Multiplication(data):
    global Product

    for i in data:
        Product = Product * i

def main():
    size = int(input("Enter number of elements: "))
    data = []

    print("Enter elements:")
    for i in range(size):
        data.append(int(input()))

    t1 = threading.Thread(target=Addition, args=(data,))
    t2 = threading.Thread(target=Multiplication, args=(data,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print("Sum =", Sum)
    print("Product =", Product)

if __name__ == "__main__":
    main()
