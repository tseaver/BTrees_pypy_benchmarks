from setuptools import setup

with open('README.rst') as f:
    README = f.read()

with open('CHANGES.rst') as f:
    CHANGES = f.read()

setup(name='BTrees_pypy_benchmarks',
      version='0.1',
      description='BTrees benchmarks for PyPY',
      long_description='\n\n'.join([README, CHANGES]),
      py_modules=[
        'lobtree_bench',
      ],
      install_requires=['BTrees'],
      entry_points = """\
        [console_scripts]
        lobtree_bench = lobtree_bench:main
        """,
     )
