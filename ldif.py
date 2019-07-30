import csv

f=open("out.ldif", "a+")

def writeFile(text):
    f.write(text+"\n")

#writeFile("e")

with open('ldif.csv', newline='') as csvfile:
     reader = csv.DictReader(csvfile) #, delimiter=',', quotechar='|'
     for row in reader:
        id=row['ID']
        Display_name=row['Display Name']
        gidnumber=int(id)+100
        givenname=row['First Name']
        sn=givenname
        mail=row['E-mail Address']
        mobile=row['Mobile Phone']
        address=row['Home Street']
        birthday=row['Birthday']

         #line 1
        writeFile("# Entry "+id+": cn="+Display_name+",dc=domain,dc=fr")
        writeFile("dn: cn="+Display_name+",dc=domain,dc=fr")
        writeFile("cn: "+Display_name)
        writeFile("description: birthday: "+birthday)
        writeFile("gidnumber: "+str(gidnumber))
        writeFile("givenname: "+givenname)
        writeFile("homedirectory: /home/users/"+str(gidnumber))
        writeFile("mail: "+mail)
        writeFile("mobile: "+mobile)
        writeFile("objectclass: inetOrgPerson")
        writeFile("objectclass: posixAccount")
        writeFile("objectclass: top")
        writeFile("postaladdress: "+address)
        writeFile("sn: "+sn)
        writeFile("uid: "+sn)
        writeFile("uidnumber: "+str(gidnumber))
        writeFile("userpassword: {MD5}gnzLDuqKcGxMNKFokfhOew==\n\n")
