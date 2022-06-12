import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="dbteasy",
    version="0.2.6",
    author="Arthur Morais",
    author_email="arthurfmmorais@gmail.com",
    description="A small package to simplify the use of dbt core",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ArthurMor4is/dbteasy",
    project_urls={
        "Bug Tracker": "https://github.com/ArthurMor4is/dbteasy/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    py_modules=["dbteasy"],
    python_requires=">=3.9.13",
    packages=setuptools.find_packages(),
    install_requires=["invoke==1.7.1"],
    entry_points={"console_scripts": ["dbteasy = dbteasy.main:program.run"]},
)
