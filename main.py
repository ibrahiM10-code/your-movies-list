from classes import FileManager, RandomSelector, Processes
import os

rndm_selector = RandomSelector()
process = Processes(random_selector=rndm_selector)
decision = int(input("Are you creating a new movie/series list or checking one? (1/2): "))

if decision == 1:
    new_file = input("Give a name to the file: ")
    new_file = FileManager(file_name=new_file)
    while True:
        continue_adding = process.add_to_new_file(file_manager=new_file)
        if continue_adding == "n":
            break
elif decision == 2:
    os.system("cls")
    process.display_lists()
    file_name = input("Write the name of the list which movies/series you want to check out (don't include the .txt extension): ")
    file_mng = FileManager(file_name=file_name)
    if not file_mng.get_file_data():
        rndm_movie = int(input("Do you want to get a random movie/series to watch? or Are you trying to add a movie/series? (1/2): "))
        os.system("cls")
        while True:
            if rndm_movie == 1:
                if not process.get_random_movie_series(file_manager=file_mng):
                    break
                else:
                    print("There has been a problem getting a random movie/series, try again.")
            elif rndm_movie == 2:
                add_more = process.add_movie_series(file_manager=file_mng)
                if add_more.lower() == "n":
                    break
                elif add_more == False:
                    print("There has been a problem when adding the movie/series, try again.")
            else:
                os.system("cls")
                print("Goodbye!")
