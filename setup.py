from setuptools import setup, find_packages
import sys, os

version = '0.0'

setup(name='treddit-notifs',
      version=version,
      description="Treddit Notifications",
      long_description="""\
Timed notifications for Reddit""",
      classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      keywords='',
      author='Brenden Crowie',
      author_email='brenden@crowie.dev',
      url='https://crowie.dev',
      license='',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
