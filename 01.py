def get_full_name(first_name:str,last_name:str):
    full_name = first_name + last_name
    return full_name
print(get_full_name('angel','white'))
def get_name_with_age(name:str,age:int):
    name_with_age = name + 'is this old'+ str(age)
    return name_with_age
print(get_name_with_age('wicky',18))
class person:
    def __init__(self,name:str):
        self.name = name
def get_person_name(one_person:person):
    return one_person.name