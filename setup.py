import os
import re
import sys

from setuptools import setup, find_packages


v = open(
    os.path.join(
        os.path.dirname(__file__),
        'dogpile_cache_native_redis', '__init__.py')
)
VERSION = re.compile(r".*__version__ = '(.*?)'", re.S).match(v.read()).group(1)
v.close()

readme = os.path.join(os.path.dirname(__file__), 'README.rst')

setup(
    name='dogpile_cache_native_redis',
    version=VERSION,
    description="backend for dogpile.cache with reading and writing the native value",
    long_description=open(readme).read(),
    install_requires=['dogpile.cache>=0.6.2', 'redis>=2.10.5'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
    ],
    keywords='caching',
    author='Shinya Okano',
    author_email='tokibito@gmail.com',
    url='https://github.com/tokibito/dogpile_cache_native_redis',
    license='MIT',
    packages=find_packages('.', exclude=['tests*']),
    entry_points="""
    [dogpile.cache]
    native_redis = dogpile_cache_native_redis.backends:NativeRedisBackend
    """,
    zip_safe=True,
)
