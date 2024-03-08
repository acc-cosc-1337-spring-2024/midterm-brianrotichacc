import question_c as c


while True:
    age = int(input("Enter a person's age: ")) 
    category = c.get_person_category(age)
    print(f"The person falls in into the category of {category}.")
    keep_going = input("Do you want to continue? (Y/N): ").lower()
    if keep_going != 'y':
        exit()