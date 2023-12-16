<h1 align="center"> GeoNLPlify
:earth_africa: :book:
</h1>

[![Documentation Status](https://readthedocs.org/projects/geonlplify/badge/?version=latest)](https://geonlplify.readthedocs.io/en/latest/?badge=latest)
![GitHub](https://img.shields.io/github/license/remydecoupes/GeoNLPlify)
![GitHub release (latest by date)](https://img.shields.io/github/v/release/remydecoupes/GeoNLPlify)

A NLP library for data augmentation focusing on spatial information contained in text.

<p align="center">
  <img src="./readme_ressources/geonlplify_example_schema.png" />
</p>


## Usage
```python
import geonlplify

my_text = "My name is Clara and I live in Berkeley."
geonlplify.geonlplify(my_text)
```
```bash
'My name is Clara and I live in Bristol'
```

## Installation
```bash
pip install GeoNLPlify
# Download data. Please visit Simplemaps: https://simplemaps.com/data/world-cities
python3 -c "from geonlplify import download_simplemaps_data; download_simplemaps_data()"
# Download spacy model
python -m spacy download en_core_web_trf  
```

## Contributions
You can install GeoNLPlify in three ways: in a [virtual_env](#virtual-environment), in a [conda environment](#conda-environment)
### Virtual Environment
1. Git clone this repository
  ```bash
  git clone https://github.com/remydecoupes/GeoNLPlify.git
  ```
2. Create a virtual env
  ```bash
  python -m venv geonlplify_venv
  source geonlplify_venv/bin/activate
  pip install --upgrade pip
  ```
3. Install dependencies
  ```bash
  cd GeoNLPlify
  pip install -r virtual_env_requirements.txt
  ```

5. Donwload [world-cities from simple maps](https://simplemaps.com/data/world-cities)
  ```bash
  wget -qO- https://simplemaps.com/static/data/world-cities/basic/simplemaps_worldcities_basicv1.75.zip  | bsdtar -xvf- -C ./geonlplify/simplemaps/
  ```
### Conda environment
1. Git clone this repository
  ```bash
  git clone https://github.com/remydecoupes/GeoNLPlify.git
  ```
2. Create a conda with all the required dependencies
  ```bash
  cd GeoNLPlify
  conda create -n geonlplify_conda --file conda_environment.yml python==3.10.6
  conda activate geonlplify_conda
  ```
3. Install spacy models
  ```bash 
  python -m spacy download en_core_web_trf
  ```
4. Donwload [world-cities from simple maps](https://simplemaps.com/data/world-cities)
  ```bash
  wget -qO- https://simplemaps.com/static/data/world-cities/basic/simplemaps_worldcities_basicv1.75.zip  | bsdtar -xvf- -C ./geonlplify/simplemaps/
  ```

## Acknowledgement
:pray: This library use those terrific tools/libraries/data :muscle::
+ [Spacy](https://spacy.io/)
+ [The Komoot geocoder Photon](https://photon.komoot.io/)
+ [OpenStreeMap](https://www.openstreetmap.org/copyright)
+ [Simplemaps data](https://simplemaps.com/data/world-cities)

## Scientific publication
| Conference / journal   |      paper      |  description |
|----------|:-------------:|------:|
| [EGC'2023](https://egc2023.sciencesconf.org/) |  [short paper (in French)](https://editions-rnti.fr/?inprocid=1002848) | [video](https://youtu.be/-QaTBtjWr9g) |
| [Iospress - Intelligent Data Analysis](https://content.iospress.com/journals/intelligent-data-analysis) | [long paper (in English)](https://www.doi.org/10.3233/IDA-230040) | Open Access |
