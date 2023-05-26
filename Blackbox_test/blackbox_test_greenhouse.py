import unittest
import greenhouse_functions

class blackboxtest1(unittest.TestCase):
    def setUp(self):
        self.adjusttemp = greenhouse_functions.adjust_temperature
        self.currentTemp = 20

    def test_open_window(self):
        targetTemp = 27
        self.assertEqual("closing window", self.adjusttemp(targetTemp, self.currentTemp))
    
    def test_close_window(self):
        targetTemp = 17
        self.assertEqual("opening window", self.adjusttemp(targetTemp, self.currentTemp))

    def test_wrong_input(self):
        targetTemp = "fejl"
        self.assertEqual("TypeError", self.adjusttemp(targetTemp, self.currentTemp))





if __name__ == '__main__':
    unittest.main()