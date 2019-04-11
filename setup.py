from setuptools import setup

setup(name='genderless',
      version='0.1',
      description='Voice algorithms that do not rely on gender',
      url='https://osf.io/7vzyb/',
      author='David R. Feinberg',
      author_email='feinberg@mcmaster.ca',
      license='MIT',
      packages=['genderless'],
      install_requires=[
          'parselmouth',
      ],
      zip_safe=False)
