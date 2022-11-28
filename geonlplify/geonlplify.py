import pandas as pd
import spacy
import requests # for geocoding with photon and OSM data
import numpy as np
from random import randrange # select random cities
import pkg_resources

global importing_error
importing_error = []

try:
    nlp_en = spacy.load("en_core_web_trf") # speed up things. No need to load spacy several times
except:
    error = "Error: no spacy model found!: download the spacy en_core_web_trf: 'python -m spacy download en_core_web_trf'"
    importing_error.append(error)
global world_cities_df # global var to speed run time

def load_simplemaps():
    """
    Load simplemaps from https://simplemaps.com/data/world-cities
    CC-BY 4.0 attribution from https://simplemaps.com/data/world-cities
    :return:
    """
    try:
        stream = pkg_resources.resource_stream(__name__, "/simplemaps/worldcities.csv")
        print("loading data from https://simplemaps.com/data/world-cities")
        return pd.read_csv(stream)
    except:
        error = "No data found!: download world-cities from simplemaps: python3 -c \"from geonlplify import download_simplemaps_data; download_simplemaps_data()\""
        importing_error.append(error)

def importing_error_check():
    """
    Check if there is any importing issue (like missing data or spacy model)
    :return:
    """
    if len(importing_error) != 0:
        raise ImportError

world_cities_df = load_simplemaps()

def geonlplify(text, method="spatial_synonym"):
    """
    GeoNLPlify aims to make variations of an input sentence working on spatial information contained in words

    Examples:
        >> geonlplify.geonlplify("5 cases of avian influenza found in Montpellier")
        5 cases of avian influenza found in Bangalore

    :param text: Input
    :param method: Between those 3 methods [generalization, specialization, spatial_synonym]
    :return: the variation of the input text
    """

    try:
        importing_error_check()
    except:
        print(*importing_error, sep="\n")
        exit()

    list_sne = find_sne(text)
    list_geonlplify_variant = spatial_varations(list_sne, method)
    return replace_variants(text, list_geonlplify_variant, method)


def replace_variants(text, list_of_variant, method, conserve_n_gram=True):
    """

    :param text:
    :param list_of_variant: example:
        - error:
            [{'name': 'South Sudan', 'label': 'GPE', 'start_char': 56, 'end_char': 67, 'generalization': nan, 'generalization_failed': 'sea'}]
        - ok:
            [{'name': 'New Jersey', 'label': 'GPE', 'start_char': 39, 'end_char': 49, 'generalization': 'United States'}]
    :return:
    """
    if list_of_variant:  # list is not empty
        for sne in list_of_variant:
            try:
                if sne[method] != np.nan and sne["name"] != str(sne[method]):
                    if conserve_n_gram:
                        if sne["name"].count(' ') == str(sne[method]).count(' '):
                            text = text.replace(sne["name"], str(sne[method]))
                        else:
                            text = np.nan
                    else:
                        text = text.replace(sne["name"], str(sne[method]))
                else:
                    text = np.nan
            except:
                # print("Couldn't replace text with SNE: " + str(sne) + "and text: " + text)
                text = np.nan
                return text
    else:  # empty list
        text = np.nan
    return text


def geocode(sne_name):
    """
    Input a place name and retrieves OSM properties.
    Exemple for sne_name="Montpellier":

        {'osm_id': 65442261,
        'osm_type': 'N',
        'country': 'France',
        'osm_key': 'place',
        'city': 'Montpellier',
        'countrycode': 'FR',
        'osm_value': 'city',
        'postcode': '34062',
        'name': 'Montpellier',
        'county': 'Hérault',
        'state': 'Occitanie',
        'type': 'district'}

    :param sne_name:
    :return: a dictionary with OSM properties
    """
    url_photon = "https://photon.komoot.io/api/?q="  # don't forget to force the lang: &lang=en
    try:
        reponses = requests.get(url_photon + str(sne_name) + "&lang=en")
        r = reponses.json()['features'][0]["properties"]
    except:
        print("error when geocoding: " + sne_name)
        raise Exception("Geocoding failed")
    return r


def find_sne(text):
    """
    Return list of SNE

    :param text: input text
    :return: list of SNE
    """
    list_of_sne = []

    ner = nlp_en(text)
    for entity in ner.ents:
        if entity.label_ == "GPE":
            sne = {
                "name": str(entity),
                "label": entity.label_,
                "start_char": entity.start_char,
                "end_char": entity.end_char
            }
            list_of_sne.append(sne)
    return list_of_sne


def spatial_varations(list_of_sne, method="generalization"):
    list_of_variants_sne = []

    for sne in list_of_sne:
        try:
            geocoded = geocode(sne["name"])
        except:
            continue
        if method == "generalization":
            try:
                if geocoded["osm_value"] == "sea":
                    sne["generalization"] = np.nan
                    sne["generalization_failed"] = "sea"
                elif geocoded["osm_value"] == "continent":
                    sne["generalization"] = np.nan
                    sne["generalization_failed"] = "continent"
                else:  # nothing special
                    sne["generalization"] = geocoded["country"]
            except:
                # raise Exception("No country for " + sne["name"] + "  | geocode: \n" + str(geocoded))
                print("No country for " + sne["name"] + "  | geocode: \n" + str(geocoded))
                continue
        elif method == "specialization":
            if geocoded["osm_value"] == "country":
                try:
                    country_cities = world_cities_df[world_cities_df["country"] == geocoded["country"]]
                    if len(country_cities) != 0:
                        sne["specialization"] = country_cities["city"].iloc[randrange(len(country_cities))]
                    else:
                        sne["specialization"] = np.nan
                except:
                    print("No country for " + sne["name"] + "  | geocode: \n" + str(geocoded))
                    continue
        elif method == "spatial_synonym":
            if geocoded["osm_value"] == "city":
                try:
                    sne["spatial_synonym"] = world_cities_df["city"].iloc[randrange(len(world_cities_df))]
                except:
                    print("No city for " + sne["name"] + "  | geocode: \n" + str(geocoded))
                    sne["spatial_synonym"] = np.nan
            elif geocoded["osm_value"] == "country":
                try:
                    sne["spatial_synonym"] = world_cities_df["country"].iloc[randrange(len(world_cities_df))]
                except:
                    print("No country for " + sne["name"] + "  | geocode: \n" + str(geocoded))
                    sne["spatial_synonym"] = np.nan
        else:
            print("The method is unknown")
            raise Exception("The method is unknown")
        list_of_variants_sne.append(sne)
        return list_of_variants_sne

def download_simplemaps_data():
    import requests, zipfile
    from io import BytesIO

    print("GeoNLPlify uses simplemaps data: https://simplemaps.com/data/world-cities.\n Please be respectfull with their license (CC-BY)")
    url = "https://simplemaps.com/static/data/world-cities/basic/simplemaps_worldcities_basicv1.75.zip"
    filename = url.split('/')[-1]
    req = requests.get(url)
    zipfile = zipfile.ZipFile(BytesIO(req.content))
    import geonlplify
    dir = geonlplify.__path__
    zipfile.extractall(dir[0] + "/simplemaps/")



