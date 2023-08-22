print('print 1')

if __name__ == '__main__':
    import sys
    from pprint import pprint
    print('Hello World! Python will look for code in these directories:')
    pprint(sys.path)
    pass
else:
    print('print 2')

print('print 3')