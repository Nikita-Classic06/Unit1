import runner
import unittest

class RunnerTest(unittest.TestCase):
    def test_walk(self):
        p = runner.Runner("Anton")
        for i in range(10):
            p.walk()
        self.assertEqual(p.distance, 50)
    def test_run(self):
        q = runner.Runner("Vita")
        for i in range(10):
            q.run()
        self.assertEqual(q.distance, 100)
    def test_challenge(self):
        a1 = runner.Runner("Nikita")
        a2 = runner.Runner("Dima")
        for i in range(10):
            a1.run()
            a2.walk()
        self.assertNotEqual(a1.distance,a2.distance)


if __name__ == "__main__":
    RunnerTest()

