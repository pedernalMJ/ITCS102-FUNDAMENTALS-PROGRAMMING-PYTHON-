print("Welcome to the Manga Reader Recommender!")
print("Answer a few questions to find your next read.")

genre = input("What genre do you like? (action, romance, horror): ").lower()
length = input("How long should the manga be? (short, medium, long): ").lower()
decade = input("Which decade? (2000, 2010): ").lower()

print("\nSearching for", length, genre, "manga from the", decade, "...\n")

if genre == "action" and length == "short" and decade == "2000":
    print("We recommend: Hikaru no Go")
elif genre == "action" and length == "short" and decade == "2010":
    print("We recommend: One Punch Man")
elif genre == "action" and length == "medium" and decade == "2000":
    print("We recommend: Fullmetal Alchemist")
elif genre == "action" and length == "medium" and decade == "2010":
    print("We recommend: My Hero Academia")
elif genre == "action" and length == "long" and decade == "2000":
    print("We recommend: Naruto or Bleach")
elif genre == "action" and length == "long" and decade == "2010":
    print("We recommend: Attack on Titan")

elif genre == "horror" and length == "short" and decade == "2000":
    print("We recommend: Higurashi")
elif genre == "horror" and length == "short" and decade == "2010":
    print("We recommend: Another")
elif genre == "horror" and length == "medium" and decade == "2000":
    print("We recommend: Death Note")
elif genre == "horror" and length == "medium" and decade == "2010":
    print("We recommend: Tokyo Ghoul")
elif genre == "horror" and length == "long" and decade == "2000":
    print("We recommend: Parasyte")
elif genre == "horror" and length == "long" and decade == "2010":
    print("We recommend: The Promised Neverland")

elif genre == "romance" and length == "short" and decade == "2000":
    print("We recommend: Lovely Complex")
elif genre == "romance" and length == "short" and decade == "2010":
    print("We recommend: Your Lie in April")
elif genre == "romance" and length == "medium" and decade == "2000":
    print("We recommend: Boys Over Flowers")
elif genre == "romance" and length == "medium" and decade == "2010":
    print("We recommend: Ao Haru Ride")
elif genre == "romance" and length == "long" and decade == "2000":
    print("We recommend: Kimi ni Todoke")
elif genre == "romance" and length == "long" and decade == "2010":
    print("We recommend: Nana")

else:
    print("Sorry, no", length, genre, "manga from the", decade, "in our list pls pick others.")
