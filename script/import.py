# import a movie list csv file and use the imdb API to find the imdbID

import sys
import pandas as pd

def check_database(year):
    current_file = "./data" + year + ".csv"
    current_list = pd.read_csv(current_file, encoding='utf-8')
    print(current_list)

if __name__ == "__main__":
    print(f"Update database with IMDB API")
    if len(sys.argv) < 2:
        print("You did not provide a year as argument. Put it as a parameter after import.py")
        exit()
    year = sys.argv[1]
    check_database(year)
