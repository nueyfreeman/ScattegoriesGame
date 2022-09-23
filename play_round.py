import players as user
import random


def add_some(obj):
    obj.add_pt(random.randint(0, 5))


def main():
    ps = []
    for i in range(3):
        ps.append(user.Player(i))
        ps[i].add_pt(2)
        #add_some(ps[i])
        ps[i].add_win()
    ps[0].add_pt(3)
    ps[2].add_win()
    user.Player.wins = 3
    print(f'{ps[0]}, {ps[2]}, {ps[1]}')


if __name__ == '__main__':
    main()
