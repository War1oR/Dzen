__author__ = 'warior'
__mastermind__ = ['http://legacy.python.org/dev/peps/pep-0428/']
import pathlib

p1 = pathlib.Path('/home/w#/work_area')
p2 = pathlib.Path(p1, 'test')

print('{0} > {1} - {2}'.format(p1, p2, p1 > p2))
print('{0} < {1} - {2}'.format(p1, p2, p1 < p2))
print('{0} = {1} - {2}'.format(p1, p2, p1 == p2))
print('------')

p3 = pathlib.PurePath(p1, 'set.py')
print('path - {0}\nname - {1}\nsuffix - {2}\nsuffixes - {3}\np2 exists ? - {4}\nparts - '
      '{5}\nroot - {6}'.format(p3, p3.name, p3.suffix, p3.suffixes, p2.exists(),
                                 p3.parts, p3.root))
print('------')

p4 = pathlib.PurePosixPath('/home')
p4 /= 'foo'
p4 = p4.joinpath('bar')
print(p4)
print('------')

print(p1.is_dir())
#p.is_file()
#p.is_dir()
#p.is_symlink()
#p.is_socket()
#p.is_fifo()
#p.is_block_device()
#p.is_char_device()
print('------')
p = pathlib.Path('docs')
#for child in p.iterdir(): child
