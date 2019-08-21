import ldap3
from ldap3 import Server, Connection, ALL



### usefull help: https://ldap3.readthedocs.io/tutorial.html
conn = Connection(server, 'cn=admin,dc=geeraert,dc=eu', '', auto_bind=True)
print(conn.extend.standard.who_am_i())
conn.search('ou=cesi,dc=geeraert,dc=eu', '(objectclass=person)')
print(conn.entries)