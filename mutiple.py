
#
#Author:Yoshiki Hoshinaga
#Date: June 8
#Title: Ps8pr3

#1
def double(s):
    """ your docstring goes here """
    result = ''
    for c in s:
        result+= c + c
    return result
#2
def weave(s1,s2):
    """ your docstring goes here """
    result = ''
    len_shorter = min(len(s1), len(s2))
    for i in range(len_shorter):
        result+=s1[i]
        result+=s2[i]
    result+=s1[len_shorter:]
    result+=s2[len_shorter:]
    return result
#3
def square_evens(vals):
    for i in range(len(vals)):
        if vals[i]%2==0:
            vals[i]=vals[i]**2


#4
def index(elem,seq):
    for i in range(len(seq)):
        if seq[i]==elem:
            return i
    return-1

if __name__=='__main__':
#test1
    print(double('hello'))
    print(double('python'))
    print(double(''))
    
#test2
    print(weave('aaaaaa', 'bbbbbb'))
    print(weave('abcde', 'VWXYZ'))
    print(weave('abcde', 'VWXYZ'))
    print(weave('aaaaaa', 'bb'))
    print(weave('aaaa', 'bbbbbb'))
    print(weave('aaaa', ''))
    print(weave('', 'bbbb'))
    print(weave('', '') )

#test3
    vals1 = [1,2,3,4,5,6]
    square_evens(vals1)
    print(vals1)
    vals2 = [7,3,10,8]
    square_evens(vals2)
    print(vals2)
    
    
#test4
    print('index(5, [4, 10, 8, 5, 3, 5])',index(5, [4, 10, 8, 5, 3, 5]))
    print('index("hi", ["well", "hi", "there"])',index('hi', ['well', 'hi', 'there']))
    print('index("b", "banana")',index('b', 'banana'))
    print('index("a", "banana")',index('a', 'banana'))
    print('index("n", "banana")',index('n', 'banana'))
    print('index("i", "team")',index('i', 'team'))
    print('index(8, [4, 10, 5, 3])',index(8, [4, 10, 5, 3]))
