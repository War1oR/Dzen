__author__ = 'warior'
__mastermind__ = ['https://docs.python.org/3.4/library/string.html#formatspec',
                  'http://pythonworld.ru/osnovy/formatirovanie-strok-metod-format.html']


print('{0}, {1}, {2}'.format('a', 'b', 'c'))
print('{}, {}, {}'.format('a', 'b', 'c'))
print('{2}, {1}, {0}'.format('a', 'b', 'c'))
print('{2}, {1}, {0}'.format(*'abc'))
print('{0}{1}{0}'.format('abra', 'cad'))
print('Coordinates: {latitude}, {longitude}'.format(latitude='37.24N', longitude='-115.81W'))
coord = {'latitude': '37.24N', 'longitude': '-115.81W'}
print('Coordinates: {latitude}, {longitude}'.format(**coord))
print("Units destroyed: {players[0]}".format(players = [1, 2, 3]))
