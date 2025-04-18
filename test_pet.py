import unittest
from src.pet import Pet

class TestPet(unittest.TestCase):

    def setUp(self):
        self.pet = Pet(name="Buddy")

    def test_initial_attributes(self):
        self.assertEqual(self.pet.name, "Buddy")
        self.assertEqual(self.pet.hunger, 5)
        self.assertEqual(self.pet.energy, 5)
        self.assertEqual(self.pet.happiness, 5)

    def test_eat(self):
        self.pet.eat()
        self.assertLess(self.pet.hunger, 5)
        self.assertGreaterEqual(self.pet.energy, 5)

    def test_sleep(self):
        self.pet.sleep()
        self.assertGreater(self.pet.energy, 5)
        self.assertEqual(self.pet.hunger, 5)

    def test_play(self):
        self.pet.play()
        self.assertGreater(self.pet.happiness, 5)
        self.assertLess(self.pet.energy, 5)

    def test_get_status(self):
        status = self.pet.get_status()
        self.assertIn("Hunger", status)
        self.assertIn("Energy", status)
        self.assertIn("Happiness", status)

    def test_train(self):
        self.pet.train("roll over")
        self.assertIn("roll over", self.pet.show_tricks())

if __name__ == '__main__':
    unittest.main()