
import sys


def calculate_simple_interest(p, r, t):
    return (p * r * t) / 100


def main():
    if len(sys.argv) == 4:
        p = float(sys.argv[1])
        r = float(sys.argv[2])
        t = float(sys.argv[3])
    else:
        p = float(input("Enter the principal amount: "))
        r = float(input("Enter the rate of interest: "))
        t = float(input("Enter the time in years: "))

    si = calculate_simple_interest(p, r, t)

    print("Simple Interest =", si)


if __name__ == "__main__":
    main()