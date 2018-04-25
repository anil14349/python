def main():
    x = 0

    while (x < 5):
        print(x)
        x = x + 1

    for x in range(5, 10):
        # if(x==7): break
        if (x % 2 == 0): continue
        print(x)

    days = ["Mon", "Tue"]
    for d in days:
        print(d)

    for i, d in enumerate(days):
        print(i, d)


if __name__ == "__main__":
    main()
