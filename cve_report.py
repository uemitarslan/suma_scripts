#!/usr/bin/env python3
from xmlrpc.client import ServerProxy
import argparse
import datetime
import time

MANAGER_URL = "$SUMA_URL"
MANAGER_LOGIN = "$SUMA_Login"
MANAGER_PASSWORD = "$YOUR_PASSWORD_HERE"

my_list = [] # list with system id's unfiltered
my_list2 = [] # filtered system id's

client = ServerProxy(MANAGER_URL)
master = ServerProxy(MANAGER_URL)
key = client.auth.login(MANAGER_LOGIN, MANAGER_PASSWORD)


print("Please provide a CVE-ID:")
cve_input = input()

#cve_list = (client.audit.listSystemsByPatchStatus(key,"CVE-2021-4156"))
cve_list = (client.audit.listSystemsByPatchStatus(key,cve_input))
# Array with patch information
# [{'system_id': 1000010042, 'patch_status': 'AFFECTED_PATCH_INAPPLICABLE', 'channel_labels': ['sles12-sp5-updates-x86_64'],


counter=0

while counter < len(cve_list):
    id_to_name = (cve_list[counter]["system_id"]) # Generate system id and write to var
# {'name': 'sle12sp4.suse.de', 'id': 1000010042, 'last_checkin': <DateTime '20220127T03:00:05' at 0x7f9889d7c470>}
 #   print(client.system.getName(key,id_to_name)) # print system names derived from system id
    my_list.append( (client.system.getName(key,id_to_name)) )
    #print(my_list[counter]['name'])
    my_list2.append( (my_list[counter]['name']) )
    counter = counter + 1

counter=0
while counter < len(cve_list):
     cve_list[counter]["system_id"]=(my_list2[counter])
     counter = counter + 1

### Replace old key "system_id" with "system_name"

counter=0
while counter < len(cve_list):
     print(cve_list[counter])
     counter = counter + 1
     
print("")
print("AFFECTED_PATCH_INAPPLICABLE - Affected, patch available in unassigned channel")
print("AFFECTED_PATCH_APPLICABLE - Affected, patch available in assigned channel")
print("NOT_AFFECTED - Not affected")
print("PATCHED - Patched")
