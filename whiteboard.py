# Our football team has finished the championship.

# Our team's match results are recorded in a collection of strings. Each match is represented by a string in the format "x:y", where x is our team's score and y is our opponents score.

# For example: ["3:1", "2:2", "0:1", ...]

# Points are awarded for each match as follows:

# if x > y: 3 points (win)
# if x < y: 0 points (loss)
# if x = y: 1 point (tie)
# We need to write a function that takes this collection and returns the number of points our team (x) got in the championship by the rules given above.

# Notes:

# our team always plays 10 matches in the championship

def solution(points):
    total_points = 0
    for point in points:
        game = points.split(":")
        team_1 = int(game[0])
        team_2 = int(game[-1])
        if team_1 >team_2:
            total_points += 3
        elif team_1 == team_2:
            total_points += 1
    return total_points

def solution(arr):
    x-0
    for a in arr:
        c,d - a.split(':')
        e - int(c)
        f - int(d)
        if e > f:
            x+=3
        elif e< f:
            x+=0
        else:
            x+= 0
            