import unittest
from password_validator import is_password_secure


class test_checker(unittest.TestCase):
    
    def setUp(self):
        pass
        
    def test_false_case(self):
        self.assertEqual(is_password_secure(str(1234)),False)
        self.assertEqual(is_password_secure(str(1234567890987)),False)
        self.assertEqual(is_password_secure("1234567890tgdfsyttr7"),False)
        self.assertEqual(is_password_secure("123456 ERY90tgdfsyttr7"),False)


    def test_true_case(self):
        self.assertEqual(is_password_secure("KKFGkgjg349596@#$"),True)
        self.assertEqual(is_password_secure("1234AS!d"),True)
