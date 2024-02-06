def main():
    nums = [55, 987, 89, -233, 8, 13, -377, 3, 1, -34, 610, 144, 5, 21, 2, 1]

    nums.sort(key=lambda n: abs(n))

    print(nums)

    # list comprehension
    doubled = [2 * n for n in nums]
    print(doubled)

    # (lazy) generator
    doubled2 = (2 * n for n in nums)
    print(type(doubled2))
    print(list(doubled2))


if __name__ == '__main__':
    main()
