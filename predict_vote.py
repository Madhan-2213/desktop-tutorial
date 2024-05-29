import random

def cast_votes(voter_list, candidates):
    votes = {}
    for voter in voter_list:
        vote = random.choice(candidates)  
        if vote in votes:
            votes[vote].append(voter)
        else:
            votes[vote] = [voter]
    return votes

def determine_winner_and_runner(votes):
    vote_counts = {candidate: len(voters) for candidate, voters in votes.items()}
    sorted_candidates = sorted(vote_counts.items(), key=lambda item: item[1], reverse=True)
    
    winner = sorted_candidates[0][0]
    runner_up = sorted_candidates[1][0]
    
    return winner, runner_up

def main():
    voter_list = ['Voter1', 'Voter2', 'Voter3', 'Voter4', 'Voter5', 
                  'Voter6', 'Voter7', 'Voter8', 'Voter9', 'Voter10']
    candidates = ['A', 'B', 'C']
    
    
    votes = cast_votes(voter_list, candidates)
    
    
    winner, runner_up = determine_winner_and_runner(votes)
    
    
    print("Votes:", votes)
    print("Winner:", winner, "with voters:", votes[winner])
    print("Runner-Up:", runner_up, "with voters:", votes[runner_up])

if __name__ == "__main__":
    main()
