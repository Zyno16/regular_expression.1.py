import re
zz ="we just receive £10.000 for cookies"
x=re.findall("\£[0-9.]+",zz)
print(x)
# this escape character