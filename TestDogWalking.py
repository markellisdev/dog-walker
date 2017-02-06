import unittest
from dogwalking import User
from registrar import Registrar

class TestDogWalking(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.bob = User("bobbytables", "Bob", "Roberts", "po@po.com",) #instance of user
        self.jane = User("janejetson", "Jane", "Jetson", "jane@jane.com",) #instance of user
        self.pickles = Dog("pickles", "Jack Russell", ) #instance of dog
        self.scheduler = Scheduler() #person whose responsibility it is to schedule walks
        self.registrar = Registrar()

    def test_user_can_register(self):
        self.assertIsInstance(bob, User)

        self.registrar.register_user(bob) #saves to our persistent storage --added registrar bc let's not make this a global method (code smells)
        self.assertTrue(user_is_registered(bob))

    def test_user_can_register_dog(self):
        self.registrar.register_dog(self.bob, self.pickles)
        # self.bob.register_dog(self.pickles) here we know the dog is registered by user, but we're using registrar above
        self.assertIn(self.pickles, self.bob.get_dogs()) #assert pickles is in bob's dogs

    def test_user_can_set_available_walking_time(self):
        self.scheduler.add_walk_time(self.pickles, "1:00p", "2:30p") #sets start time and end

        available_times = self.pickles.get_walk_times()
        time_was_recorded = False

        for time in available_times:
            if time[1] == "11:00a" and time[2] == "12:00p":
                time_was_recorded = True

    def test_user_can_select_dog_to_walk(self):
        self.registrar.register_user(self.jane) #because jane was not yet registered

        available_times = self.pickles.get_walk_times() #available times is a list
        # [ (1, "11:00a", "12:00p", 1), (2, "4:00p", "6:00p", 1)] This is what will be returned

        self.scheduler.schedule_walk(self.jane, available_times[0][0]) #passing the walker and time - dog info is included in time tuple
        schedules = self.scheduler.get_user_schedule(self.jane)
        # pk, user_id, time_id
        # [ (1, 2, 1)]

        walk_is_scheduled = False
        for time in schedules:
            if time[2] == available_times[0][0]:
                walk_is_scheduled = True
        
        self.assertTrue(walk_is_scheduled)

if __name__ == "__main__":
    unittest.main()