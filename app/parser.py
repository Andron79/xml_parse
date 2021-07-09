import os
import xml.etree.cElementTree as ET
from parse.settings import XML_FILE_PATH, XML_FIELDS

key_set = XML_FIELDS
file_list = os.listdir(XML_FILE_PATH)


def remove_namespaces(string):
    return string[string.rfind("}") + 1:len(string)]


def parse_xml_data_to_dict(xml_file):
    xml_data_dict = {}
    try:
        root = ET.parse(xml_file).getroot()
        xml_data_dict = {'xml_type': remove_namespaces(root.tag)}
        for child_of_root in root.iter():
            if remove_namespaces(child_of_root.tag) in key_set:
                xml_data_dict[remove_namespaces(child_of_root.tag)] = child_of_root.text
    except ET.ParseError as e:
        print(e, 'Ошибка обработки файла xml')
    return xml_data_dict


def parse_xml_data_to_list():
    """
    Получение списка словарей с распарсенными данными из xml файлов
    :return: list
    """
    parse_xml_data_list = [
        parse_xml_data_to_dict(XML_FILE_PATH + file) for file in file_list if
        parse_xml_data_to_dict(XML_FILE_PATH + file)
    ]

    return parse_xml_data_list
