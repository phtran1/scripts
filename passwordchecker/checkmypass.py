import requests
import hashlib

def request_api_data(query_char):
    url = "https://api.pwnedpasswords.com/range/" + query_char
    response = requests.get(url)
    
    if response.status_code != 200:
        raise RuntimeError(f"Error fetching: {response.status_code}, check the API and try again.")
    return response

def pwned_api_check(password):
    #Check Password if it exists in API response 
    sha1password = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    return sha1password

pw = pwned_api_check("123")
request_api_data(pw[:5])
