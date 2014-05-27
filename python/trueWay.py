__author__ = 'warior'

if __name__ == '__main__':
    print('-----------x, not x-----------')
    name = 'Jo'
    lastName = ''
    if name:
        print('name')
    if not lastName:
        print('Why?')
    print('--------------in--------------')
    if 'H' in name:
        print('Yes!')
    else:
        print('No')
    mSet = ('foo', 'bar', 'psi')
    for i in mSet:
        print('Name - ', i)
    print('--------------=)--------------')
    a, b = 'foo', 'bar'
    print(a, b)
    a, b = b, a
    print(a, b)
    print('-------------join-------------')
    char = ('S', 'u', 'p', 'e', 'r', 'F', 'o', 'o', '!')
    name = ''.join(char)
    print(name)
    print('-------------try--------------')
    var = {'n': '5'}
    try:
        print(var['n'])
    except(KeyError, TypeError, ValueError):
        print('None')
    print('-------------enum-------------')
    for n, i in enumerate(mSet):
        print(n, i)
    print('-----list comprehensions------')
    dat = (range(10))
    res = [i * 2 for i in dat if i % 2 == 0]
    print(res)
    print('-------------dict-------------')
    key = ['foo', 'bar', 'slow', 'pip', 'ext']
    m_dict = dict(zip(key, res))
    print(m_dict)
