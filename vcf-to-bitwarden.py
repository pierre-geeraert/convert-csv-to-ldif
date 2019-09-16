import csv

f=open("bitwarden.json", "a+")

def writeFile(text):
    f.write(text+"\n")

#writeFile("e")
id=0;
with open('bitwarden.csv', newline='') as csvfile:
     reader = csv.DictReader(csvfile) #, delimiter=',', quotechar='|'
     for row in reader:
        id=id+1
        #id=row['ID']
        Display_name=row['Display Name']
        gidnumber=int(id)+100
        givenname=row['First Name']
        sn=givenname
        mail=row['E-mail Address']
        mobile=row['Mobile Phone']
        address=row['Home Street']
        birthday=row['Birthday']

         #line 1

        writeFile("{")
        writeFile("  \"id\": \"ID"+str(id)+"\",")
        writeFile("  \"organizationId\": \"organization\",")
        writeFile("  \"folderId\": null,")
        writeFile("  \"type\": 4,")
        writeFile("  \"name\": \""+Display_name+"\",")
        writeFile("  \"notes\": null,")
        writeFile("  \"favorite\": false,")
        writeFile("  \"identity\": {")
        writeFile("    \"title\": null,")
        writeFile("    \"firstName\": \""+givenname+"\",")
        writeFile("    \"middleName\": null,")
        writeFile("    \"lastName\": \"\",")
        writeFile("    \"address1\": \"Adresse\",")
        writeFile("    \"address2\": null,")
        writeFile("    \"address3\": null,")
        writeFile("    \"city\": \"City\",")
        writeFile("    \"state\": \"Région\",")
        writeFile("    \"postalCode\": \"PostalCode\",")
        writeFile("    \"country\": \"France\",")
        writeFile("    \"company\": \"company\",")
        writeFile("    \"email\": \""+mail+"\",")
        writeFile("    \"phone\": \""+mobile+"\",")
        writeFile("    \"ssn\": null,")
        writeFile("    \"username\": \""+Display_name+"\",")
        writeFile("    \"passportNumber\": null,")
        writeFile("    \"licenseNumber\": null")
        writeFile("  },")
        writeFile("  \"collectionIds\": [")
        writeFile("    \"collectionIds\"")
        writeFile("  ]")
        writeFile("},")


     csvfile.close()
f.close()
