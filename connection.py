import ldap3
from ldap3 import Server, Connection, ALL


if __name__ == "__main__":
    ldap_server="geeraert.eu"
    username = "cn=admin,dc=geeraert,dc=eu"
    password= "dinner_sl@v3"
    # the following is the user_dn format provided by the ldap server
    user_dn = "uid="+username+",ou=someou,dc=somedc,dc=local"
    # adjust this to your base dn for searching
    base_dn = "dc=somedc,dc=local"
    connect = ldap3.open(ldap_server)
    search_filter = "uid="+username
    try:
        #if authentication successful, get the full user data
        connect.bind_s(user_dn,password)
        result = connect.search_s(base_dn,ldap3.SCOPE_SUBTREE,search_filter)
        # return all user data results
        connect.unbind_s()
        print(result)
    except ldap3.LDAPError:
        connect.unbind_s()
print("authentication error")