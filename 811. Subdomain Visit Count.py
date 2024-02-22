'''
https://github.com/baseballcoder1/LeetCode

LeetCode 811: Subdomain Visit Count

Difficulty: Medium
'''

class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        info = {}
        for s in cpdomains:
            count, domain = s.split(" ")
            while True:
                if domain not in info:
                    info[domain] = int(count)
                else:
                    info[domain] += int(count)
                i = domain.find(".")
                if i == -1:
                    break
                domain = domain[i+1:]
        return [str(count) + " " + subdomain for subdomain, count in info.items()]
