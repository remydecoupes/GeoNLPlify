Installation
============

You can install GeoNLPlify in three ways:

- using pip
- in a `virtual environment (venv) <#virtual-environment>`__
- in a `conda environment <#conda-environment>`__ or

Pip install
~~~~~~~~~~~

.. code:: bash

    pip install GeoNLPlify
    python3 -c "from geonlplify import download_simplemaps_data; download_simplemaps_data()" # download simplemaps data
    python -m spacy download en_core_web_trf # download spacy model


Virtual Environment
~~~~~~~~~~~~~~~~~~~

1. Git clone this repository

.. code:: bash

    git clone https://github.com/remydecoupes/GeoNLPlify.git

2. Create a virtual env

.. code:: bash

    python -m venv geonlplify_venv   source geonlplify_venv/bin/activate   pip install --upgrade pip

3. Install dependencies

.. code:: bash

    cd GeoNLPlify   pip install -r virtual_env_requirements.txt

4. Donwload `world-cities from simple maps <https://simplemaps.com/data/world-cities>`

.. code:: bash

   wget -qO- https://simplemaps.com/static/data/world-cities/basic/simplemaps_worldcities_basicv1.75.zip  | bsdtar -xvf- -C ./geonlplify/simplemaps/

Conda environment
~~~~~~~~~~~~~~~~~

1. Git clone this repository

.. code:: bash

   git clone https://github.com/remydecoupes/GeoNLPlify.git

2. Create a conda with all the required dependencies

.. code:: bash

   cd GeoNLPlify
   conda env create -n geonlplify_conda --file conda_environment.yml python==3.10.6
   conda activate geonlplify_conda

3. Install spacy models

.. code:: bash

   python -m spacy download en_core_web_trf

4. Donwload `world-cities from simple
   maps <https://simplemaps.com/data/world-cities>`__

.. code:: bash

   wget -qO- https://simplemaps.com/static/data/world-cities/basic/simplemaps_worldcities_basicv1.75.zip  | bsdtar -xvf- -C ./geonlplify/simplemaps/