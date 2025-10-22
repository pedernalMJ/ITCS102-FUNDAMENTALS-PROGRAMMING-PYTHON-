anime_list = []
while True:
    anime = input("Enter the title of an anime (or type 'exit' to finish): ")

    if anime.lower() == "exit":
         print("you have exited the anime program")
         break
    else: 
        anime_list.append(anime)   

    
print(f"The anime you have listed:{anime_list}")