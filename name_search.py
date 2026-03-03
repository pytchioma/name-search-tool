import time

# Name_Search Tool

# Step 1: Create dictionary with 50 names
names_dict = {
    "Chioma": 1,
    "Eniola": 2,
    "Ebuka": 3,
    "Victor": 4,
    "Gift" : 5,
    "Emeka" : 6,
    "Moyo" : 7,
    "Jamal" : 8,
    "Elijah" : 9,
    "Davis" : 10,
    "Raph" : 11,
    "Halima" : 12,
    "Treasure" : 13,
    "Fisayo" : 14,
    "Emzy" : 15, 
    "Micheal" : 16,
    "Austin" : 18,
    "James" : 19,
    "Lanre" : 20,
    "Dami" : 21,
    "Seyi" : 22,
    "Tolu" : 23,
    "Ahmed" : 24,
    "Chike" : 25,
    "Chidinma" : 26,
    "Alice" : 27,
    "Ridwan" : 28,
    "May" : 29,
    "Esther" : 30
}


#Step 2: Create search function
def search_name():
    user_input = input("Enter a name to search: ").strip().capitalize()
    found = False


    print("\nSearching....\n")
    found = False

    # Loop through the dictionary and print each name one by one with a delay
    for name in names_dict:
        print("Checking:", name)
        time.sleep(0.3)  # Wait half a second between each name
        if name == user_input:
           found = True
           break        # Stop searching  if the name is found

    # After the loop finishes print the result

    if found:
        print("\nFound!", user_input)

    else:
        print("\n", user_input, "\nNot Found!\n")
        print("Goodbye !")

search_name()  # Inside the loop


#Step 3: Run the tool
