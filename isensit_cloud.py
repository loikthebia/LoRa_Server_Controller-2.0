import urllib3.contrib.pyopenssl
import requests
import json
from config import Config
import socket
import sys
import signal
from time import sleep
from requests.packages.urllib3.exceptions import InsecureRequestWarning

# from requests.packages.urllib3.exceptions import HTTPError as BaseHTTPError

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

# disable SSLV3 certificate check , aws does not support it
urllib3.contrib.pyopenssl.inject_into_urllib3()


# Register an handler for the timeout
def handler(signum, frame):
    print("Function timeout was called!")
    raise Exception("func timeout")


class ISensitCloud:

    def __init__(self):
        self.config_data = Config()
        self.config_data.init_json_config_data()
        self.post_counter = 0
        # Register the signal function handler
        signal.signal(signal.SIGALRM, handler)

    def get_gateway_data(self):

        try:
            self.config_data.get_get_url() is not None
        except TypeError:
            print("Is a Null value")
            return False

        else:
            try:
                r = requests.get(self.config_data.get_get_url(), timeout=3, verify=False)

            except requests.exceptions.ConnectTimeout as e:
                print("Server took too long to respond!", str(e))
                return False

            except requests.exceptions.ConnectionError as e:
                print("These aren't the domains we're looking for. Error: ", str(e))
                return False

            else:
                return r.text

    def post_data(self, post_data):

        signal.alarm(1)
        # sleep(4)
        try:
            self.config_data.get_post_url() is not None
        except TypeError:
            print("Post URL is a Null value")
            return False

        try:
            json_data = json.dumps(post_data)
        except ValueError:  # includes simplejson.decoder.JSONDecodeError
            print('Decoding JSON has failed')
            return False

        except TypeError:
            print("Not a valid json data")
            return False

        else:
            try:
                r = requests.post(self.config_data.get_post_url(), json_data, timeout=2, verify=False)

                errorFlag = True if "errorMessage" in r.json() else False
                self.post_counter += 1
                print("Post Counter: ", self.post_counter)
                print("Data: ", r.json())
                if errorFlag:
                    print("Error recieved: ", r.json())
                    return False

                if r.json() == "SUCCESS":
                    return r.json()
                else:
                    return False

            except requests.exceptions.RequestException as e:  # This is the correct syntax
                print(e)
                sys.exit(1)

            except requests.exceptions.SSLError as e:
                print("That domain looks super sketchy. Error : ", str(e))
                return False

            except requests.HTTPError as e:
                print("HTTP Error ", str(e))
                return False

            except socket.gaierror:
                print("Unexpected error:", sys.exc_info()[0])
                return False

            except requests.exceptions.ConnectionError as e:
                print("Domain error , ", str(e))
                return False

            except Exception as e:
                print("Post error, reason: ", str(e))
                return False

            else:
                return r.text

    def get_data():
        
        signal.alarm(1)
        # sleep(4)
        try:
            self.config_data.get_get_url() is not None
        except TypeError:
            print("Post URL is a Null value")
            return False

        try:
                r = requests.post(self.config_data.get_get_url(), json_data, timeout=2, verify=False)

                errorFlag = True if "errorMessage" in r.json() else False
                self.post_counter += 1
                print("Post Counter: ", self.post_counter)
                print("Data: ", r.json())
                if errorFlag:
                    print("Error recieved: ", r.json())
                    return False

                if r.json() == "SUCCESS":
                    return r.json()
                else:
                    return False

            except requests.exceptions.RequestException as e:  # This is the correct syntax
                print(e)
                sys.exit(1)

            except requests.exceptions.SSLError as e:
                print("That domain looks super sketchy. Error : ", str(e))
                return False

            except requests.HTTPError as e:
                print("HTTP Error ", str(e))
                return False

            except socket.gaierror:
                print("Unexpected error:", sys.exc_info()[0])
                return False

            except requests.exceptions.ConnectionError as e:
                print("Domain error , ", str(e))
                return False

            except Exception as e:
                print("Post error, reason: ", str(e))
                return False

            else:
                return r.text