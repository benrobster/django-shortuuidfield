from setuptools import setup, find_packages

setup(
    name='django-shortuuidfield',
    version='0.1.3',
    author='Ben Roberts',
    author_email='roberts81@gmail.com',
    description='Short UUIDField for Django.  Good for use in urls & file names.  (Base 57, 22 characters)',
    url='https://github.com/nebstrebor/django-shortuuidfield',
    zip_safe=False,
    install_requires=[
        'django',
        'shortuuid',
        'six'
    ],
    packages=find_packages(),
    include_package_data=True,
    classifiers=[
        "Framework :: Django",
        "Intended Audience :: Developers",
        "Intended Audience :: System Administrators",
        "Operating System :: OS Independent",
        "Topic :: Software Development"
    ],
)
