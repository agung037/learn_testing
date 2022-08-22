def main():
    pass


def interest_rate_of(x):
    if x < 0 : return "invalid"
    if x >= 0 and x <= 100 : return 0.03
    if x >= 101 and x <= 1000: return 0.05
    if x >= 1001 : return 0.07


if __name__ == "__main__":
    main()