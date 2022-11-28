Developpers
===========

If you want to contribute to the project, here you can find some guidelines

Building and installing the python package
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code:: bash

    python3 -m build # build the wheel
    pip install ./dist/GeoNLPlify-0.0.1-py3-none-any.whl # install the package
    python3 -c "from geonlplify import download_simplemaps_data; download_simplemaps_data()" # download simplemaps data
    python -m spacy download en_core_web_trf # download spacy model

Uninstall the python package
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code:: bash

    pip uninstall geonlplify

.. code:: bash

    rm -r [your_site_package]/geonlplify/simplempas


