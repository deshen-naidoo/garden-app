"""
Garden Advice Application.
Provides gardening tips based on user-selected seasons and plants.
"""

def get_season_input():
    """
    Prompts the user for a valid season.
    Returns the validated season string.
    """
    while True:
        user_season = input("Enter season (summer/winter): ")
        user_season = user_season.strip().lower()
        if user_season in ["summer", "winter"]:
            return user_season
        print("Invalid. Please enter 'summer' or 'winter'.")

def get_plant_input():
    """
    Prompts the user for a valid plant type.
    Returns the validated plant type string.
    """
    while True:
        user_plant = input("Enter plant type (flower/vegetable): ")
        user_plant = user_plant.strip().lower()
        if user_plant in ["flower", "vegetable"]:
            return user_plant
        print("Invalid. Please enter 'flower' or 'vegetable'.")

def generate_advice(selected_season, selected_plant):
    """
    Generates advice string based on the season and plant type.
    """
    advice_message = ""

    if selected_season == "summer":
        advice_message += "Water regularly and provide shade.\n"
    elif selected_season == "winter":
        advice_message += "Protect plants from frost with covers.\n"
    else:
        advice_message += "No advice for this season.\n"

    if selected_plant == "flower":
        advice_message += "Use fertiliser to encourage blooms."
    elif selected_plant == "vegetable":
        advice_message += "Keep an eye out for pests!"
    else:
        advice_message += "No advice for this type of plant."

    return advice_message

# Execute the functions
season_choice = get_season_input()
plant_choice = get_plant_input()
final_advice = generate_advice(season_choice, plant_choice)
print(final_advice)
