
class player:
    name = ""
    position = ""
    status = 0 #1 = playing, 0 = not playing

    def __init__(self, name, position, status):
        self.name = name
        self.position = position
        self.status = status #1 = playing, 0 = not playing

    def get_name(self):
        return self.name

    def get_position(self):
        return self.position

    def get_status(self):   
        return self.status

    def __str__(self) -> str:
        return("Name- " + str(self.name) + "\nPosition- " + str(self.position) + "\nStatus- " + str("Playing" if self.status == 1 else "Not Playing") + "\n")