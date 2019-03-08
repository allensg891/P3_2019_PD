####
# Each team's file must define four tokens:
#     team_name: a string
#     strategy_name: a string
#     strategy_description: a string
#     move: A function that returns 'c' or 'b'
####

team_name = 'YoteBoat9' # Only 10 chars displayed.
strategy_name = 'BigBrain'
strategy_description = 'Always betray'
    
def move(my_history, their_history, my_score, their_score):
    ''' Arguments accepted: my_history, their_history are strings.
    my_score, their_score are ints.
    
    Make my move.
    Returns 'c' or 'b'. 
    '''

    # my_history: a string with one letter (c or b) per round that has been played with this opponent.
    # their_history: a string of the same length as history, possibly empty. 
    # The first round between these two players is my_history[0] and their_history[0].
    # The most recent round is my_history[-1] and their_history[-1].
    
    # Analyze my_history and their_history and/or my_score and their_score.
    # Decide whether to return 'c' or 'b'.
    
    #strategy 1:
    #return 'b'
           
    #strategy 2:
    '''if len(my_history)==0 or len(my_history)==1:
        return 'c'
    if len(their_history)>=2:
        if 'bb' in their_history[-2]:
            return 'b'
        if 'bc' in their_history[-2]:
            return 'c'
        if 'cc' in their_history[-2]:
            return 'c'
            '''
    #strategy 3:
    if len(my_history)==0:
        return 'c'
    if len(my_history)>=1:
        return their_history[-1]