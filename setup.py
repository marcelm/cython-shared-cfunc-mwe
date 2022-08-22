from setuptools import setup, Extension

setup(ext_modules=[
    Extension("foo.one", sources=["foo/one.pyx", "foo/cfunc.c"]),
    Extension("foo.two", sources=["foo/two.pyx"]),
])
