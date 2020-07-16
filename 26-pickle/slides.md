%title: PYTHON
%author: xavki
%Site : xavki.blog


# PYTHON : Pickle


<br>
* serialization/deserialization = Python objects > binaire

* objets : class, lists, dictionnaires...

* sauvegarder, conserver, compresser

<br>
* on pickle

```
dictionnaire = {
    "alias": "xavki",
    "prenom": "xavier",
    "ville": "paris"
}
print(dictionnaire)
output = open("ouput.pickle","wb")
pickle.dump(dictionnaire,output)
output.close()
```

<br>
* on depickle

```
input = open("output.pickle","rb")
dictin = pickle.load(input)
print(dictin)
```
