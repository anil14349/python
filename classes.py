class myClass():
    def method1(self):
        print("myclass method1")

    def method2(self, str):
        print("my class method 2 " + str)


class anotherClass(myClass):
    def method1(self):
        myClass.method1(self)
        print("anotherClass method1")

    def method2(self, str):
        print("anotherClass method 2 " + str)


def main():
    c = myClass()
    c.method1()
    c.method2("anil")

    c2 = anotherClass()
    c2.method1()
    c2.method2("kumar")


if __name__ == "__main__":
    main()
