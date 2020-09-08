regex_pattern = r'^((?!IIII|VVVV|XXXX|LLLL|LL|CCCC|DDDD|MMMM).)*$'

import re
print(str(bool(re.match(regex_pattern, input()))))
