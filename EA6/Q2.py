# write a python / R function to simulate the Goat-car door open problem (Monty Hall problem) 100 times. write the conclusion and what do you think?
import random

def monthly_hall(num_simulations=100):
    wins_switching_door = 0
    wins_by_staying = 0
    for i in range(num_simulations):
        # Randomly select a car door
        car_door = random.randint(1, 3)
        
        # Randomly select a player's initial guess
        guess = random.randint(1, 3)
        
        # Randomly select a goat door
        goat_door = random.choice([1, 2, 3])
        while goat_door == guess or goat_door == car_door:
            goat_door = random.choice([1, 2, 3])
        
        # Player switches to the other door
        if guess != car_door:
            wins_switching_door += 1
        
        # Player stays with their original guess
        if guess == car_door:
            wins_by_staying += 1
    return wins_switching_door, wins_by_staying

# Run the simulation 100 times
wins_switching_door, wins_by_staying = monthly_hall()

# Print the results
print("Wins switching door:", wins_switching_door)
print("Wins staying with original door:", wins_by_staying)

print("Conclusion:")
print("Running these functions will show a win rate around 66.67% for switching doors and 33.33% for staying on the same door. This reinforces the counterintuitive nature of the Monty Hall problem – switching doors nearly doubles your chance of winning!")

print("My thoughts:")
print("The Monty Hall problem is a fascinating example of how seemingly logical intuition can be wrong when dealing with probability. By revealing a goat behind one of the unchosen doors, Monty provides valuable information that allows you to effectively choose the remaining door with a higher chance of having the car. It's a great example of the power of conditional probability.")