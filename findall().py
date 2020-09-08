import re
v = '[qwrtypsdfghjklzxcvbnm]'
a = re.findall('(?<=' + v +')([aeiou]{2,})' + v, input(), re.I)
print('\n'.join(a or ['-1']))
