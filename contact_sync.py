import quopri
import sys
import credentials_project
from ldap3 import Server, Connection


#path_vcf = credentials_project.vcf_file.path
path_vcf = sys.argv[1]



def ldap_connection(Server_url,id_ldap_in,password_ldap_in):
    server = Server(Server_url)
    conn = Connection(server,id_ldap_in,password_ldap_in, auto_bind=True)
    return conn

def number_conversion(number_input):
    zero_number=number_input
    indicatif_number=number_input
    if number_input[0] == "+":
        zero_number = "0" + str(number_input[3:])
    elif number_input[0] == "0":
        indicatif_number = "+33" + str(number_input[1:])
    else:
        #print(str(number_input)+" = invalid number")
        zero_number = number_input
        indicatif_number = number_input
    return zero_number,indicatif_number

def write_into_ldap(connection,firstname,surname,birthday,phonenumber,mail,address):
    """
            Function to write on the target server
            Parameters
            ----------
            connection : object
                The current connection object
            cn : str
                The CN used for the user ( all the path) e.g: cn=test,ou=house,dc=organisation,dc=org
            uid: str
                UID of the specified user
            sn: str
                SN of the specified user
            displayname: str
                displayname of the specified user
            mail: str
                mail of the specified user
            """
    new_surname=''
    if len(surname) > 0:
        new_surname = " "+surname
        sn = surname
    elif len(surname) == 0:
        sn = firstname
    cn = "cn="+firstname +new_surname+",ou=users,"+credentials_project.ldap.baseDN_ldap

    given_name = firstname
    if mail == False:
        mail = firstname+"@"+surname+".com"
    if address == False:
        postal_adress = "postal address"
    if phonenumber == False:
        phonenumber = 0000000000
    user_password = 1234
    description = "birthday: "+birthday
    homephone = birthday
    result = connection.add(cn, 'inetOrgPerson',{'sn': str(sn),'homePhone': str(homephone),'description': str(description),'givenName': str(given_name),'mail': str(mail),'mobile': str(phonenumber),'postalAddress': str(postal_adress),'userPassword': str(user_password)})
    if not result:
        print("This user might already exist or the full path is not correct")
    return result

def check_number_already_present(connection,phone,BaseDN_in):
    return_result = False
    zero_number,indicatif_number= number_conversion(phone)
    if(connection.search('ou=users,'+str(BaseDN_in), '(&(mobile='+zero_number+'))', attributes=['cn']))or(connection.search('ou=users,'+str(BaseDN_in), '(&(mobile='+indicatif_number+'))', attributes=['cn'])):
        return_result = True
    return return_result

def number_card(path_vcf_file):
    file  = open(path_vcf_file, 'r').read()
    count = file.count('BEGIN:VCARD\n')
    return count

def number_present(dict,number):
    return_value = False
    for value in dict.values():
        if value == number:
            return_value = True
        else:
            return_value = False
    return return_value


connection_ldap = ldap_connection(credentials_project.ldap.server_ldap,credentials_project.ldap.id_ldap,credentials_project.ldap.password_ldap)

with open(path_vcf, "r") as ins:

    id_contact = 0
    full_name="default"
    surname = ""
    email="default"
    birthday="1970-01-01"
    telephone="default"

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

            if '\u00e8' in full_name:
                full_name = full_name.replace("\u00e8", 'e')

            if '\u00ea' in full_name:
                full_name = full_name.replace("\u00ea", 'e')

            if '\u00eb' in full_name:
                full_name = full_name.replace("\u00eb", 'e')

        if 'TEL;CELL:' in line:
            telephone = str(line.translate({ord('\n'): None}))
            telephone = telephone.replace("TEL;CELL:","")

        if 'TEL;TYPE=CELL,PREF:' in line:
            telephone = str(line.translate({ord('\n'): None}))
            telephone = telephone.replace("TEL;TYPE=CELL,PREF:", "")

        if 'TEL;CELL;PREF:' in line:
            telephone = str(line.translate({ord('\n'): None}))
            telephone = telephone.replace("TEL;CELL;PREF:", "")

        if 'TEL;CELL,PREF:' in line:
            telephone = str(line.translate({ord('\n'): None}))
            telephone = telephone.replace("TEL;CELL,PREF:", "")

        if 'TEL;TYPE=VOICE,PREF:' in line:
            telephone = str(line.translate({ord('\n'): None}))
            telephone = telephone.replace("TEL;TYPE=VOICE,PREF:", "")

        if 'TEL;TYPE=CELL:' in line:
            telephone = str(line.translate({ord('\n'): None}))
            telephone = telephone.replace("TEL;TYPE=CELL:", "")

        if 'TEL;TYPE=PREF:' in line:
            telephone = str(line.translate({ord('\n'): None}))
            telephone = telephone.replace("TEL;TYPE=PREF:", "")

        if 'EMAIL;TYPE=PREF:' in line:
            email = str(line.translate({ord('\n'): None}))
            email = email.replace("EMAIL;TYPE=PREF:", "")

        if 'BDAY:' in line:
            birthday = str(line.translate({ord('\n'): None}))
            birthday = birthday.replace("BDAY:", "")



        if 'END:VCARD' in line:
            if full_name!="default" and telephone != "default":
                if not(check_number_already_present(connection_ldap, telephone, credentials_project.ldap.baseDN_ldap)):
                    print("--------------------")
                    print(str(full_name)+" : "+str(telephone) + " non présent")
                    firstname = full_name.split()[0]
                    if (len(full_name.split())) == 1:
                        surname = ""
                    if (len(full_name.split()))>1:
                        surname = full_name.split()[1]
                    if (len(full_name.split())) > 2:
                        surname = surname+" "+full_name.split()[2]
                    if (len(full_name.split())) > 3:
                        surname = surname+"_"+full_name.split()[3]

                    print(write_into_ldap(connection_ldap,firstname,surname,birthday,telephone,email,address=False))
                else:
                    #print(str(full_name)+" : "+str(telephone) + " deja présent")
                    blank = 0


            ###reset value after append
            full_name = "default"
            telephone = "default"
            email = "default"
            birthday = "default"
            surname = "default"

