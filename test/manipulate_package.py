import geonlplify

help(geonlplify)
help(geonlplify.geonlplify)

text = "5 cases of avian influenza found in Montpellier"
text = "An unknown disease is decimating cattle in Moamba, to the consternation of the more than 3,000 breeders in that part of Maputo province, Mozambique."
for i in range(10):
    print(geonlplify.geonlplify(text))
