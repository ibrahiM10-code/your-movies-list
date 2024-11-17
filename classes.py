import random, time


class RandomSelector:
    def find_item(self, items_list: list) -> str:
        chosen_item = random.choice(items_list)
        return chosen_item.strip("\n")


class FileManager:
    def __init__(self, file_name: str, list_items: list) -> None:
        self.file_name = file_name
        self.list_items = list_items

    def create_file(self):
        with open(f"{self.file_name}.txt", "w") as file:
            for item in self.list_items:
                file.write(item + "\n")
            print("Items added succesfully!")

    def add_data(self, new_item: str):
        with open(f"{self.file_name}.txt", "a") as file:
            file.write(new_item + "\n")
        print(f"{new_item} has been added.")

    def get_file_data(self) -> str:
        with open(f"{self.file_name}.txt", "r") as file:
            data = file.readlines()
            print(f"You have {len(data)} items in your file.")
            time.sleep(1)
            for text in data:
                print(text.strip("\n"))

    def update_file(self, random_item: str):
        with open(f"{self.file_name}.txt", "r+") as file:
            lines = file.readlines()
            for line in range(0, len(lines)):
                if lines[line].strip("\n") == random_item:
                    lines.remove(lines[line])
                    break
            with open(f"{self.file_name}.txt", "w") as f:
                for line in lines:
                    f.write(line)
        print(f"{random_item} has been removed from the text file.")

    def get_data(self) -> list:
        with open(f"{self.file_name}.txt", "r") as file:
            data = file.readlines()
            return data
