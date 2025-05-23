#Douglas Martinez
#CIS261
#Movie_Guide_Part_2
import os

# Use a safe writable path
file_path = os.path.expanduser("~/movie_guide_data.txt")

def initialize_movies_file():
    if not os.path.exists(file_path):
        with open(file_path, "w") as file:
            file.write("Cat on a Hot Tin Roof\n")
            file.write("On the Waterfront\n")
            file.write("Monty Python and the Holy Grail\n")

def read_movies_from_file():
    with open(file_path, "r") as file:
        return [line.strip() for line in file.readlines()]

def write_movies_to_file(movies):
    with open(file_path, "w") as file:
        for movie in movies:
            file.write(movie + "\n")

def display_menu():
    print("\n=== Movie List Program ===")
    print("1. View movies")
    print("2. Add a movie")
    print("3. Delete a movie")
    print("4. Exit")

def add_movie(movies):
    title = input("Enter the movie title to add: ").strip()
    if title:
        if title in movies:
            print(f"'{title}' is already in the list.")
        else:
            movies.append(title)
            write_movies_to_file(movies)
            print(f"'{title}' has been added.")
    else:
        print("No title entered.")

def delete_movie(movies):
    view_movies(movies)
    try:
        index = int(input("Enter the number of the movie to delete: ")) - 1
        if 0 <= index < len(movies):
            removed = movies.pop(index)
            write_movies_to_file(movies)
            print(f"'{removed}' has been deleted.")
        else:
            print("Invalid number.")
    except ValueError:
        print("Please enter a valid number.")

def view_movies(movies):
    if not movies:
        print("No movies in the list.")
    else:
        print("\n=== Movie List ===")
        for i, movie in enumerate(movies, start=1):
            print(f"{i}. {movie}")

def main():
    initialize_movies_file()

    while True:
        movies = read_movies_from_file()
        display_menu()
        choice = input("Enter a menu option (1-4): ").strip()

        if choice == "1":
            view_movies(movies)
        elif choice == "2":
            add_movie(movies)
        elif choice == "3":
            delete_movie(movies)
        elif choice == "4":
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid selection. Please choose a valid option (1-4).")

if __name__ == "__main__":
    main()
