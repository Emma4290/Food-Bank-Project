import requests

postcode = input("What is your postcode? ")

url = "https://www.givefood.org.uk/api/2/foodbanks/search/?address={}".format(postcode)

response = requests.get(url)
response.raise_for_status()

data = response.json()

for name in data:
    print("\n**********\n")
    print("Name:", name["name"].upper())
    print("-----")
    print("Address:\n", name["address"])
    print("-----")
    print("Needs:\n", name["needs"]["needs"])
    print("-----")
    print("Excess:\n", name["needs"]["excess"])
    print("-----")
    print("Website:\n", name["urls"]["html"])
