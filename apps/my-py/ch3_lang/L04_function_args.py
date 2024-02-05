def main():
    print("say_hello()")
    say_hello()

    print("say_hello(name)")
    say_hello("Zoe")

    print("say_hello(name, times)")
    say_hello("Zoe", 5)

    print("say_hello(name, times, 1, 2, 3, 4)")
    say_hello("Zoe", 5, 1, 2, 3, 4)

    print("say_hello(name, times, 1, 2, 3, 4, val=7, mode=prod)")
    say_hello("Zoe", 5, 1, 2, 3, 4, val=7, mode="prod")


def say_hello(name='friend', times=1, *args, **kwargs):
    print(f"Hello {name} with times={times}, args={args}, kwargs={kwargs}!")
    print()


if __name__ == '__main__':
    main()
