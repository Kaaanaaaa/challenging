#3
import re
text = 'The ghost that says boo haunts the loo'
match = re.findall('.oo', text)
print(match)