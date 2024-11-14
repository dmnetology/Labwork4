# -*- coding: utf-8 -*-
import xml.etree.ElementTree as xml
import json
import xmltodict


def createXML(filename):

    # Создать XML файл.

    root = xml.Element("Persons")

    person1 = xml.Element("Person")
    root.append(person1)
    # создаем дочерний суб-элемент.
    name = xml.SubElement(person1, "Name")
    name.text = "Иван"

    age = xml.SubElement(person1, "Age")
    age.text = "30"

    profession = xml.SubElement(person1, "Profession")
    profession.text = "учитель"

    city = xml.SubElement(person1, "City")
    city.text = "Санкт-Петербург"

    person2 = xml.Element("Person")
    root.append(person2)
    # создаем дочерний суб-элемент.
    name = xml.SubElement(person2, "Name")
    name.text = "Анна"

    age = xml.SubElement(person2, "Age")
    age.text = "25"

    profession = xml.SubElement(person2, "Profession")
    profession.text = "инженер"

    city = xml.SubElement(person2, "City")
    city.text = "Москва"

    person3 = xml.Element("Person")
    root.append(person3)
    # создаем дочерний суб-элемент.
    name = xml.SubElement(person3, "Name")
    name.text = "Максим"

    age = xml.SubElement(person3, "Age")
    age.text = "27"

    profession = xml.SubElement(person3, "Profession")
    profession.text = "программист"

    city = xml.SubElement(person3, "City")
    city.text = "Екатеринбург"

    person4 = xml.Element("Person")
    root.append(person4)
    # создаем дочерний суб-элемент.
    name = xml.SubElement(person4, "Name")
    name.text = "Ольга"

    age = xml.SubElement(person4, "Age")
    age.text = "26"

    profession = xml.SubElement(person4, "Profession")
    profession.text = "дизайнер"

    city = xml.SubElement(person4, "City")
    city.text = "Краснодар"

    person5 = xml.Element("Person")
    root.append(person5)
    # создаем дочерний суб-элемент.
    name = xml.SubElement(person5, "Name")
    name.text = "Елена"

    age = xml.SubElement(person5, "Age")
    age.text = "28"

    profession = xml.SubElement(person5, "Profession")
    profession.text = "врач"

    city = xml.SubElement(person5, "City")
    city.text = "Новосибирск"


    tree = xml.ElementTree(root)

    with open(filename, "wb") as fh:
        tree.write(fh)

def convert_xml_json(filename_xml, filename_json):
    with open(filename_xml, encoding='utf-8') as xml_file:
        data_dict = xmltodict.parse(xml_file.read())

        json_data = json.dumps(data_dict)

        with open(filename_json, "w") as json_file:
            json_file.write(json_data)


if __name__ == "__main__":
    createXML("d://persons2.xml")
    convert_xml_json("d://persons2.xml", "d://persons2.json")