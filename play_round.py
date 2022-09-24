import players as user
import random


def add_some(obj):
    obj.add_pt(random.randint(0, 5))


def show_with_id(variable):
    print(variable)
    print(hex(id(variable)))


def main():
    x = 10
    show_with_id(x)
    y = 10
    show_with_id(y)
    y += 2
    show_with_id(y)
    x = 5
    show_with_id(x)
    x = [3, 4, 6]
    show_with_id(x)
    x.append(8)
    show_with_id(x)
    x = [3, 4, 5]
    show_with_id(x)
    list_test()


def list_test():
    ps = []
    abc = 'abc'
    for i in range(3):
        ps.append(user.Player(i))
        var = {abc[i]: i}
        ps[i].add_pt(2)
        add_some(ps[i])
        ps[i].add_win()
        # ps[i].answers.clear()
        ps[i].answers.update(var)
    ps[1].wins = 3
    print(f'{ps[0]}, {ps[2]}, {ps[1]}')
    for i in range(3):
        show_with_id(ps[i].answers)


if __name__ == '__main__':
    main()
