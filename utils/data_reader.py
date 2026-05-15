import json
import os


def load_test_data():

    current_dir = os.path.dirname(__file__)

    project_dir = os.path.dirname(current_dir)

    file_path = os.path.join(
        project_dir,
        "test_data",
        "users.json"
    )

    with open(file_path, "r") as file:
        data = json.load(file)

    return data