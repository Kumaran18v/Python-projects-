import random  
import string  

# word lists for social media names and gaming names 
social_adjectives = ["trendy", "chill", "vibing", "stylish", "glam", "aesthetic", "cozy", "dreamy"]  
social_nouns = ["queen", "star", "icon", "model", "artist", "blogger", "guru", "influencer"]  

gaming_adjectives = ["shadow", "dark", "furious", "mystic", "stealth", "deadly", "frozen", "unstoppable"]  
gaming_nouns = ["slayer", "hunter", "assassin", "warrior", "sniper", "reaper", "ghost", "ninja"]  

#function to generate username 
def generate_username(category, add_number, add_special, length):  
    if category == "1":  
        adjectives, nouns = social_adjectives, social_nouns  
    else:  
        adjectives, nouns = gaming_adjectives, gaming_nouns  

    username = ""  
    while len(username) < length:  
        adjective = random.choice(adjectives).capitalize()  
        noun = random.choice(nouns).capitalize()  
        username = adjective + noun  
# creating option to select the numbers , special characters or both
        if add_number and add_special:  
            username += str(random.randint(10, 99)) + random.choice(string.punctuation)  
        elif add_number:  
            username += str(random.randint(10, 99))  
        elif add_special:  
            username += random.choice(string.punctuation)  

    return username[:length]  

#function to save username in file. You can change the filename instead of username.txt
def save_username(username):  
    with open("usernames.txt", "a") as file:  
        file.write(username + "\n")  
#Main function 
def main():  
    print("welcome to the random username generator!")  
    print("choose username type:")  
    print("1. social media")  
    print("2. gaming")  

    while True:  
        category = input("enter your choice (1-2): ")  
        if category in ["1", "2"]:  
            break  
        print("invalid choice! enter 1 or 2.")  

#Asking user to add numbers or special characters in username 
    print("choose customization options:")  
    print("1. include numbers")  
    print("2. include special characters")  
    print("3. include both")  
    print("4. no extras")  

    while True:  
        choice = input("enter your choice (1-4): ")  
        if choice in ["1", "2", "3", "4"]:  
            break  
        print("invalid choice! enter 1, 2, 3, or 4.")  

    add_number = choice in ["1", "3"]  
    add_special = choice in ["2", "3"]  

    while True:  
        try:  
            length = int(input("enter desired username length (min 5, max 17): "))  
            if 5 <= length <= 17:  
                break  
            print("please enter a number between 5 and 17.")  
        except ValueError:  
            print("invalid input! enter a number.")  

    username = generate_username(category, add_number, add_special, length)  
    print(f"generated username: {username}")  

# Asking user for save the username or not 
    if input("save this username to file? (y/n): ").lower() == "y":  
        save_username(username)  
        print("username saved!")  

# Calling the main function 
if __name__ == "__main__":  
    main()
