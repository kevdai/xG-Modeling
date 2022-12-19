import numpy as np

# Function to calculate the xG for a shot using a Markov chain model
def calc_xg(shot_distance, shot_angle, shot_type, model, tactical_style):
  # Assign initial state based on shot distance and angle
  if shot_distance < 20 and abs(shot_angle) < 15:
    state = "high_prob"
  elif shot_distance < 30:
    state = "medium_prob"
  elif shot_distance < 40:
    state = "low_prob"
  else:
    state = "very_low_prob"
  
  # Adjust initial state based on shot type
  if shot_type == "header":
    state += "_header"
  elif shot_type == "volley":
    state += "_volley"
  elif shot_type == "penalty":
    state = "penalty"
  
  # Initialize xG to 0
  xG = 0
  
  # Loop until a goal is scored or the attack ends
  while state != "goal" and state != "end":
    # Look up the transition probabilities for the current state
    transitions = model[state]
    
    # Adjust the transition probabilities based on tactical style
    if tactical_style == "attacking":
      # Increase the probability of taking a shot
      transitions["shot_taken"] *= 1.2
      # Decrease the probability of losing possession
      transitions["lost_possession"] *= 0.8
    elif tactical_style == "defensive":
      # Decrease the probability of taking a shot
      transitions["shot_taken"] *= 0.8
      # Increase the probability of losing possession
      transitions["lost_possession"] *= 1.2
    
    # Choose the next state based on the transition probabilities
    next_state = np.random.choice(list(transitions.keys()), p=list(transitions.values()))
    
    # Update xG based on the xG value for the current state
    xG += model[state]["xG"]
    
    # Update the current state
    state = next_state
  
  # Return the final xG value
  return xG

# Function to calculate the xG for a team
def calc_team_xg(shots, model, tactical_style):
  team_xg = 0
  for shot in shots:
    shot_distance = shot[0]
    shot_angle = shot[1]
    shot_type = shot[2]
    team_xg += calc_xg(shot_distance, shot_angle, shot_type, model, tactical_style)
  return team_xg

# Example Markov chain model
model = {
  "high_prob": {
    "goal": 0.3,
    "medium_prob": 0.4,
    "low_prob": 0.2,
    "very_low_prob": 0.1,
    "shot_taken": 0.0,
    "lost_possession": 0.0,
    "end": 0.0,
    "
