"""
convert.py

A simple script that allows csv-xml conversion for Bandwidth's NUR

Author: Jacob Mulford

Copywrite Bandwidth INC
"""
import csv
import xmltodict


TNAO = "TelephoneNumbersAssignmentOrder"
ORDER_ID = "CustomerOrderId"
ACTION = "Action"
TNS = "TelephoneNumbers"
TN = "TelephoneNumber"

VALID_ACTIONS = ["ASSIGN", "UNASSIGN"]

def to_xml_from_csv(file_name, directory_destination, action_value, order_id):
    """
    Converts the given csv file to xml and saves it into the given
    destination in sets of 5000 phone numbers

    Args:
        file_name (str): The initial csv file to convert to xml
        directory_destination (str): The directory destination of the xml files
        action_value (str): Assignment value. ASSIGN or UNASSIGN
        order_id (str): The custom ID of the order

    Returns:
        void
    """
    # Open file for reading
    # Initialize empty xml dictionary with the following structure
    #  dict["TelephoneNumbersAssignmentOrder"] = {}
    #  dict["TelephoneNumbersAssignmentOrder"]["CustomerOrderId"] = <>
    #  dict["TNAO"]["Action"] = ASSIGN/UNASSIGN
    #  dict["TNAO"]["TelephoneNumbers"] = {}
    #  dict["TNAO"]["TelephoneNumbers"]["TelephoneNumber"] = []
    # Write dict (xmltodict.unparse(dict)) once 5000 numbers are added
    # Clear dict["TNAO"]["TNs"]["TN"]
    # Rinse and repeat
    nur_xml_dict = {}
    nur_xml_dict[TNAO] = {}
    nur_xml_dict[TNAO][ORDER_ID] = order_id
    nur_xml_dict[TNAO][ACTION] = action_value
    nur_xml_dict[TNAO][TNS] = {}
    nur_xml_dict[TNAO][TNS][TN] = []

    with open(file_name) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=",")
        csv_reader_iter = iter(csv_reader)
        next(csv_reader_iter) #Skip 1st row of csv file
        count = 0
        for row in csv_reader_iter:
            nur_xml_dict[TNAO][TNS][TN].append(row[0])

            if len(nur_xml_dict[TNAO][TNS][TN] >= 5000):
                # Write nur_xml_dict
                with open(directory_destination + "/" + str(count) + ".xml", "x") as f:
                    f.write(xmltodict.unparse(nur_xml_dict)

                # clear nur_xml_dict[TNAO][TNS][TN]
                nur_xml_dict[TNAO][TNS][TN] = []
                count += 1
