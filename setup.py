from setuptools import setup, find_packages

setup(name="pelicansqlgenerator",
      version="0.0.1",
      description="Feed pelican from a database",
      long_description="",
      url="https://github.com/gkrnours/pelican-sqlgenerator",
      author="gkr",
      author_email="couesl@gmail.com",
      license="ISC",
      classifiers=[
        "Development Status :: 3 - Alpha",
        "License :: OSI Approved :: ISC License (ISCL)",
        "Intended Audience :: Developers",
        "Topic :: Software Development",
        "Environment :: Plugins",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
      ],
      packages=find_packages("src"),
      package_dir={"": "src"},
      install_requires=["pelican", "peewee", "markdown"],
)
