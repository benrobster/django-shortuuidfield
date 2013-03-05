from setuptools import setup, find_packages

setup(
    name='django-shortuuidfield',
    version='0.1.0',
    author='Ben Roberts',
    author_email='roberts81@gmail.com',
    author_email='roberts81@gmail.com',
    description='Short UUIDField in Django',
    url='https://github.com/roberts/django-shortuuidfield',
    zip_safe=False,
    install_requires=[
        'django',
        'shortuuid'
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
