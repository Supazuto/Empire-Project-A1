
from data import family_members

def show_members():
    for member in family_members :
        print(f"{member["name"]},{member["age"]},{member["role"]},{member["power"]},{member["money"]},{member["equipment"]}")


if __name__ == "__main__":
    show_members()    
