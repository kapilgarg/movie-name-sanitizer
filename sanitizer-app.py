from sanitizer import sanitize
from rich import print


if __name__ == '__main__':    
    while  True:
        name = input("Input : ")
        movie_details = sanitize(name)        
        print("Output ->", movie_details)
        print("\n")