import unittest
import inspect

class Runner:
    def __init__(self, name):
        self.name = name
        self.distance = 0

    def run(self):
        self.distance += 10

    def walk(self):
        self.distance += 5

    def __str__(self):
        return self.name

class RunnerTest(unittest.TestCase):
    is_frozen = True

    @unittest.skipIf(is_frozen == False, 'Тесты в этом кейсе заморожены')
    def test_walk(self):
        runner_1 = Runner('name')
        for i in range (10):
         runner_1.walk()
        self.assertEqual(runner_1.distance, 50)

    @unittest.skipIf(is_frozen == False, 'Тесты в этом кейсе заморожены')
    def test_run(self):
        runner_2 = Runner('name')
        for i in range (10):
         runner_2.run()
        self.assertEqual(runner_2.distance, 100)

    @unittest.skipIf(is_frozen == False, 'Тесты в этом кейсе заморожены')
    def test_challenge(self):
        runner_3 = Runner('name')
        runner_4 = Runner('name')
        for i in range (10):
         runner_3.run()
         runner_4.walk()
        self.assertNotEqual(runner_3.distance, runner_4.distance)

class Runner:
    def __init__(self, name, speed=5):
        self.name = name
        self.distance = 0
        self.speed = speed

    def run(self):
        self.distance += self.speed * 2

    def walk(self):
        self.distance += self.speed

    def __str__(self):
        return self.name

    def __eq__(self, other):
        if isinstance(other, str):
            return self.name == other
        elif isinstance(other, Runner):
            return self.name == other.name


class Tournament:
    def __init__(self, distance, *participants):
        self.full_distance = distance
        self.participants = list(participants)

    def start(self):
        finishers = {}
        place = 1
        while self.participants:
            for participant in self.participants:
                participant.run()
                if participant.distance >= self.full_distance:
                    finishers[place] = participant
                    place += 1
                    self.participants.remove(participant)

        return finishers

class TournamentTest(unittest.TestCase):
    is_frozen = True

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.run_1 = Runner('Усэйн',10)
        self.run_2 = Runner('Андрей',9)
        self.run_3 = Runner('Ник',3)

    @classmethod
    def tearDownClass(cls):
        print()
        for result in cls.all_results:
            print()
            print(f'{result}:')
            print({k: str(v) for k, v in cls.all_results[result].items()})

    @unittest.skipIf(is_frozen == True, 'Тесты в этом кейсе заморожены')
    def test_run_1_run_3(self):
        tournament = Tournament(90, self.run_1, self.run_3)
        results = tournament.start()
        self.all_results[inspect.stack()[0][3]] = results
        self.assertTrue('Ник' == results[len(results)].name)

    @unittest.skipIf(is_frozen == True, 'Тесты в этом кейсе заморожены')
    def test_run_2_run_3(self):
        tournament = Tournament(90, self.run_2, self.run_3)
        results = tournament.start()
        self.all_results[inspect.stack()[0][3]] = results
        self.assertTrue('Ник' == results[len(results)].name)

    @unittest.skipIf(is_frozen == True, 'Тесты в этом кейсе заморожены')
    def test_run_1_run_2_run_3(self):
        tournament = Tournament(90, self.run_1, self.run_2, self.run_3)
        results = tournament.start()
        self.all_results[inspect.stack()[0][3]] = results
        self.assertTrue('Ник' == results[len(results)].name)

if __name__ == "__main__":
    unittest.main()