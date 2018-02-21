class Enemy:

        def __init__(self, name, hit_points, lives):
            self.name = name
            self.hit_points = hit_points
            self.lives = lives

        def take_damage(self, damage):
            remaining_points = self.hit_points - damage
            if remaining_points>=0:
                self.hit_points = remaining_points
                print("{} took {} points damage and have {} left".format(self.name, damage, self.hit_points))
            else:
                self.lives -= 1

        def __str__(self):
            return "Name: {0.name}, Lives: {0.lives}, Hit points: {0.hit_points}".format(self)


class Troll(Enemy):

    def __init__(self, name):
        super(Troll, self).__init__(name=name, lives=1, hit_points=23)

    def grunt(self):
        print("Me {0.name}, {0.name} stomp you".format(self))


class Vampyre(Enemy):

    def __init__(self, name):
        super(Vampyre, self).__init__(name=name, lives=3, hit_points=12)


mega = Enemy("megasaur", 10, 1)

megatroll = Troll("trollman")
megatroll.take_damage(10)

megavampyre = Vampyre("blood sucker")
megavampyre.take_damage(10)

