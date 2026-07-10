from multiprocessing import Pool
import os

def EvenSum(n):
    total = 0

    for i in range(2, n + 1, 2):
        total += i

    print("Process ID:", os.getpid())
    print("Input:", n)
    print("Sum of Even Numbers:", total)

    return total

def main():
    data = [1000000, 2000000, 3000000, 4000000]

    p = Pool()

    p.map(EvenSum, data)

    p.close()
    p.join()

if __name__ == "__main__":
    main()
