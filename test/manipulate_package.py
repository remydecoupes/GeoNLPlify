import geonlplify

help(geonlplify)
help(geonlplify.geonlplify)

text = "5 cases of avian influenza found in Montpellier"
for i in range(5):
    print(geonlplify.geonlplify(text))
