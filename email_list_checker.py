import re
from email_validator import validate_email

class EmailListChecker:
    def __init__(self, email_list):
        self.email_list = email_list
    
    @staticmethod
    def _strip_email(email_address):
        """
        remove extra periods in username
        remove eveything between + and @ symbols, inclusive
        """
        return re.sub("(?:\.|\+.*)(?=.*?@)", "", email_address)
    
    @staticmethod
    def _valid_email(email_address):
        try:
            validate_email(email_address)
        except:
            return False
        return True

    @property
    def valid_email_list(self):
        valid = True
        for email in self.email_list:
            if not self._valid_email(email):
                print(email)
                valid = False
                break
        return valid

    @property
    def stripped_email_list(self):
        """
        returns a list of stripped email addresses
        """
        stripped_emails = [self._strip_email(email) for email in self.email_list]
        return stripped_emails

    @property
    def unique_email_count(self):
        """
        counts unique stripped emails
        """
        return len(set(self.stripped_email_list))


