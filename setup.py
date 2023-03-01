from setuptools import setup, find_packages

try:
    import torch
except ImportError:
    raise EnvironmentError('Torch must be installed before install moftransformer')

with open("requirements.txt", "r") as f:
    install_requires = f.readlines()

extras_require = {
    'docs': ['sphinx', 'livereload', 'myst-parser']
}


setup(
    name = "moftransformer",
    version = "1.0",
    author = "akshat",
    description = "This is a custom package developed by Volta by Akshat",
    packages=find_packages(),
    package_data={'moftransformer': ['libs/GRIDAY/*', 'libs/GRIDAY/scripts/*', 'libs/GRIDAY/FF/*',
                                     'assets/*.json', 'examples/dataset/*', 'examples/dataset/**/*',
                                     'examples/raw/*', 'examples/visualize/dataset/*', 'examples/visualize/dataset/test/*']},
    install_requires=install_requires,
    extras_require=extras_require,
)