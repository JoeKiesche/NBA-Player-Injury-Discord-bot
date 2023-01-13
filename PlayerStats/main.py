import requests 
from bs4 import BeautifulSoup
from Team import Team

#Fetch URl using beautiful soup
url = "https://rotogrinders.com/courtiq?"

#Parse the HTML using beautiful soup
response = requests.get(url)

#Fetch the team names and IDs
soup = BeautifulSoup(response.text, 'html.parser')

teams = []

teamNames = soup.find("select", attrs={'id': 'team_id'}).find_all("option")

for team in teamNames:
    if team.text != "All Teams":
        teams.append(Team(team.text, team['value']))

#Remove the first element as it is not a team
teams.pop(0)

#Print the team names and IDs
for team in teams:
    print(team)