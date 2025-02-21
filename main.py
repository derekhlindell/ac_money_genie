def init():
    # import csv's
    pass

def greeting():
    print("Welcome, I am the ACNH Money Genie, I can give you the info you need to make the most money.")
    print("But first, I need some info from you.")

def get_user_data():
    hemisphere = input("What hemisphere is your ACNH game in?: (N/S): ")
    month = input("Great, now what month is it currently (please spell out the whole month): ")
    time = input("Ok, one last thing, what hour is it currently in 24 hour format rounded down? (example response for 4:32 PM, 16): ")
    return hemisphere, month, time

def find_bugs() -> dict:
    pass

def find_fish() -> dict:
    pass

def find_marine_life() -> dict:
    pass

def main():
    # Program to tell you what to focus on to make the most money at your current time in AC NH
    # create a database of all bugs, fish and marine life.
        # imported into CSVs
    greeting()

    setting_up = True
    while setting_up:
        hemisphere, month, time = get_user_data()
        if (input(f"Great, you're in the {hemisphere} hemisphere, it's {month} at {time} o'clock correct? (y/n): ")) != "y":
            print("Oh, ok, let's fix what we got wrong then.")
        else:
            print("Great, let's see how you can make the most money then.")
            setting_up = False

    # Indexes bugs, fish, marine life based on current hemisphere, month and current time.
    print("Here are your options")
    valid_bugs = find_bugs()
    valid_fish = find_fish()
    valid_marine_life = find_marine_life()

if __name__ == "__main__":
    main()
