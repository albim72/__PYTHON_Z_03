class FootballTeamIterator:
    def __init__(self,members):
        self.members = members
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.members):
            val = self.members[self.index]
            self.index += 1
            return val
        else:
            raise StopIteration("przkroczona liczba osób uprawnionych!")

class FootballTeam:

    def __init__(self,members):
        self.members = members

    def __iter__(self):
        return FootballTeamIterator(self.members)

def main():
    members = [f'player{str(x)}' for x in range(1,23)]
    members = members + ['trener1A','trener2A','trener1B','trener2B']
    team  = FootballTeam(members)
    team_it = iter(team)
    while True:
        print(next(team_it))

if __name__ == '__main__':
    try:
        main()
    except StopIteration as s:
        print(s)
