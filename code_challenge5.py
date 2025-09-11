
print("Welcome to the Manga Reader Recommender!")
print("Answer a few questions to find your next read.")

genre = input("What genre do you like? (action, romance, horror): ").lower().strip()
length = input("How long should the manga be? (short, medium, long): ").lower().strip()
decade = input("Which decade? (2000, 2010): ").lower().strip()

print("\nSearching for", length, genre, "manga from the", decade, "...\n")

if genre == "action":
    if length == "short" and decade == "2000":
        print("We recommend: Black Cat, Rurouni Kenshin, Flame of Recca")
    elif length == "short" and decade == "2010":
        print("We recommend: One Punch Man, Akame ga Kill, Blue Exorcist")
    elif length == "medium" and decade == "2000":
        print("We recommend: Fullmetal Alchemist, Gantz, D.Gray-man")
    elif length == "medium" and decade == "2010":
        print("We recommend: My Hero Academia, Magi, Noragami")
    elif length == "long" and decade == "2000":
        print("We recommend: Naruto, Bleach, Katekyo Hitman Reborn")
    elif length == "long" and decade == "2010":
        print("We recommend: Attack on Titan, Fairy Tail, Hunter x Hunter")

elif genre == "horror":
    if length == "short" and decade == "2000":
        print("We recommend: Higurashi, Uzumaki, Goth")
    elif length == "short" and decade == "2010":
        print("We recommend: Another, I Am a Hero, Ajin")
    elif length == "medium" and decade == "2000":
        print("We recommend: Death Note, Monster, Elfen Lied")
    elif length == "medium" and decade == "2010":
        print("We recommend: Tokyo Ghoul, Paranoia Agent, Doubt")
    elif length == "long" and decade == "2000":
        print("We recommend: Parasyte, Blade of the Immortal, Bastard!!")
    elif length == "long" and decade == "2010":
        print("We recommend: The Promised Neverland, Deadman Wonderland, Terra Formars")

elif genre == "romance":
    if length == "short" and decade == "2000":
        print("We recommend: Lovely Complex, Fruits Basket, Itazura na Kiss")
    elif length == "short" and decade == "2010":
        print("We recommend: Your Lie in April, Orange, Toradora")
    elif length == "medium" and decade == "2000":
        print("We recommend: Boys Over Flowers, Peach Girl, Honey and Clover")
    elif length == "medium" and decade == "2010":
        print("We recommend: Ao Haru Ride, Say I Love You, My Little Monster")
    elif length == "long" and decade == "2000":
        print("We recommend: Kimi ni Todoke, Kare Kano, Marmalade Boy")
    elif length == "long" and decade == "2010":
        print("We recommend: Nana, Skip Beat!, Nodame Cantabile")

else:
    print("Sorry, no", length, genre, "manga from the", decade, "in our list.")
