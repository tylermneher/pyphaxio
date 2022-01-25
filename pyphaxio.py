import Credentials
from phaxio import PhaxioApi

# credentials and numbers
api_key = Credentials.API_KEY
api_secret = Credentials.API_SECRET
fax_no_phaxio = Credentials.FAX_NO_PHAXIO
fax_no_tyler = Credentials.FAX_NO_DIRECT

api_url = "https://api.phaxio.com/v2.1"

send_to_no='+1-732-825-7572'
send_to_file='/Volumes/GoogleDrive/My Drive/From_BrotherDevice/20211218222325_001.pdf'


api = PhaxioApi(api_key, api_secret)
response = api.Fax.send(to=send_to_no,
    files=send_to_file)
print(response.data.id)
