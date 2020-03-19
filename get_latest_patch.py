#!/usr/bin/env python3
from xmlrpc.client import ServerProxy
import os, ssl

MANAGER_URL = "https://YOUR_SUMA_HOSTNAME/rpc/api"
MANAGER_LOGIN = "YOUR_ADMIN_USERNAME"
MANAGER_PASSWORD = "YOUR_ADMIN_PASSWORD"

# skip ssl verification
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# create suma client instance
suma = ServerProxy(MANAGER_URL, context=ctx)

# authenticate to obtain session key
sessionKey = suma.auth.login(MANAGER_LOGIN, MANAGER_PASSWORD)

# list all available channels in SUSE Manager
print(suma.channel.listAllChannels(sessionKey))

# list all advisories for rhel8
channelLabel = 'rhel8-x86_64-appstream'
print(suma.channel.software.listErrata(sessionKey, channelLabel))

# list affected systems for a given advisory
advisory = 'RHBA-2019:3337'
print(suma.errata.listAffectedSystems(sessionKey, advisory))
# sample output: 
# [{'name': 'rhel1.suse.lab', 'id': 1000010006, 'system_id': 1000010006, 'system_name': 'rhel1.suse.lab'}]

# logout
suma.auth.logout(sessionKey)
