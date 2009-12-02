from setuptools import setup, find_packages
import os

version = '1.1'

setup(name='upc.genweb.banners',
      version=version,
      description="",
      long_description=open("README.txt").read() + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      # Get more strings from http://www.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
        ],
      keywords='',
      author='PloneTeam@UPCnet',
      author_email='plone.team@upcnet.es',
      url='https://devel.upcnet.es/svn/genwebupc/trunk/upc.genweb.banners',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['upc', 'upc.genweb'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
