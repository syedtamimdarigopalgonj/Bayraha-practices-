import requests
import matplotlib.pyplot as plt

# Step 1: Fetch data from the local server URL
url = "http://localhost:8000/customers.json"
response = requests.get(url)

if response.status_code == 200:
    data = response.json()  # Load the JSON data from the response
    print("Data fetched successfully!")
else:
    print(f"Failed to retrieve data. Status code: {response.status_code}")
    exit()

# Step 2: Process the JSON data
astronauts = data['people']
for astronaut in astronauts:
    print(f"{astronaut['name']} is on the {astronaut['craft']} spacecraft.")

# Step 3: Count astronauts per spacecraft and plot as before
craft_counts = {}
for astronaut in astronauts:
    craft = astronaut['craft']
    if craft in craft_counts:
        craft_counts[craft] += 1
    else:
        craft_counts[craft] = 1

crafts = list(craft_counts.keys())
counts = list(craft_counts.values())

# Step 4: Create the bar chart
plt.bar(crafts, counts, color='skyblue')
plt.xlabel('Spacecraft')
plt.ylabel('Number of Astronauts')
plt.title('Number of Astronauts on Each Spacecraft')
plt.show()