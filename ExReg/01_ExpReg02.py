import re

br_regexp = re.compile(r'Batman|Robin')
mo = br_regexp.search('Batman y Robin')
print('1',mo.group())

mo = br_regexp.search('Robin y Batman')
print('2',mo.group())
input("...")
bat_regex = re.compile (r"Batman|Batimovil|Batarang")  
mo = bat_regex.search("Batman subio a su Batimovil olvidó su Batarang.")  
print ('3',mo.group())  
input("...")
mo = bat_regex.findall("Batman subio a su batimovil olvidó su Batarang. Batman, Batman")
print ('4',mo)
