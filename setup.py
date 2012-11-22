from setuptools import setup, find_packages

version = '1.1.1.dev0'

setup(name='policy.cpasforest',
      version=version,
      description="'policy of CPAS Forest'",
      long_description=open("README.rst").read() + "\n" +
                       open("CHANGES.txt").read(),
      # Get more strings from
      # http://pypi.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
        "Framework :: Plone",
        "Programming Language :: Python",
        ],
      keywords='',
      author='',
      author_email='',
      url='http://svn.plone.org/svn/collective/',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['policy'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          # -*- Extra requirements: -*-
          'collective.ckeditor',
          'collective.easyslider',
          'Solgema.fullcalendar',
          'collective.collage.maps',
          'collective.collage.easyslider',
          'collective.gallery',
          'quintagroup.analytics',
          'collective.recaptcha',
          'qi.portlet.TagClouds',
	  'Products.PloneFormGen',
          'plonetheme.cpasforest'
      ],
      entry_points="""
      # -*- Entry points: -*-

      [z3c.autoinclude.plugin]
      target = plone
      """,
      )
