import statistics

# Function to calculate the xG for a shot
def calc_xg(shot_distance, shot_angle, shot_type):
  # Assign different xG values based on the shot distance and angle
  if shot_distance < 20 and abs(shot_angle) < 15:
    xG = 0.9
  elif shot_distance < 30:
    xG = 0.7
  elif shot_distance < 40:
    xG = 0.5
  else:
    xG = 0.3
  
  # Adjust xG based on shot type
  if shot_type == "header":
    xG *= 0.8
  elif shot_type == "volley":
    xG *= 0.6
  elif shot_type == "penalty":
    xG = 0.75
  
  return xG

# Function to calculate the xG for a team
def calc_team_xg(shots):
  team_xg = 0
  for shot in shots:
    shot_distance = shot[0]
    shot_angle = shot[1]
    shot_type = shot[2]
    team_xg += calc_xg(shot_distance, shot_angle, shot_type)
  return team_xg

# Example usage
shots_team_1 = [(35, 10, "normal"), (25, -5, "volley"), (12, 0, "header")]
shots_team_2 = [(40, -15, "normal"), (20, 10, "penalty"), (32, 5, "normal")]

xG_team_1 = calc_team_xg(shots_team_1)
xG_team_2 = calc_team_xg(shots_team_2)

print("Team 1 xG:", xG_team_1)
print("Team 2 xG:", xG_team_2)

# Calculate the overall xG for the match
match_xG = xG_team_1 + xG_team_2
print("Match xG:", match_xG)

# Calculate the xG difference between the two teams
xG_diff = xG_team_1 - xG_team_2
print("xG difference:", xG_diff)
