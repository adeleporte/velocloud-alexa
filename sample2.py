from __future__ import print_function

from uuid import uuid4

import velocloud
from velocloud.rest import ApiException

# If SSL verification disabled (e.g. in a development environment)
import urllib3
urllib3.disable_warnings()
velocloud.configuration.verify_ssl=False

client = velocloud.ApiClient(host="vco.shwrfr.com")
client.authenticate("super@velocloud.net", "vcadm!n", operator=True)
api = velocloud.AllApi(client)

UNIQ = str(uuid4())

list = []

#
# 3. Provision an Edge
#
print("### PROVISIONING EDGE ###")
params = { "enterpriseId": 1 }
try:
    edges_list = api.enterpriseGetEnterpriseEdges(params)
#    print(edges_list)
except ApiException as e:
    print(e)

for i in edges_list:
    list.append(i.name)


print(", ".join(list))

#print("```List of SDDCs in your organization: \n" + (", ".join(edges_list)) + "```")


