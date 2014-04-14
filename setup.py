from setuptools import setup

with open('README.rst') as f:
    README = f.read()

with open('CHANGES.rst') as f:
    CHANGES = f.read()

setup(name='BTrees_pypy_benchmarks',
      version='0.1',
      description='BTrees benchmarks for PyPY',
      long_description='\n\n'.join([README, CHANGES]),
      url='https://github.com/tseaver/BTrees_pypy_benchmarks',
      author='Tres Seaver',
      author_email='tseaver@agendaless.com',
      py_modules=[
        'lobtree_bench',
      ],
      classifiers=[
        "Development Status :: 3 - Alpha",
        "Framework :: ZODB",
        "License :: OSI Approved :: Zope Public License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.2",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: Implementation :: CPython",
        "Programming Language :: Python :: Implementation :: PyPy",
      ],
      install_requires=['BTrees'],
      entry_points = """\
        [console_scripts]
        lobtree_bench = lobtree_bench:main
        """,
     )
