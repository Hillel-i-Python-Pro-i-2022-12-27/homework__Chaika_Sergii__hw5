from application.files_example.avare_value_file import average_value_from_csv
from application.files_example.create_text_fine import create_txt_file
from application.files_example.number_of_astronauts import number_of_astronaut
from application.files_example.read_text_file import read_text_file
from application.files_example.request_end_download import get_requests_data, \
    get_download_file
from application.files_example.write_file_user import to_write_file_user
from application.logging.init_logging import init_logging


def main() -> None:
    create_txt_file(name_file="fake_text")
    read_text_file(name_file="fake_text")
    to_write_file_user(name_file="users", amount_users=15)
    get_requests_data(url="http://api.open-notify.org/astros.json")
    number_of_astronaut(name_file="output")
    get_download_file("https://drive.google.com/uc?export=download&id=1yM0a4CSf0iuAGOGEljdb7qcWyz82RBxl")
    average_value_from_csv(name_file="output")


if __name__ == "__main__":
    init_logging()
    main()
