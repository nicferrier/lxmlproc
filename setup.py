from distutils.core import setup

classifiers = [
    'Development Status :: 3 - Alpha',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: GNU General Public License (GPL)',
    'Operating System :: OS Independent',
    'Programming Language :: Python',
    'Topic :: Utilities',
    'Topic :: Text Processing :: Markup',
]

setup(
    name = "lxmlproc",
    version = "0.1",
    description = "lxml version of xsltproc",
    long_description = """An lxml version of the popular libxslt tool, xsltproc.""",
    license = "GNU GPL v3",
    author = "Nic Ferrier",
    author_email = "nic@ferrier.me.uk",
    url = "http://github.com/nicferrier/lxmlproc",
    download_url="http://github.com/nicferrier/lxmlproc/downloads",
    platforms = ["any"],
    scripts=['src/lxmlproc'],
    classifiers =  classifiers
    )
