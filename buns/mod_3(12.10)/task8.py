# 8
my_str = "+7 (812) 134-12-324"
c = ''.join([x for x in my_str if x not in (" ", "(", ")", "-")])
print(c)
