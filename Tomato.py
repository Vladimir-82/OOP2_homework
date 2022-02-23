import random


class Tomato():
    def __init__(self, index, states):
        self._index = index
        self._state = states[self._index]

    def is_ripe(self):
        if self._state == 'ripe':
            print('I have already ripe!!!')
            return True

    def grow(self):
        if not self.is_ripe():
            print(f'I am tomato. My stage is {self._state} and I need to grow!')
            self._index += 1
            self._state = states[self._index]


class TomatoBush():
    def __init__(self, count):
        self.count = count
        self.tomatoes = []

    def grow_all(self):
        for el, tomato in enumerate(self.tomatoes):
            print(el+1, end=' ')
            tomato.grow()

    def all_are_ripe(self):
        counter = 0
        for tomato in self.tomatoes:
            if tomato._state == 'ripe':
                counter += 1
            if self.count == counter:
                print('All tomatos have grown!')
                return True

    def give_away_all(self):
        self.tomatoes.clear()
        print('All tomatos have harvested!')



states = {1: 'bloom', 2: 'green', 3: 'red-green', 4: "ripe"}


tom_at_bush = 3
bush = TomatoBush(tom_at_bush)

for _ in range(tom_at_bush):
    tomato = Tomato(random.randint(1, 3), states)
    bush.tomatoes.append(tomato)

round = 1
while True:
    print(f'Round {round}')
    print('_____________')
    if bush.all_are_ripe():
        bush.give_away_all()
        break
    else:
        bush.grow_all()
    round += 1














