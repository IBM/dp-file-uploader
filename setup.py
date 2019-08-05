from setuptools import setup

version = {}
with open('./dp_file_uploader/version.py') as fp:
    exec(fp.read(), version)

setup(
    name='dp_file_uploader',
    version=version['__version__'],
    description='Push file(s) to a DataPower Gateway via the XML Management Interface.',
    url='https://github.com/IBM/dp-file-uploader',
    author='Aidan Harbison',
    author_email='aharbis@us.ibm.com',
    license='MIT',
    packages=[
        'dp_file_uploader'
    ],
    entry_points={
        'console_scripts': [
            'dp-file-uploader=dp_file_uploader.command_line:main'
        ]
    },
    install_requires=[
        'requests'
    ],
    zip_safe=False
)
