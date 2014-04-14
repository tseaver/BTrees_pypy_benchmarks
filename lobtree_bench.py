"""lobtree_bench [options]

Exercise adding keys/values to an LOBTree, and verify them.

Options:
--------

-s, --seed      Seed to be passed to 'random.seed()' (default, 0xDEADBEEF).

-n, --count     How many key ranges to generate (default, 10000)
"""
import getopt
import random
import sys
import time

from BTrees.LOBTree import LOBTree

USAGE = __doc__

try:
    xrange
except NameError: # Py3k
    xrange = range

def generate_keys(how_many=50000):
    keys = {}
    for block in xrange(how_many):
        keys[random.randint(0, 0xFFFFFFFF)] = None
    return keys

def populate_lobtree(keys):
    # Simulate a BTree with keys as ranges of contiguous blocks w/ random base
    # Aim for 500K keys.
    tree = LOBTree()
    for base in keys:
        count = keys[base] = random.randint(900, 1000)
        for i in xrange(count):
            key = base + i
            tree[key] = '%s' % key
    return tree

def verify_lobtree(tree, keys):
    for base in random.sample(list(keys), len(keys)):
        for i in xrange(keys[base]):
            key = base + i
            assert(tree[key] == '%s' % key)


def main(argv=sys.argv[1:]):
    seed = 0xDEADBEEF
    how_many = 10000
    try:
        opts, args = getopt.getopt(argv, 's:n:h?',
                                   ['seed=',
                                    'count=',
                                    'help',
                                   ])
    except getopt.GetoptError:
        print(USAGE)
        sys.exit(1)

    if args:
        print(__doc__)
        sys.exit(1)

    for k, v in opts:

        if k in ('-h', '-?', '--help'):
            print(__doc__)
            sys.exit(2)

        if k in ('-s', '--seed'):
            try:
                seed = int(v)
            except:
                seed = v

        if k in ('-n', '--count'):
            how_many = int(v)

    random.seed(seed)
    keys = generate_keys(how_many)
    start = time.time()
    tree = populate_lobtree(keys)
    after_populate = time.time()
    verify_lobtree(tree, keys)
    after_verify = time.time()

    print('=' * 30)
    print('Timings (for %d key bases)' % how_many)
    print('=' * 30)
    print('Populate tree:  %8.3f sec' % (after_populate - start))
    print('Verify tree:    %8.3f sec' % (after_verify - after_populate))
    print('-' * 30)
    print('Total:          %8.3f sec' % (after_verify - start))
    print('=' * 30)

if __name__ == '__main__':
    main()
