anime_list = []
while True:
    anime = input("Enter the title of an anime (or type 'exit' to finish): ")

    if anime.lower() == "exit":
         print("you have exited the anime program")
         break
    else: 
        anime_list.append(anime)   
        print(f"{anime} has been added to your list.")
    
print("Your anime List:")
for title in anime_list:
    print(f"-{title}")
