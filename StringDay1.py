import unittest

def translate(email):
    # given email contains only 1 @
    username, domain = email.split('@')
    translatedName = username.split('+')[0]
    translatedName = translatedName.replace('.', '')
    # handles empty string as well
    
    result = '{0}@{1}'.format(translatedName, domain)
    return result

def numUniqueEmails(emails):
    """
    :type emails: List[str]
    :rtype: int
    """
    uniqueEmails = {}
    for email in emails:
        if email not in uniqueEmails and translate(email) not in uniqueEmails:
            uniqueEmails[translate(email)] = True
    return len(uniqueEmails)


class TestCases(unittest.TestCase):

    def test_regular(self):
        emails = ["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]
        self.assertEqual(numUniqueEmails(emails), 2)

    def test_emptyList(self):
        self.assertEqual(numUniqueEmails([]),0)

if __name__ == '__main__':
    unittest.main()




