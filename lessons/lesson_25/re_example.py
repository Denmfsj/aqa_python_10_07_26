# https://regex101.com/

# (Apple\s)([\D]+\s)?(price)\s(is\s)?([0-9]){1,4}\s[Uu][Ss][Dd]

# (Apple\s) - конкретно Apple + знак розділення
# ([\D]+\s) - будь який текст з пробілом
#  (price)\s конкретно price + знак розділення
#  ([0-9]){1,4} цифра яке складаетсья з 1,2,3,4 символів
#  [Uu][Ss][Dd] в кінці USD не залено від регістра

# Apple price is 200 usd
# Apple last close price 230 USD
# Apple close price is 180 Usd
#
# Apple close price is 180 EUR
# Apple AUM is 180 EUR
# Apple MC is 180 EUR

import re

pattern = r"(Apple\s)([\D]+\s)?(price)\s(is\s)?([0-9]{1,4}\s)([Uu][Ss][Dd])"

text = '''Apple price is 20000 usd
Apple last close price 230 USD
Apple close price is 180 Usd

Apple close price is 180 EUR
Apple AUM is 180 EUR
Apple MC is 180 EUR'''

print(re.findall(pattern, text))
if not re.findall(pattern, text):
    print('assert Cant find expected text')


res = re.search(pattern, text)
print(res.group(5))