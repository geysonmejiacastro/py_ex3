# CMP 269: Programming Methods III
# In-Class Assignment: File I/O and API Integration

import requests

"""
INSTRUCTIONS:
Complete 5 tasks involving file I/O, JSON, and API requests.
"""

#  TASK 1 
def task_1_append_logger():
    print("\n--- Task 1: Append Logger ---")

    note = input("Enter a note for the log: ")

    with open("session_log.txt", "a") as file:
        file.write(note + "\n")

    print("\n--- Log History ---")
    with open("session_log.txt", "r") as file:
        print(file.read())


# TASK 2 
def task_2_word_count_utility():
    print("\n--- Task 2: Word Count Utility ---")

    text = "Knowledge is Power. Go Lightning! Python makes data easy."

    with open("lehman_motto.txt", "w") as file:
        file.write(text)

    with open("lehman_motto.txt", "r") as file:
        content = file.read()
        words = content.split()
        print("Word Count:", len(words))


#  TASK 3 
def task_3_api_status_checker():
    print("\n--- Task 3: API Status Checker ---")

    try:
        response = requests.get(
            "https://jsonplaceholder.typicode.com/posts/101",
            timeout=5
        )

        if response.status_code == 200:
            print(response.json())

        elif response.status_code == 404:
            print("Error: Post not found.")

        else:
            print("Error: Unexpected status code", response.status_code)

    except requests.exceptions.Timeout:
        print("Error: Request timed out.")


# TASK 4 
def task_4_data_filtering():
    print("\n--- Task 4: Data Filtering ---")

    try:
        response = requests.get("https://jsonplaceholder.typicode.com/users")
        users = response.json()

        print("Users living in Suite addresses:\n")

        for user in users:
            if "Suite" in user["address"]["suite"]:
                print(user["name"])

    except Exception as e:
        print("Error:", e)


 # TASK 5 
def task_5_integration_report():
    print("\n--- Task 5: Integration Report ---")

    try:
        response = requests.get("https://jsonplaceholder.typicode.com/posts/1")
        data = response.json()

        title = data["title"]
        body = data["body"]

        with open("api_report.txt", "w") as file:
            file.write("API REPORT\n")
            file.write("====================\n")
            file.write("Title: " + title + "\n\n")
            file.write("Body:\n" + body + "\n")

        print("Report Generated")

    except Exception as e:
        print("Error:", e)


if __name__ == "__main__":

    while True:
        print("\n===== MENU =====")
        print("1. Task 1 - Logger")
        print("2. Task 2 - Word Count")
        print("3. Task 3 - API Status Checker")
        print("4. Task 4 - Data Filtering")
        print("5. Task 5 - Integration Report")
        print("0. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            task_1_append_logger()
        elif choice == "2":
            task_2_word_count_utility()
        elif choice == "3":
            task_3_api_status_checker()
        elif choice == "4":
            task_4_data_filtering()
        elif choice == "5":
            task_5_integration_report()
        elif choice == "0":
            break
        else:
            print("Invalid choice")