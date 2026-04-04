class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        
        for index in range(len(emails)):
            # break the emails based on @ as the seperator. 
            email = emails[index]
            local_name, domain_name = email.split('@')
            # print(local_name, domain_name)
            # process the local_name 
            # 1. remove everything after first +
            local_name = local_name.split('+')[0]
            # print(local_name)
            # 2. remove . in the local_name
            local_name = ''.join(local_name.split('.'))
            print(local_name, domain_name)
            emails[index] = local_name+'@'+domain_name
        return len(set(emails))
