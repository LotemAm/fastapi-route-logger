import pathlib

from setuptools import setup

here = pathlib.Path(__file__).parent.resolve()

long_description = (here / "readme.md").read_text(encoding="utf-8")

setup(
    name="fastapi-route-logger",
    version="0.0.2",
    description="Simple middleware for FastAPI to generate log entries on all requests",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/jeffsiver/fastapi-route-logger",
    author="Jeff Siver",  # Optional
    author_email="jeffsiver@gmail.com",
    classifiers=[  # Optional
        "Development Status :: 3 - Alpha",
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3 :: Only",
    ],
    keywords="fastapi, logging",
    packages=["route_logger"],
    python_requires=">=3.7, <4",
    install_requires=["fastapi"],
)