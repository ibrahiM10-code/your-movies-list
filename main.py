from classes import FileManager, RandomSelector
import os

movies_list = []

decision = int(input("Are you creating a new movie/series list or checking one? (1/2): "))

if decision == 1:
    while True:
        new_file = input("Give a name to the file: ")
        movie = input("Add to your txt file: ")
        movies_list.append(movie)
        continue_adding = input("Want to add more? yes/no: ")
        if continue_adding == "no":
            break
elif decision == 2:
    file_name = input("Write the name of the file which movies you want to check out: ")
    file_mng = FileManager(file_name=file_name, list_items=movies_list)
    file_mng.get_file_data()
    rndm_movie = input("Do you want to get a random movie/series to watch? (y/n): ")
    if "y" == rndm_movie.lower():
        rndm_selector = RandomSelector()
        chosen_item = rndm_selector.find_item(items_list=file_mng.get_data())
        print(chosen_item + " is the chosen movie.")
        file_mng.update_file(random_item=chosen_item)
    else:
        os.system("cls")
        print("Goodbye!")
