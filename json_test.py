import json

L=['aa','bb','cc']
L_str=json.dumps(L)
print(L_str)
print(type(L_str))
print(L_str[0])

str1='{"name":"jxn","age":31}'
str1_L=json.loads(str1)
print(str1_L)
print(type(str1_L))
print(str1_L['name'])

dict1={'name':'jxn'}
print(json.dumps(dict1))

data = {'a':True, 'b':False, 'c':None, 'd':(1,2), 1:'abc'}
print(json.dumps(data))