#Alyce Gaines
#CSI261
#MovieGuidePart2

FILENAME = "movies.txt"

def write_movies(movies):
    with open(FILENAME, "w") as file:
        for movie in movies:
            file.write(f"{movie}\n")

def read_movies():
    movies = []
    with open(FILENAME) as file:
        for line in file:
            line = line.replace("\n", "")
            movies.append(line)
        return movies

def list_movies(movies):
    for i, movie in enumerate(movies, start=1):
        print(f"{i}. {movie}")
    print()

def add_movie(movies):
    movie =inout("Movie: ")
    movies.append(movie)
    write_movies(movies)
    print(f"{movies} was added.\n")

def delete_movie(movies):
    index = int(input("Number: "))
    if index < 1 or index > len(movies):
        print("invaild movie number.\n")
    else:
        movie = movies.pop(index - 1)
        write_movies(movies)


def display_menu():
    print("the movie list program")
    
    print("command menu")
    print("list - list all movies")
    print("add - add a movie")
    print("del - delete a movie")
    print("exit - exit program")
    
def list(movie_list):
    for i, movie in enumerate(movie_list, start=1):
        print(f"{i}. {movie}")

def add(movie_list):
    movie = input("Name: ")
    movie_list.append(movie)
    print(f"{movie} was added.\n")

def delete(movie_list):
    number = int(input("Number: "))
    if number < 1 or number > len(movie_list):
        print("invalid movie number.\n")
    else:
        movie = movie_list.pop(number-1)
        print(f"{movie} was deleted.\n")

def main():
    movie_list = ["alien vs predator",
                  "pride & prejudice",
                  "labor day(2013)"]
    
    display_menu()
    while True:        
        command = input("Command: ")
        if command.lower() == "list":
            list(movie_list)   
        elif command.lower() == "add":
            add(movie_list)
        elif command.lower() == "del":
            delete(movie_list)  
        elif command.lower() == "exit":
            break
        else:
            print("invalid. try again.\n")

    print("laterz!")

if __name__ == "__main__":
    main()