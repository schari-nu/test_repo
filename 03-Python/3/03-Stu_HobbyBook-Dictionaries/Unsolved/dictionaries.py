
# Create a dictionary to hold the actor's names.
#actors = {}

# Create a dictionary using the built-in function.
actors = dict()

# A dictionary of an actor.
actors = {"name": "Tom Cruise"}
print(f'{actors["name"]}')
print("-" * 50)
print()
actors["name"] = "Denzel Washington"
print(f'{actors["name"]}')
print("-" * 50)
print()
actors = {"name": "DZ"}

actors_list = [
    "Tom Cruise",
    "Angelina Jolie",
    "Kristen Stewart",
    "Denzel Washington"]
actors["name"] = actors_list
print(f'{actors["name"]}')
print("-" * 50)
print()
# Print the first actor
print(f'{actors["name"][1]}')
print("-" * 50)
print()


# A dictionary can contain multiple pairs of information
actress = {
    "name": "Angelina Jolie",
    "genre": "Action",
    "nationality": "United States"
}

print(f"{actress["genre"]}")

another_actor = {
    "name": "Sylvester Stallone",
    "age": 62,
    "married": True,
    "best movies": [
        "Rocky",
        "Rocky 2",
        "Rocky 3"]}
print(f'{another_actor["name"]} was in {another_actor["best movies"][2]}')
print("-" * 50)
print()

film = {
    "title": "Interstellar",
    "revenues": {
        "United States": 360,
        "China": 250,
        "United Kingdom": 73
    }
}

# film = {
#     "title": "Interstellar",
#     "revenues": {  "United States": 360,  "China": 250,   "United Kingdom": 73
#     }
# }
print(f'{film["title"]} made {film["revenues"]["United States"]}'" million dollars in the US.")

