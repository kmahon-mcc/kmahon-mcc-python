"""
Modify Artist List: Write a function to replace an artist in the top_artists list. The function should ask the user for an index and a new artist name. Ensure your function catches and handles ValueError for invalid number conversion and IndexError for out-of-range indices.
General Error Handling: Modify your function to catch both ValueError and IndexError using a single except block. Provide a general error message like "An input error occurred."
"""


def main():
    top_artists = ["The Beatles", "Madonna", "Elton John", "Elvis Presley", "Mariah Carey",
                   "Stevie Wonder", "Janet Jackson", "Michael Jackson", "Whitney Houston", "Rihanna"]
    print(top_artists)
    while True:
        try:
            art_index = int(
                input("Enter the index of the artist you'd like to replace (0-9): "))
            # if not 0 <= art_index < len(top_artists):
            # raise IndexError
            artist = input("Enter the name of the artist you'd like to add: ")
            top_artists[art_index] = artist.strip().title()
            print(top_artists)
            break
        except (ValueError, IndexError):
            print("An input error occurred")
        except Exception as e:
            print("An unexpected error occurred:", e)
            break


main()
