def main():
    x, y = 100, 1000
    if (x < y):
        st = "x is less"
    elif (x == y):
        st = "equal"
    else:
        st = "x is greater"
    print(st)

    st = "x is less" if (x < y) else "x is greater"
    print(st)


if __name__ == "__main__":
    main()
