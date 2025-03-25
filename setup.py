from setuptools import setup, find_packages

setup(
    name='diablo-auto',
    version='0.1.0',
    author='Your Name',
    author_email='your.email@example.com',
    description='A project for automating tasks related to Diablo.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/yourusername/diablo-auto',
    packages=find_packages(),
    install_requires=[
        # List your project dependencies here
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)