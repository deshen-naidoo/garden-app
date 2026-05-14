# Variables replaced with robust validation loops
while True:
    season = input("Enter season (summer/winter): ")
    season = season.strip().lower()
    if season in ["summer", "winter"]:
        break
    print("Invalid input. Please enter 'summer' or 'winter'.")

while True:
    plant_type = input("Enter plant type (flower/vegetable): ")
    plant_type = plant_type.strip().lower()
    if plant_type in ["flower", "vegetable"]:
        break
    print("Invalid input. Please enter 'flower' or 'vegetable'.")

# Variable to hold gardening advice
advice = ""

if season == "summer":
    advice += "Water your plants regularly and provide some shade.\n"
elif season == "winter":
    advice += "Protect your plants from frost with covers.\n"
else:
    advice += "No advice for this season.\n"

if plant_type == "flower":
    advice += "Use fertiliser to encourage blooms."
elif plant_type == "vegetable":
    advice += "Keep an eye out for pests!"
else:
    advice += "No advice for this type of plant."

print(advice)
