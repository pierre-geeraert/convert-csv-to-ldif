# import class and constants
import credentials_project
from ldap3 import Server, Connection, ALL, MODIFY_REPLACE,SUBTREE

total_entries = 0
# define the server
s = Server(credentials_project.ldap.server_ldap, get_info=ALL)  # define an unsecure LDAP server, requesting info on DSE and schema

# define the connection
c = Connection(s, user=credentials_project.ldap.id_ldap, password=credentials_project.ldap.password_ldap)
c.bind()

c.search(search_base = 'ou=users,'+credentials_project.ldap.baseDN_ldap,
         search_filter = '(objectClass=inetOrgPerson)',
         search_scope = SUBTREE,
         attributes = ['cn', 'givenName','sn','mobile','postalAddress','mail','description'])
total_entries += len(c.response)
#print(total_entries)
print("--------------------------------------------------------------------------")
for entry in c.response:
    print(entry)
    print("name")
    print(entry['attributes']['givenName'][0])
    new_name = input(entry['attributes']['givenName'][0])
    print(new_name)
    if not(new_name):
        new_name = entry['attributes']['givenName'][0]
    print("sn")
    new_sn = input(entry['attributes']['sn'][0])
    print(new_sn)
    if not(new_sn):
        new_sn = entry['attributes']['sn'][0]
    print("birthday")
    new_birthday = input(entry['attributes']['description'][0])
    print(new_birthday)
    if not(new_birthday):
        new_birthday = entry['attributes']['description'][0]
    print("mail")
    new_mail = input(entry['attributes']['mail'][0])
    print(new_mail)
    if not(new_mail):
        new_mail = entry['attributes']['mail'][0]
    print("mobile")
    new_mobile = input(entry['attributes']['mobile'][0])
    print(new_mobile)
    if not(new_mobile):
        new_mobile = entry['attributes']['mobile'][0]

    print("poste")
    new_postalAddress = input(entry['attributes']['postalAddress'][0])
    print(new_postalAddress)
    if not(new_postalAddress):
        new_postalAddress = str(entry['attributes']['postalAddress'][0])

    # perform the Modify operation
    c.modify(entry['dn'],
             {'givenName': [(MODIFY_REPLACE, [new_name])],
              'sn': [(MODIFY_REPLACE, [new_sn])],
              'description': [(MODIFY_REPLACE, [new_birthday])],
              'mail': [(MODIFY_REPLACE, [new_mail])],
              'mobile': [(MODIFY_REPLACE, [new_mobile])],
              'postalAddress': [(MODIFY_REPLACE, [new_postalAddress])]
              })
    #print(c.result)

# close the connection
c.unbind()
