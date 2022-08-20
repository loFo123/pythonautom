import unittest

from main import show_time_of_pid

# print(show_time_of_pid("Jul 6 14:01:23 computer.name CRON[29440]: USER (good_user)"))

class MyTest(unittest.TestCase):
    def test_basic(self):
        testcase = "Jul 6 14:01:23 computer.name CRON[29440]: USER (good_user)"
        anser = "Jul 6 14:01:23"
        self.assertEqual(show_time_of_pid(testcase),anser)
    def test_no(self):
        testcase = ""
        anser = None
        self.assertEqual(show_time_of_pid(testcase), anser)
    def test_error(self):
        self.assertRaises(AssertionError,show_time_of_pid,1234)

unittest.main()