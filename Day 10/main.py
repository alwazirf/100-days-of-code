# fUNCTION WITH OUTPUT
# def format_name(firstName, lastName):
#     fullName = firstName + " " + lastName
#     return fullName.title()

# multiple return
def format_name(first_name, last_name):
    """Take first and last name and format it
    to return the title case version of the name."""
    if first_name == "" or last_name == "":
        return
    full_name = first_name + " " + last_name
    return f"Result: {full_name.title()}"

print(format_name(input("what is your first name?: "), input("what is your lastname?: ")))