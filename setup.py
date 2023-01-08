from distutils.core import setup

import setuptools

with open("C:\\Users\\admin\\PycharmProjects\\HeadlessAsyncPywhatKit\\requirements.txt", "r") as f:
    reqs = [line.strip() for line in f]

setup(
    name="HeadLessPywhatKit",
    packages=setuptools.find_packages(),
    version="0.0.5",
    license="Apache 2.0",
    description="This is the headless Version Of pywhatKit",
    author="SigireddyBalasai",
    author_email="SigireddyBalasai@gmail.com",
    url="https://github.com/SigireddyBalasai/HeadlessAsyncPywhatKit",
    keywords=["sendwhatmsg"],
    install_requires=reqs,
    include_package_data=True,
    long_description_content_type="text/markdown",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Build Tools",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
)
