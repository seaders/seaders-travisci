from setuptools import setup

INSTALL_REQUIRES = [
]

TEST_REQUIRES = [
    'mock'
]

version = 0.01

setup(
        name='seaders-travisci',
        version=version,
        packages=[
        ],
        package_dir={
        },
        install_requires=INSTALL_REQUIRES,
        url='https://github.com/seaders/seaders-travisci',
        license='MIT',
        author='seaders',
        author_email='',
        description='travis-ci tester for seaders',
        classifiers=[
            'License :: OSI Approved :: MIT License',
            'Operating System :: OS Independent',
            'Programming Language :: Python :: 3.6',
        ],
        test_suite='tests'
)
