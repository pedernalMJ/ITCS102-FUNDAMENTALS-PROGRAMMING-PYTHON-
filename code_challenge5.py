print("Welcome to the Manga Reader Recommender!")
print("Answer a few questions to find your next read.")

genre = input("What genre do you like? (action, romance, horror): ").lower()
length = input("How long should the manga be? (short, medium, long): ").lower()
decade = input("Which decade? (2000, 2010): ").lower()

print("\nSearching for", length, genre, "manga from the", decade, "...\n")
#ACTION
if genre == "action" and length == "short" and decade == "2000":
    print("We recommend: Black Cat, Rurouni Kenshin, Flame of Recca")
elif genre == "action" and length == "short" and decade == "2010":
    print("We recommend: One Punch Man, Akame ga Kill, Blue Exorcist")
elif genre == "action" and length == "medium" and decade == "2000":
    print("We recommend: Fullmetal Alchemist, Gantz, D.Gray-man")
elif genre == "action" and length == "medium" and decade == "2010":
    print("We recommend: My Hero Academia, Magi, Noragami")
elif genre == "action" and length == "long" and decade == "2000":
    print("We recommend: Naruto, Bleach, Katekyo Hitman Reborn")
elif genre == "action" and length == "long" and decade == "2010":
    print("We recommend: Attack on Titan, Fairy Tail, Hunter x Hunter")
#HORROR
elif genre == "horror" and length == "short" and decade == "2000":
    print("We recommend: Higurashi, Uzumaki, Goth")
elif genre == "horror" and length == "short" and decade == "2010":
    print("We recommend: Another, I Am a Hero, Ajin")
elif genre == "horror" and length == "medium" and decade == "2000":
    print("We recommend: Death Note, Monster, Elfen Lied")
elif genre == "horror" and length == "medium" and decade == "2010":
    print("We recommend: Tokyo Ghoul, Paranoia Agent, Doubt")
elif genre == "horror" and length == "long" and decade == "2000":
    print("We recommend: Parasyte, Blade of the Immortal, Bastard!!")
elif genre == "horror" and length == "long" and decade == "2010":
    print("We recommend: The Promised Neverland, Deadman Wonderland, Terra Formars")
#ROMANCE
elif genre == "romance" and length == "short" and decade == "2000":
    print("We recommend: Lovely Complex, Fruits Basket, Itazura na Kiss")
elif genre == "romance" and length == "short" and decade == "2010":
    print("We recommend: Your Lie in April, Orange, Toradora")
elif genre == "romance" and length == "medium" and decade == "2000":
    print("We recommend: Boys Over Flowers, Peach Girl, Honey and Clover")
elif genre == "romance" and length == "medium" and decade == "2010":
    print("We recommend: Ao Haru Ride, Say I Love You, My Little Monster")
elif genre == "romance" and length == "long" and decade == "2000":
    print("We recommend: Kimi ni Todoke, Kare Kano, Marmalade Boy")
elif genre == "romance" and length == "long" and decade == "2010":
    print("We recommend: Nana, Skip Beat!, Nodame Cantabile")

else:
    print("Sorry, no", length, genre, "manga from the", decade, "in our list.")

