from setuptools import setup, find_packages
import os

version = '0.1'

setup(name='gomobiletheme.irceline',
      version=version,
      description="A theme for Go mobile for Plone",
      long_description=open("README.txt").read() + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      # Get more strings from
      # http://pypi.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
        "Framework :: Plone",
        "Programming Language :: Python",
        ],
      keywords='gomobile theme IRCEL CELINE irceline',
      author='Olav Peeters',
      author_email='peeters@irceline.be',
      url='http://github.com/opeeters/',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['gomobiletheme'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          'gomobiletheme.basic',
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      # -*- Entry points: -*-

      [z3c.autoinclude.plugin]
      target = plone
      """,
      setup_requires=["PasteScript"],
      paster_plugins = ["ZopeSkel"],

      )
