class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        countall = defaultdict(int)
        for temp in cpdomains:
            count,domain = temp.split()
            count= int(count)
            subdomain = domain.split('.')
            for i in range(len(subdomain)):
                tempp = '.'.join(subdomain[i:])
                countall[tempp]+=count
        ans = []
        for domain, count in countall.items():
            ans.append(str(count) + " " + domain )
        return ans