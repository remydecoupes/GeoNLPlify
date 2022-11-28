.. GeoNLPlify documentation master file, created by
   sphinx-quickstart on Wed Nov 23 11:37:11 2022.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to GeoNLPlify's documentation!
======================================

.. image:: ./../readme_ressources/geonlplify_example_schema.png

A NLP library for data augmentation focusing on spatial information contained in text.

Usage:

.. code-block:: python
   :linenos:
   :emphasize-lines:  4

   >>> import geonlplify
   >>> my_text = "My name is Clara and I live in Berkeley."
   >>> geonlplify.geonlplify(my_text)
   'My name is Clara and I live in Bristol'

.. toctree::
   :maxdepth: 2
   :caption: Contents:

   ./index.rst
   ./installation.rst
   ./contributions.rst
   ./api
   ./acknowledgements
