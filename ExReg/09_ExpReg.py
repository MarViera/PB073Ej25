import re

men_regex = re.compile (r"Bat(ha)+man") 
mo = men_regex.search("Batman")   
print (mo)
mo = men_regex.search ("Bathahahaman")
print (mo)
print (mo.group())
print (mo.group(1))
