
from data import family_members

def search_member(target_name):
    target_name = target_name.lower() 
    for member in family_members :
        if member["name"].lower() == target_name :
            return target_name
    return None
    
if __name__ == "__main__":
    print(search_member("tony"))       
    print(search_member("ไม่มีคนนี้"))   