from setuptools import setup, find_packages

setup(
    name='djangocodemirror',
    version=__import__('djangocodemirror').__version__,
    description=__import__('djangocodemirror').__doc__,
    long_description=open('README.rst').read(),
    author='David Thenon',
    author_email='sveetch@gmail.com',
    url='http://pypi.python.org/pypi/djangocodemirror',
    license='MIT',
    packages=find_packages(),
    classifiers=[
        'Programming Language :: Python',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Text Editors :: Text Processing',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    install_requires=[
        'rstview>=0.1.2',
    ],
    include_package_data=True,
    zip_safe=False
)