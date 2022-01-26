import sys
import os
import configargparse
import json
import Credentials
from phaxio import PhaxioApi
from phaxio import swagger_client
import datetime

# credentials and numbers
api_key = Credentials.API_KEY
api_secret = Credentials.API_SECRET
fax_no_phaxio = Credentials.FAX_NO_PHAXIO
fax_no_tyler = Credentials.FAX_NO_DIRECT

# Define function to get fax status
def faxStatus(fax_id):
    phaxio_api = PhaxioApi(api_key, api_secret)
    fax_status = phaxio_api.Fax.status(fax_id)
    ct = str(datetime.datetime.now())
    # fax_status_file = open(ct+"_"+fax_id+"_status.txt", 'w+')
    #with open('status.json', 'w', encoding='utf-8') as f:
        #json.dump(fax_status, f, ensure_ascii=False, indent=4)
    print(fax_status)
    


fax_id = input("Phaxio fax_id # to check status:  ")

faxStatus(fax_id)

