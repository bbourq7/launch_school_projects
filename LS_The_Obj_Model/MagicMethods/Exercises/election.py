class Candidate:

    def __init__(self, name):
        self.name = name
        self.votes = 0

    def __iadd__(self, other):
        if not isinstance(other, int):
            return NotImplemented
        
        self.votes += 1
        return self
    
class Election():

    def __init__(self, candidates):
        self.candidates = candidates
        

    def results(self):
        max_votes = 0
        vote_count = 0
        winner = None

        for candidate in self.candidates:
            candidate += candidate.votes
            vote_count += candidate.votes
            if candidate.votes > max_votes:
                max_votes = candidate.votes
                winner = candidate.name

        for candidate in self.candidates:
            name = candidate.name
            votes = candidate.votes
            print(f'{name}: {votes} votes')

        percent = 100 * (max_votes / vote_count)
        print()
        print(f'{winner} won: {percent}% of votes')
