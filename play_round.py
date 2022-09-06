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
#    playerz = []
 #   for p in range(3):
  #      playerz.append(user.Player(input('Say something: '), {}, p))
   #     while True:
    #        feed = int(input('Give a number: '))
     #       if feed < 10:
      #          playerz[p].add_pt()
       #     elif feed == 10:


if __name__ == '__main__':
    main()