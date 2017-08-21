from distutils.core import setup

setup(name='mkdata',
      version='0.1.0',
      description='Python general utilities and code snippets',
      author='Alvaro Ulloa',
      author_email='aeulloacerna@geisinger.edu',
      url='https://github.com/alvarouc/py_utils',
      packages=['mkdata'],
      install_requires=[
          'numpy',
          'sklearn'],
      entry_points={'console_scripts':
                    ['mkdata=mkdata.main:main']},

      )
