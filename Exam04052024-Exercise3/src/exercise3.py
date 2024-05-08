# Write your solution to exercise 3 here
def read_points():   
    tuple_for_game = []
    try:    
        with open ("statistics.txt") as file:
            for line in file:
                    line_str = line.replace("\n","")
                    parts = line_str.split(":")
                    team_name = parts[0]
                    points = parts[1].split("-")
                    if points:
                        wins = int(points[0]) * 3
                        losses = int(points[1]) * 0
                        ties = int(points[2]) * 1
                        sum_of_points = wins + losses + ties
                        tuple_for_game.append((team_name, sum_of_points))
            return tuple_for_game        
    except ValueError:
            print ("Could not convert your string or float value to integer. Please check your file and use integer-convertible values.")                 

print(read_points())                           


      

       

