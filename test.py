import requests


def greet(who_to_greet):
    greeting = "Hello, {}".format(who_to_greet)
    return greeting


print("My son! It's my son!")
r = requests.get("https://coreyms.com")

print(r.status_code)
