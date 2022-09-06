import players as user


def main():
    p1 = user.Player(int(input('Pick a number: ')))
    p1.pick_name()
    print(p1.print_name())
    print(p1.print_eye_d())
    print(p1.pts())
    for i in range(p1.print_eye_d()):
        p1.add_pt(3)
    print(p1.pts())


if __name__ == '__main__':
    main()