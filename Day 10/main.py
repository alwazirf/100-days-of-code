# fUNCTION WITH OUTPUT
# def format_name(firstName, lastName):
#     fullName = firstName + " " + lastName
#     return fullName.title()

# multiple return
def format_name(firstName, lastName):
    """Take first and last name and format it
    to return the title case version of the name."""
    if firstName == "" or lastName == "":
        return
    fullName = firstName + " " + lastName
    return f"Result: {fullName.title()}"

print(format_name(input("what is your first name?: "), input("what is your lastname?: ")))