
def calculate_simple_interest(p, r, t):
    return (p * r * t) / 100


def main():
    p = float(input("Enter principal amount: "))
    r = float(input("Enter rate of interest: "))
    t = float(input("Enter time in years: "))

    interest = calculate_simple_interest(p, r, t)
    print("Simple Interest =", interest)


if __name__ == "__main__":
    main()
