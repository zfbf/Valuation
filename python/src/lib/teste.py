import sys
from .utils import generate_random_int

print(sys.platform)
print(sys.path)
print('random int: {}'.format(generate_random_int(3, 9)))
print('__name__ : {}'.format(__name__))
print('__file__: {}'.format(__file__))
print('package: {}'.format(str(__package__)))

