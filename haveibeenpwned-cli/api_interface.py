import requests, configparser
class api_interface:
    def __init__(self):
        self.config = configparser.ConfigParser()
        self.config.read('config.ini')

        self.headers = {'user-agent': 'haveibeenpwned-cli',
                        'hibp-api-key': '{}'.format(self.config.get('default', 'apiKey'))
        }

    def check_pwned(self, email):
        endpoint = "https://haveibeenpwned.com/api/v3/breachedaccount/{}".format(email)
        search = requests.get(endpoint, headers=self.headers)
        return search.json()

    def list_pwned(self, results):
        output = ""

        for result in results:
            output += result.get("Name", "")
            output += "\n"

        return output

