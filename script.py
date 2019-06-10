
import sys

for line in sys.stdin:
    print(line)

print ('Number of arguments:', len(sys.argv), 'arguments.')
print ('Argument List:', str(sys.argv))

try:
    t = open('foo_copy.txt')
    print('*' * 100)
    print(t.content)
    print('*' * 100)
except Exception as e:
    print(e)
