from API.Iluminator_MultiSpectral import *

propiedades = dir(Iluminator_MultiSpectral)
print(propiedades)

atributos = []
get_metodos = []
set_metodos = []
methods = []

for propiedad in propiedades:
    if propiedad[-2:] == '__':
        pass

    elif propiedad[:3] == 'set':

        set_metodos.append(propiedad)

    elif propiedad[:3] == 'get':

        get_metodos.append(propiedad)

    elif propiedad[:2] == '__':

        atributos.append(propiedad)

    else:

        methods.append(propiedad)

print(atributos)
print(methods)
print(set_metodos)
