# TDD approach(we define the behaviour we want) so we write tests before we def the functions themselves in the test module 
# note: python3 file_name.py -v #gives result of each test and associated description
import unittest
from activities import eat, nap, is_funny, laugh

class AvtivityTests(unittest.TestCase):
    #counts one function as one test
    def test_eat_healthy(self):
        #assertions
        """It should indicate youare eating healthy!""" #description
        self.assertEqual(
            eat("broccoli",is_healthy=True),        #if both parameters match(True)...
            "I'm eating broccoli, because my body is a temple"  #return thisclear
            )
    
    def test_eat_unhealthy(self):
        """It should indicate youare eating unhealthy!"""
        self.assertEqual(
            eat("pizza",is_healthy=False),        #if both parameters match(True)...
            "I'm eating pizza, because YOLO!"  #return this
            )
        
    #testing for errors
    def test_eat_healthy_boolean(self):
        """is_healthy must be a bool"""
        with self.assertRaises(ValueError): #raises error and we can choose type of error
            eat("pizza", is_healthy="who cares?")
    
    def test_short_nap(self):
        """long nps should be refreshing!"""
        self.assertEqual(
            nap(1),
            "I'm feeling refreshed after my 1 hour nap"
        )
        
    def test_long_nap(self):
        """long naps should be discouraging"""
        self.assertEqual(
            nap(3),
            "Ugh I overslept. I didn't measn to nap for 3 hours!"
        )
        
    def test_is_funny_tim(self):
        self.assertEqual(is_funny("tim"), False) #same as below
        # self.assertFalse(is_funny("tim"), "tim should not be funny") #checks if this is Falsy not False

    def test_is_funny_anyone_test(self):
        """anyone else but tim should be funny"""
        self.assertTrue(is_funny("blue"), "blue should be funny")
        self.assertTrue(is_funny("tammy"), "tammy should be funny")
        self.assertTrue(is_funny("sven"), "sven should be funny")
        
    def test_laugh(self):
        self.assertIn(laugh(), ('lol','haha','tehehe'))  #checks if value in collection/range
        
    
if __name__ == "__main__":
    unittest.main() #runs or executes our tests