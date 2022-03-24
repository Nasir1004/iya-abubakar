# def build_person(first_name, last_name, age = None):
#     person = {"first": first_name, "last": last_name}
#     if age:
#         person[age] = age
#     return person
# musician =  build_person('nasir', "sharu", age = 27)
# print(musician)

from webbrowser import get


def get_formatted_name(first_name, last_name):
    full_name = f"{first_name} {last_name}"
    return full_name.title()
while True:
    print("\nPlease tell me your name:")
    f_name = input("First name: ")
    l_name = input("Last name: ")
    formatted_name = get_formatted_name(f_name, l_name)
    print(f"\nHello, {formatted_name}!")

