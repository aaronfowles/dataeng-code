from distutils.core import setup

install_requires = open('requirements.txt').read().strip().split('\n')

# add pytest-runner from setup_requires
install_requires.append('pytest')

setup(
    name='dataeng_code',
    version='0.0.5',
    packages=['dataeng_code'],
    install_requires=install_requires,
    tests_require=[
        'pytest'
    ],
    include_package_data=True,
    python_requires=">=3.6.*"
)
