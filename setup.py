import setuptools

setuptools.setup(
    name="geonlplify",
    version="0.1.0",
    url="",
    author="Rémy Decoupes",
    author_email="",
    description="GeoNLPlify aims to make variations of an input sentence working on spatial information contained in words",
    long_description=open('README.md').read(),
    packages=setuptools.find_packages(),
    install_requires=["pandas", "spacy", "requests"],
    classifiers=[
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.10',
    ],
)