from bs4 import BeautifulSoup  # type: ignore
import requests  # type: ignore
import pandas as pd
page = requests.get("https://www.scrapethissite.com/pages/simple/")
soup = BeautifulSoup(page.content , "lxml")
countries_name = []
countries_Capital = []
countries_Population = []
countries_Area = []
counties_details = soup.find_all("div" , class_ = "col-md-4 country")
for country in counties_details :
    # get country name 
    countries_name.append(country.find("h3" , class_ = "country-name").text.strip())
    # get country Capital 
    countries_Capital.append(country.find("span" , class_ = "country-capital").text.strip())
    # get country Population and convert it to int
    countries_Population.append(int(country.find("span" , class_ = "country-population").text.strip()))
    # get country area and convert it to float
    countries_Area.append(float(country.find("span" , class_ = "country-area").text.strip()))

# making dict to convert it to df(dataframe)
my_dict = {"countries_name" : countries_name ,
        "counties-capital" : countries_Capital ,
        "countries_Population" : countries_Population ,
        "countries_Area" : countries_Area }

# making the df 
df = pd.DataFrame(my_dict)
df.to_csv("Countries_details.csv" ,index= False)
print("Saved to Countries_details.csv")


