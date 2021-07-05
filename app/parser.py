import os
import xml.etree.cElementTree as ET
from datetime import datetime
from pprint import pprint

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


def main():
    # parse_xml_data_list = [
    #     parse_xml_data_to_dict(XML_FILE_PATH + file)
    #     for file in file_list
    #     if parse_xml_data_to_dict(XML_FILE_PATH + file)
    # ]
    # pprint(parse_xml_data_list)
    # parse_xml_data_list = [
    # parse_xml_data_to_dict(XML_FILE_PATH + file)
    # xml_data_dict = parse_xml_data_to_dict(XML_FILE_PATH + file)
    for file in file_list:
        xml_data_dict = parse_xml_data_to_dict(XML_FILE_PATH + file)

        # if xml_data_dict:
        #     T_Procedures.objects.created(
        #         curator=T_Users.objects.get(curator_id=2),
        #         xml_type=xml_data_dict['xml_type'],
        #         purchaseNumber=int(xml_data_dict['purchaseNumber']),
        #         docPublishDate=datetime.datetime.strptime(xml_data_dict['docPublishDate'], '%Y-%m-%d %H:%M:%S.%f'),
        #         purchaseObjectInfo=xml_data_dict['purchaseObjectInfo'],
        #         regNum=xml_data_dict['regNum'],
        #         maxPrice=int(xml_data_dict['maxPrice'])
        #     )

        pprint(xml_data_dict)


if __name__ == '__main__':
    main()
