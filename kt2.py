import json
import csv
import os.path
FILES_DIR = os.path.dirname(file)


def get_path(filename: str):
    return os.path.join(FILES_DIR, filename)


CSV_FILE_PATH = get_path(filename="books.csv")
JSON_FILE_PATH = get_path(filename="users.json")

books_data = []
with open(CSV_FILE_PATH, newline='') as f:
    reader = csv.reader(f)
    header = next(reader)
    for row in reader:
        books_data.append(dict(zip(header, row)))

with open(JSON_FILE_PATH, "r") as f:
    users_data = json.load(f)

num_users = len(users_data)
num_books = len(books_data)
one_user_book = num_books // num_users
one_user_remaining_books = num_books % num_users

result_data = []
for user in users_data:
    user_books = []
    for i in range(one_user_book):
        user_books.append(books_data.pop(0))
    if one_user_remaining_books > 0:
        user_books.append(books_data.pop(0))
        one_user_remaining_books -= 1
    user['books'] = user_books
    result_data.append(user)

RESULT_JSON_FILE_PATH = get_path(filename="result.json")
with open(RESULT_JSON_FILE_PATH, 'w') as f:
    json.dump(result_data, f, indent=4)