import random, time, os

class RandomSelector:
    def find_item(self, items_list: list) -> str:
        try:
            chosen_item = random.choice(items_list)
            return chosen_item.strip("\n")
        except IndexError:
            print("The list is empty!")
            return 0

class FileManager:
    def __init__(self, file_name: str) -> None:
        self.file_name = file_name
        self.list_items = []

    def create_file(self):
        try:
            with open(f"{self.file_name}.txt", "w") as file:
                for item in self.list_items:
                    file.write(item + "\n")
            print("Items added successfully!")
        except Exception as e:
            print(f"Error while creating file: {e}")
            return False

    def add_data(self, new_item: str):
        try:
            with open(f"{self.file_name}.txt", "a") as file:
                file.write(new_item + "\n")
            print(f"{new_item} has been added.")
        except Exception as e:
            print(f"Error while adding data: {e}")
            return False

    def get_file_data(self):
        try:
            with open(f"{self.file_name}.txt", "r") as file:
                data = file.readlines()
                print(f"You have {len(data)} items in your file.")
                time.sleep(1)
                for text in data:
                    print(text.strip("\n"))
        except FileNotFoundError:
            print("Error: File not found.")
            return False
        except Exception as e:
            print(f"Error while reading file data: {e}")
            return False

    def update_file(self, random_item: str):
        try:
            with open(f"{self.file_name}.txt", "r") as file:
                lines = file.readlines()

            updated_lines = [line for line in lines if line.strip("\n") != random_item]

            with open(f"{self.file_name}.txt", "w") as file:
                file.writelines(updated_lines)

            print(f"{random_item} has been removed from the text file.")
        except FileNotFoundError:
            print("Error: File not found.")
        except Exception as e:
            print(f"Error while updating file: {e}")

    def get_data(self) -> list:
        try:
            with open(f"{self.file_name}.txt", "r") as file:
                data = file.readlines()
                return data
        except FileNotFoundError:
            print("Error: File not found.")
            return []
        except Exception as e:
            print(f"Error while getting data: {e}")
            return []

class Processes:
    def __init__(self, random_selector: RandomSelector):
        self.random_selector = random_selector

    def get_random_movie_series(self, file_manager: FileManager):
        try:
            chosen_item = self.random_selector.find_item(items_list=file_manager.get_data())
            if chosen_item:
                print(chosen_item + " is the chosen movie/series.")
                file_manager.update_file(random_item=chosen_item)
                time.sleep(1)
        except Exception as e:
            print(f"Error while selecting random movie/series: {e}")
            return False

    def add_movie_series(self, file_manager: FileManager):
        try:
            movie_series_to_add = input("Write the name of movie/series to add to your list: ")
            file_manager.add_data(new_item=movie_series_to_add)
            print("Added successfully!")
            more_to_add = input("Want to add more? (y/n): ")
            os.system("cls")
            return more_to_add
        except Exception as e:
            print(f"Error while adding movie/series: {e}")
            return False

    def add_to_new_file(self, file_manager: FileManager):
        try:
            movie = input("Add to your txt file: ")
            if not file_manager.add_data(new_item=movie):
                continue_adding = input("Want to add more? yes/no: ")
                os.system("cls")
                return continue_adding
        except Exception as e:
            print(f"Error while adding to new file: {e}")

    def get_lists(self):
        try:
            files = os.listdir()
            lists = [file for file in files if ".txt" in file]
            return lists
        except Exception as e:
            print(f"Error while getting lists: {e}")
            return []

    def display_lists(self):
        try:
            available_lists = self.get_lists()
            for name in available_lists:
                print(name)
        except Exception as e:
            print(f"Error while displaying lists: {e}")