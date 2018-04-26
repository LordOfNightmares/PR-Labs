import unittest as ut


class Testt(ut.TestCase):
    def setUp(self):
        print("Hello Lab1")

    def test_this_3(self):
        print("TESTED")

    def test_this_2(self):
        print("WOW")

    def tearDown(self):
        print("it cries")

if __name__ == "__main__":
    ut.main()
