from setuptools import setup

setup(
    name='nuclear',
    version='0.2',
    author='Sebastian Gomez',
    author_email='sgomez@cfa.harvard.edu',
    description='Functions to determine whether a transient is nuclear.',
    url='https://github.com/gmzsebastian/nuclear',
    license='MIT License',
    python_requires='>=3.6',
    packages=['nuclear'],
    include_package_data=True,
    package_data={'nuclear': ['ref_data/*']},
    install_requires=[
        'numpy',
        'matplotlib',
        'astropy',
        'scipy',
        'emcee'
    ]
)
