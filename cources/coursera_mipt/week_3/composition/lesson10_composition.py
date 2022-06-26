import json


class Pet:
    def __init__(self, name):
        self.name = name


class Dog(Pet):
    def __init__(self, name, breed=None):
        super().__init__(name)
        self.breed = breed


class PetExport:
    def export(self, dog):
        # does not create class instances, will be used for inheritance
        raise NotImplementedError


class ExportXML(PetExport):

    def export(self, dog):
        return """<?xml version="1.0" encoding="utf-8"?>
                <dog>
                <name>{0}</name>
                <breed>{1}</breed>
                </dog>""".format(dog.name, dog.breed)


class ExportJSON(PetExport):
    def export(self, dog):
        return json.dumps({
            "name": dog.name,
            "breed": dog.breed, })


class ExDog(Dog):
    def __init__(self, name, breed=None, exporter=None):
        super().__init__(name, breed)

        self._exporter = exporter or ExportJSON()

        if not isinstance(self._exporter, PetExport):
            raise ValueError("bad export instance value", exporter)

    def export(self):
        return self._exporter.export(self)


# create class instance and export to json by default
dog = ExDog("Harry", "Pudel", ExportXML())
print(dog.export())
