def get_strength_levels():
    # Collect the strength levels in a list
    strength_levels = []
    for i in range(12):  # We need exactly 12 inputs
        try:
            strength = int(input())
            # Validate the strength level range
            if strength < 1 or strength > 200:
                print("INVALID INPUT")
                return None
            strength_levels.append(strength)
        except ValueError:
            print("INVALID INPUT")
            return None
    return strength_levels

def calculate_averages(strength_levels):
    # Calculate the average strength for each trainee across 3 rounds
    averages = []
    for trainee_index in range(4):
        # Calculate sum of three rounds for the trainee
        total_strength = sum(strength_levels[trainee_index + round * 4] for round in range(3))
        average_strength = round(total_strength / 3)  # Round to the nearest integer
        averages.append(average_strength)
    return averages

def display_strength_by_round(strength_levels):
    # Display the strength levels for each round and trainee
    print("Round 1")
    for i in range(4):
        print(f"  Strength level of Trainee {i + 1}: {strength_levels[i]}")
    
    print("Round 2")
    for i in range(4):
        print(f"  Strength level of Trainee {i + 1}: {strength_levels[i + 4]}")
    
    print("Round 3")
    for i in range(4):
        print(f"  Strength level of Trainee {i + 1}: {strength_levels[i + 8]}")

def find_strongest_trainees(averages):
    # Find the maximum average strength
    max_average = max(averages)
    
    # Check if all trainees are unfit
    if max_average < 100:
        print("All trainees are unfit")
        return
    
    # Identify and display all trainees with the highest average
    for i, avg in enumerate(averages):
        if avg == max_average:
            print(f"Trainee Number : {i + 1}")

# Main program execution
strength_levels = get_strength_levels()
if strength_levels:
    # Display strength levels by round
    display_strength_by_round(strength_levels)
    
    # Calculate the averages for each trainee
    averages = calculate_averages(strength_levels)
    
    # Find and display the strongest trainee(s)
    find_strongest_trainees(averages)
    
