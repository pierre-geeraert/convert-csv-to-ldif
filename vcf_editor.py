import json
import quopri

#import unicodedata
#import numpy as np
#from objdict import ObjDict

path_vcf = "ignore/LDIF/2019-08-15_09-19-12.vcf"
path_json_out = "ignore/LDIF/json_out.json"

def number_card(path_vcf_file):
    file  = open(path_vcf_file, 'r').read()
    count = file.count('BEGIN:VCARD\n')
    return count

def make_contact_details(full_name, telephone):
    contact_details={}
    contact_details['nom_complet']=full_name
    contact_details['Telephone']=telephone
    return contact_details



jsondata = []
#contact_details = {}

with open(path_vcf, "r") as ins:

    id_contact = 0
    full_name="default"
    telephone="default"
    telephone2="default"
    for line in ins:

        if 'BEGIN:VCARD\n' in line:
            id_contact += 1

        if 'FN:' in line:

            full_name = str(line.translate({ord('\n'): None}))
            full_name = full_name.replace("FN:","")

        if 'FN;CHARSET=UTF-8;ENCODING=QUOTED-PRINTABLE:' in line:
            full_name = quopri.decodestring(line).decode('utf-8')
            full_name = full_name.replace("FN;CHARSET=UTF-8;ENCODING=QUOTED-PRINTABLE:","")
            full_name = full_name.replace("\n", "")

            if '\u00e9' in full_name:
                full_name = full_name.replace("\u00e9",'e')
                full_name = str(full_name.encode("utf-8"))



        if 'TEL;CELL:' in line:
            telephone = str(line.translate({ord('\n'): None}))
            telephone = telephone.replace("TEL;CELL:","")

        if 'TEL;CELL;PREF:' in line:
            telephone2 = str(line.translate({ord('\n'): None}))
            telephone2 = telephone2.replace("TEL;CELL;PREF:", "")

        if 'END:VCARD' in line:
            if telephone=="default":
                telephone=telephone2
                jsondata.append(make_contact_details(full_name, telephone))
            ###reset value after append
            full_name = "default"
            telephone = "default"
            telephone2 = "default"


    print(jsondata)

def writeInJsonFile(path,data):
    with open(path, 'w') as outfile:
        json.dump(data, outfile)

writeInJsonFile(path_json_out,jsondata)

