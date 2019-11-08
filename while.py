# string = 'wowhatamanwowowpalehche'
# substring = 'wow'
# print(string.count(substring))

def count(string,substring):
   result = 0
   i = 0
   while i > -1:
       try:
           i = string.index(substring, i) + len(substring)
           result += 1
           i -= 1
       except:
           i = -1

   return result


string = "wowhatamanwowowpalehche"
substring = "wow"
print (count(string,substring))








