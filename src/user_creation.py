'''
{'objectClass': [b'top', b'person', b'organizationalPerson', b'user'], 
'cn': [b'newuser3 newuser3'], 'sn': [b'newuser3'], 'givenName': [b'newuser3'], 
'distinguishedName': [b'CN=newuser3 newuser3,OU=nested,OU=newusers2,DC=localdomain,DC=com'], 
'instanceType': [b'4'], 'whenCreated': [b'20250226164320.0Z'], 'whenChanged': [b'20250325153042.0Z'], 
'displayName': [b'newuser3 newuser3'], 'uSNCreated': [b'25635'], 'uSNChanged': [b'90162'], 
'name': [b'newuser3 newuser3'], 'objectGUID': [b'\x1eFV\x15\xdeH!H\xa4\xbab\xb0\xdf`6:'], 
'userAccountControl': [b'66048'], 'badPwdCount': [b'0'], 'codePage': [b'0'], 'countryCode': [b'0'], 
'homeDirectory': [b'/home/newuser3'], 'badPasswordTime': [b'0'], 'lastLogoff': [b'0'], 
'lastLogon': [b'0'], 'pwdLastSet': [b'133219034003250783'], 'primaryGroupID': [b'513'], 
'objectSid': [b'\x01\x05\x00\x00\x00\x00\x00\x05\x15\x00\x00\x00\x90\xf2\x15\xd3\xea\xa0Jz1\xd7\xeeR[\x04\x00\x00'], 
'accountExpires': [b'9225372036854775807'], 'logonCount': [b'0'], 'sAMAccountName': [b'newuser3'], 
'sAMAccountType': [b'805306368'], 'userPrincipalName': [b'newuser3@localdomain.com'], 
'objectCategory': [b'CN=Person,CN=Schema,CN=Configuration,DC=localdomain,DC=com'], 
'dSCorePropagationData': [b'20250226191929.0Z', b'20250226191925.0Z', b'20250226164320.0Z', b'16010101000000.0Z'], 
'uidNumber': [b'50001'], 'gidNumber': [b'70000'], 'gecos': [b'newuser3 newuser3'], 
'loginShell': [b'/bin/mdmshell']}
'''

import ldap
from ldap import modlist

server = 'ldap://vagrant-2012-r2.localdomain.com'
connect = ldap.initialize(server)
connect.set_option(ldap.OPT_REFERRALS, 0)
user = 'syncuser@localdomain.com'
passwd = 'Vyq59[Tc/?6k4bT2]%aE'
connect.simple_bind_s(user, passwd)

for number in range(1,2500):
    username = f"users1ou{number}"
    dn = f"CN={username} {username},OU=users1,DC=localdomain,DC=com"
    attrs = {}
    attrs['objectClass'] = [b'top', b'person', b'organizationalPerson', b'user']
    attrs['cn'] = f"{username} {username}".encode('utf-8')
    attrs['sn'] = f"{username}".encode('utf-8')
    attrs['givenName'] = f"{username}".encode('utf-8')
    attrs['displayName'] = f"{username}".encode('utf-8')
    attrs['name'] = f"{username}".encode('utf-8')
    attrs['sAMAccountName'] = f"{username}".encode('utf-8')
    attrs['userPrincipalName'] = f"{username}@localdomain.com".encode('utf-8')
    attrs['userAccountControl'] = [b'544']

    ldif = modlist.addModlist(attrs)
    connect.add_s(dn, ldif)
