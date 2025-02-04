class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        my_dict = defaultdict(int)
        #splitting the number and the domains and splitting the domains by agian
        for item in cpdomains:
            number,domains = item.split()
            number = int(number)
            
            #we are going reverse and find . and each time we are going to append it to our array
            #so we have to create 2 arrays one for adding the word and one for appending it to the main
            word = []
            all_domains = []
            for ch in domains[::-1]:
                if ch == '.':
                    all_domains.append("".join(word[::-1]))
                    word.append(ch)
                else:
                    word.append(ch)
            all_domains.append("".join(word[::-1]))
            print(all_domains)
            #for each domain_name we are going to use a key and incrementing it by value of number
            for each_domain_name in all_domains:
                my_dict[each_domain_name]+=number
        #printing the output in our desired array res
        res = []
        for item,value in my_dict.items():
            res.append(f"{value} {item}")
        return res