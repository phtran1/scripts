import requests
import hashlib
import sys
import os
from dotenv import load_dotenv
load_dotenv()

def request_api_data(query_char):
    url = "https://api.pwnedpasswords.com/range/" + query_char
    response = requests.get(url)
    
    if response.status_code != 200:
        raise RuntimeError(f"Error fetching: {response.status_code}, check the API and try again.")
    return response

def get_pw_leaks_count(hashes, hash_to_check):
    # Matches tail with returned hashes to get the password leak count
    hashes = (line.split(':') for line in hashes.text.splitlines())
    for h, count in hashes:
        if h == hash_to_check:
            return count
    return 0
        
def pwned_api_check(password):
    #Check Password if it exists in API response 
    sha1password = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    first5_char, tail = sha1password[:5], sha1password[5:]
    response = request_api_data(first5_char)
    return get_pw_leaks_count(response, tail)

def main():
    raw_pw = os.getenv("secret_pw", "")

    if not raw_pw:
        print("Password not found or empty .env file")
        return
    
    pw_list = raw_pw.split(',') 

    print(f'Loaded {len(pw_list)} passwords to check safely.')

    # Returns how many times a password has been leaked and replaces password with * for output
    for pw in pw_list:
        count = pwned_api_check(pw)
        hidden_pw = '*' * len(pw)
        print(f'Checking: {hidden_pw}')
        if count:
            print(f'{hidden_pw} was found {count} times... you should probably change your password.')
        else:
            print(f'{hidden_pw} was NOT leaked you are safe.')
        print('------------------------------')

if __name__ == '__main__':
    main()
