from appDjango.models import Familiar
from appDjango.models import Mascota
from appDjango.models import Vehiculo

Familiar(nombre="Nahuel", fecha_de_nacimiento="02/01/02",dni=43156879).save()
Familiar(nombre="Matias", fecha_de_nacimiento="20/02/90",dni=43156879).save()
Familiar(nombre="Viviana", fecha_de_nacimiento="03/07/67",dni=43156879).save()

Mascota(nombre="Rocky", edad="11", animal="Perro").save()
Mascota(nombre="Maia", edad="9", animal="Gato").save()
Mascota(nombre="Cachy", edad="5", animal="Perro").save()

Vehiculo(tipo="Auto", antiguedad="5", marca="Renault").save()
Vehiculo(tipo="Bicicleta", antiguedad="0", marca="Mountainbike").save()
Vehiculo(tipo="Moto", antiguedad="1", marca="Yamaha").save()

print("Se cargo con éxito los usuarios de pruebas")