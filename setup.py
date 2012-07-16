from distutils.core import setup

from webauth import __version__

setup(
    name='webauth',
    description="A WSGI-compliant implementation of WebAuth.",
    author='Oxford University Computing Services',
    author_email='infodev@oucs.ox.ac.uk',
    version=__version__,
    packages=['webauth'],
    license='BSD',
    url='https://github.com/oucs/wsgi-webauth',
)
