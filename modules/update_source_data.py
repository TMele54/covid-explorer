import urllib.request

url = "https://covid.ourworldindata.org/data/owid-covid-data.json"

location = "C:/Users/tonym/OneDrive/APPS/covid_review/data/source/owid-covid-data.json"

print("download start!")

filename, headers = urllib.request.urlretrieve(url, filename=location)

print("download complete!")
print("download file location: ", filename)
print("download headers: ", headers)
