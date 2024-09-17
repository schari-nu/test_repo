# @TODO: Your code here
# Dictionary full of info
my_info = {"name": "Rex",
           "occupation": "dog",
           "age": 11,
           "hobbies": ["barking", "eating", "sleeping", "loving my owner","tail wagging"],
           "wake-up": {"Mon": 7, "Friday": 5, "Saturday": 10, "Sunday": 9}}
# Print out results are stored in the dictionary
print(f'Hello I am {my_info["name"]} and I am a {my_info["occupation"]}')
print(f'I have {len(my_info["hobbies"])} hobbies!')
print(f"{my_info["hobbies"][2]}")
print(f'On the weekday I get up at {my_info["wake-up"]["Friday"]}')
