from customdict import CustomIntFloatDict

test_1 = CustomIntFloatDict()
print(test_1)

#test_2 = CustomIntFloatDict({'a','b'},[23,78])

#test_3 = CustomIntFloatDict(('x','y','z'),(10,'twenty',30))
test_4 = CustomIntFloatDict(('x','y','z'),(10,20,30))
print(test_4)

test_4['r'] = 1.4
print(test_4)

test_4['h'] = 'bla'
print(test_4)
