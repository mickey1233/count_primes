import math


def countprimes(n):
    numbers = {}
    if n == 0 or n == 1:
        print(0)
    else:
        for p in range(2, int(math.sqrt(n)) + 1):
            if p not in numbers:
                for multiple in range(p*p, n, p):
                    numbers[multiple] = 1
        print(n - len(numbers) - 2)


def main():
    countprimes(10)
    countprimes(0)
    countprimes(1)
    countprimes(123)


if __name__ == "__main__":
    main()
