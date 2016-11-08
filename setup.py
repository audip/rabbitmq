from setuptools import setup, find_packages


setup(
    name='rabbit_mq_examples',

    version='0.2',

    description='Rabbit MQ examples',

    # Author details
    author='Aditya Purandare',

    # Choose your license
    license='Apache',

    classifiers=[
        'Development Status :: 3 - Alpha',

        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',

        'License :: OSI Approved :: Apache License',

        'Programming Language :: Python :: 2.7',
    ],

    install_requires=['pika'],
)
