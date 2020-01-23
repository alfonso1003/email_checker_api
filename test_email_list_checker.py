import unittest

from email_list_checker import EmailListChecker

class EmailListCheckerTest(unittest.TestCase):
    
    def test_valid_domain_list(self):
        elc = EmailListChecker(['test.email@gmail.com', 'test.email+spam@gmail.com', 'testemail@gmail.com'])
        self.assertTrue(elc.valid_email_list)

    def test_invalid_domain(self):
        elc = EmailListChecker(['test.email@gmail'])
        self.assertFalse(elc.valid_email_list)

    def test_stripped_list_one(self):
        elc = EmailListChecker(['test.email@gmail.com'])
        self.assertEqual(elc.stripped_email_list, ['testemail@gmail.com'])

    def test_stripped_list_two(self):
        elc = EmailListChecker(['test.email+spam@gmail.com'])
        self.assertEqual(elc.stripped_email_list, ['testemail@gmail.com'])

    def test_stripped_list_three(self):
        elc = EmailListChecker(['testemail@gmail.com'])
        self.assertEqual(elc.stripped_email_list, ['testemail@gmail.com'])

    def test_unique_email_count_one(self):
        elc = EmailListChecker(['test.email@gmail.com', 'test.email+spam@gmail.com', 'testemail@gmail.com', 'alfonso@gmail.com'])
        self.assertEqual(elc.unique_email_count, 2)

    def test_unique_email_count_two(self):
        elc = EmailListChecker(['test.email@gmail.com', 'test.email+spam@gmail.com', 'testemail@gmail.com', 'test@fetch.com', 'alfonso@gmail.com'])
        self.assertEqual(elc.unique_email_count, 3)


if __name__ == '__main__':
    unittest.main()