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


class Gardener():
    def __init__(self, name):
        self.name = name

    def harvest(self):
        print(f'{self.name} harvesting')

    def work(self):
        bush = TomatoBush(tom_at_bush)

        for _ in range(tom_at_bush):
            tomato = Tomato(random.randint(1, 3), states)
            bush.tomatoes.append(tomato)

        rounds = 1
        while True:
            print(f'Round {rounds}')
            print('_____________')
            if bush.all_are_ripe():
                self.harvest()
                bush.give_away_all()
                break
            else:
                bush.grow_all()
            rounds += 1
        Gardener.count_rounds = rounds




    @staticmethod
    def knowledge_base():
        print(f'fruits on the plant - {tom_at_bush}')
        print(f'stages for grow - {Gardener.count_rounds}')

states = {1: 'bloom', 2: 'green', 3: 'red-green', 4: "ripe"}
tom_at_bush = 3
gardener = Gardener('Vasia')
gardener.work()

print()
print('knowledge_base:')
gardener.knowledge_base()