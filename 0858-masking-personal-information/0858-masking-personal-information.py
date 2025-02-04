class Solution:
    def maskPII(self, s: str) -> str:
        #changing email
        if "@" in s:
        #splitting everything before @ and 
            s = s.lower()
            first_name, domain_name = s.split('@')
        #changing the letter to lower case and getting the first and last ivalue and between 
        #5 asterixs
            first_value = first_name[0]
            last_value = first_name[-1]
            return f"{first_value}*****{last_value}@{domain_name}"
        
        #masking phone number
        else:
            list_numbers = []
            #get the numbers only and put it on the some list_numbers
            for c in s:
                try:
                    number = int(c)
                    list_numbers.append(str(number))
                except:
                    pass
                
            print(list_numbers)
            list_numbers = "".join(list_numbers)
            print(list_numbers)
            four_value = list_numbers[-4:]
            print(four_value)
            #if the length of phone number is 10 it will be ***-***-XXXX
            if len(list_numbers) == 10:
                return f"***-***-{four_value}"
            #if the length of phone number is 11 it will be +*-***-***-XXXX
            elif len(list_numbers) == 11:
                return f"+*-***-***-{four_value}"
            #if the length of phone number is 12 it will be +**-***-***-XXXX
            elif len(list_numbers) == 12:
                return f"+**-***-***-{four_value}"
            #if the length of phone number is 13 it will be +***-***-***-XXXX
            elif len(list_numbers) == 13:
                return f"+***-***-***-{four_value}"
       