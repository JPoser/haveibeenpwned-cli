import requests

class api_interface:
    def __init__(self):
        self.headers = {'user-agent': 'haveibeenpwned-cli',
                        'hibp-api-key': '',
        }

    def check_pwned(self, email):
        endpoint = "https://haveibeenpwned.com/api/v3/breachedaccount/{}".format(email)
        search = requests.get(endpoint, headers=self.headers)
        return search.json()

def __init__():
    api = api_interface()
    print(api.check_pwned("joe.poser@gmail.com"))

__init__()
