from setuptools import setup

setup(
    name='HighSpider',
    version='1.0',
    py_modules=['main'],
    entry_points={'scrapy': ['settings = main']},
)
