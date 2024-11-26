from threading import Thread
from queue import Queue
import time
import random

class Table(): #Table(1)
    def __init__(self, number, guest):
        self.number = number
        self.guest = None

class Guest(Thread): #Guest('Vasya')
    def __init__(self, name):
        threading.Thread.__init__(self)
        self.name = name

    def run(self):
        time.sleep(random.randint(3,10))

class Cafe(Table): #Cafe(Table(1), Table(2),....)
    list_g = []
    def __init__(self, *tables):
        self.queue = Queue()
        self.tables = list(tables)

    def

    def guest_arrival(self, *guests):
        g = list(guests)
        t = self.tables
        quantity_g = len(g)
        free_tables = min(quantity_g, len(t))
        for k in range(free_tables):
            t[k].guest = guests[k]
            thread1 = guests[k]
            thread1.start()
            Cafe.list_g.append(thread1)
            print(f'{g[k].name} сел(-а) за стол номер {t[k].number}')
        if quantity_g > free_tables:
            for k in range(free_tables, quantity_g):
                self.queue.put(guests[k])
                print(f'{g[k].name} в очереди')

    def discuss_guests(self):







