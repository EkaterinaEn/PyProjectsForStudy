class Flat:
    ladder  = True

    def __init__(self, rooms):
        self.rooms = rooms

    def add_room(self, room):
        self.rooms.append(room)

    def get_rooms(self):
        return self.rooms


if __name__ == "__main__" :

    print(f'Flat {Flat.__dict__}')
    print(f'==========================')
    newRoomsGKArt = ['entranceHall', 'toilet', 'bathroom']
    flatGKArt = Flat(newRoomsGKArt)
    print(f'GKArt {flatGKArt.rooms}     ladder = {flatGKArt.ladder}')
    flatGKArt.add_room('bedroom')
    flatGKArt.add_room('kitchen')
    flatGKArt.ladder = False
    print(f'GKArt {flatGKArt.get_rooms()}       ladder = {flatGKArt.ladder}     ladder = {flatGKArt.__class__.ladder}')
    print(f'==========================')
    newRoomsGKSputnik = ['entranceHall', 'toilet', 'bathroom']
    flatGKSputnik = Flat(newRoomsGKSputnik)
    print(f'GKSputnik {flatGKSputnik.get_rooms()}     ladder = {flatGKSputnik.ladder}')
    flatGKSputnik.add_room('bedroom')
    print(f'GKSputnik {flatGKSputnik.get_rooms()}     ladder = {flatGKSputnik.ladder}')
    print(f'==========================')

    print(Flat.__mro__)

