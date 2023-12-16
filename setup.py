import setuptools

setuptools.setup(
    name="geonlplify",
    version="0.3.18",
    url="https://github.com/remydecoupes/GeoNLPlify",
    author="Rémy Decoupes",
    author_email="remy.decoupes@inrae.fr",
    description="GeoNLPlify aims to make variations of an input sentence working on spatial information contained in words",
    packages=setuptools.find_packages(),
    install_requires=[
        "pandas",
        "requests",
        "spacy==3.4.2",
        "tokenizers==0.12.1",
        "transformers==4.21.3",
        "spacy-transformers==1.1.8",
        "torch==1.13.0",
    ],
    classifiers=[
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.10',
    ],
)