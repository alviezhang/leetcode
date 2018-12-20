# coding: utf-8

class Solution:
    def numUniqueEmails(self, emails):
        """
        :type emails: List[str]
        :rtype: int
        """
        email_map = {}
        for email in emails:
            name, domain = email.split('@')
            name = name.replace('.', '')

            pos = name.find('+')
            if pos >= 0:
                name = name[:pos]

            new_email = '{}@{}'.format(name, domain)

            if new_email in email_map:
                email_map[new_email] += 1
            else:
                email_map[new_email] = 1

        return len(email_map.keys())
