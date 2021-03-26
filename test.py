import re

matches = re.findall(r'((.)\2{3})', 'abbcdeee')
print(matches)