import os

TOFO_FILE_PATH = "files/todos.txt"

if os.path.exists(TOFO_FILE_PATH):
    with open(TOFO_FILE_PATH, "r") as f:
        pass

def load_todos(filepath=TOFO_FILE_PATH):
    """
    my doc string
    :return:
    """
    with open(filepath, "r") as todos_file_r:
        loadable_todos_list: list[str] = todos_file_r.readlines()
    return loadable_todos_list


def show_todos(showable_todos_list):
    #todos_list = [item.strip('\n') for item in todos_list]
    for index, item in enumerate(showable_todos_list):
        item.removesuffix("\n")
        print(f"{index + 1}. {item}", end="")
    print("")


def write_todos(writeable_todos_list, filepath=TOFO_FILE_PATH):
    with open(filepath, "w") as todos_file_w:
        todos_file_w.writelines(writeable_todos_list)

