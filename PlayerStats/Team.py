
class Team:
    name = ""
    teamID = 0

    def __init__(self, name, teamID):
        self.name = name
        self.teamID = teamID

    def getName(self):
        return self.name

    def getTeamID(self):
        return self.teamID

    def __str__(self) -> str:
        return("Team- " + self.name + " ID- " + str(self.teamID))

