def main():
    pass

def system_display(n):
    if n < 0: return "invalid"
    if n >= 0 and n <= 15: return "grey bar"
    if n >= 16 and n <= 50: return "green bar"
    if n >= 51 and n <= 85: return "yellow bar"
    if n >= 86 and n <= 100: return "red bar"
    if n > 100: return "invalid"


if __name__ == "__main__":
    main()