# Read the file
with open("input", "r") as file:
    data = file.read()

# Split the data into different sections
sections = data.split("\n\n")

# Parse the seeds
seeds = list(map(int, sections[0].split(": ")[1].split()))

# Parse the seed-to-soil map
seed_to_soil_map = []
for line in sections[1].split("\n")[1:]:
    row = list(map(int, line.split()))
    seed_to_soil_map.append(row)

# Parse the soil-to-fertilizer map
soil_to_fertilizer_map = []
for line in sections[2].split("\n")[1:]:
    row = list(map(int, line.split()))
    soil_to_fertilizer_map.append(row)

# Parse the fertilizer-to-water map
fertilizer_to_water_map = []
for line in sections[3].split("\n")[1:]:
    row = list(map(int, line.split()))
    fertilizer_to_water_map.append(row)

# Parse the water-to-light map
water_to_light_map = []
for line in sections[4].split("\n")[1:]:
    row = list(map(int, line.split()))
    water_to_light_map.append(row)

# Parse the light-to-temperature map
light_to_temperature_map = []
for line in sections[5].split("\n")[1:]:
    row = list(map(int, line.split()))
    light_to_temperature_map.append(row)

# Parse the temperature-to-humidity map
temperature_to_humidity_map = []
for line in sections[6].split("\n")[1:]:
    row = list(map(int, line.split()))
    temperature_to_humidity_map.append(row)

# Parse the humidity-to-location map
humidity_to_location_map = []
for line in sections[7].split("\n")[1:]:
    row = list(map(int, line.split()))
    humidity_to_location_map.append(row)


def remap(seed, conversion_map):
    for key in conversion_map:
        if seed >= key[1] and seed < key[1]+key[2]:
            return seed-key[1]+key[0]
    return seed

def findlocations(seeds):
    locations = []
    for seed in seeds:
        soil = remap(seed, seed_to_soil_map)
        fertilizer = remap(soil, soil_to_fertilizer_map)
        water = remap(fertilizer, fertilizer_to_water_map)
        light = remap(water, water_to_light_map)
        temperature = remap(light, light_to_temperature_map)
        humidity = remap(temperature, temperature_to_humidity_map)
        location = remap(humidity, humidity_to_location_map)
        
        locations.append(location)
        
    print(f"Minimal location: {min(locations)}")
    
findlocations(seeds)



numbers = []
locations = []

for i in range(0, len(seeds), 2):
    start = int(seeds[i])
    length = int(seeds[i + 1])
    for seed in range(start, start + length):
        soil = remap(seed, seed_to_soil_map)
        fertilizer = remap(soil, soil_to_fertilizer_map)
        water = remap(fertilizer, fertilizer_to_water_map)
        light = remap(water, water_to_light_map)
        temperature = remap(light, light_to_temperature_map)
        humidity = remap(temperature, temperature_to_humidity_map)
        location = remap(humidity, humidity_to_location_map)
        
        locations.append(location)        

print(f"Minimal location: {min(locations)}")