class User:
    def __init__(self, user_id, username):
        self.id = user_id
        self.username = username
        self.followers = 0 #initalize atribute using default value
        self.following = 0
        print("new user being created ... ")
        
    def follow(self, user):
        user.followers += 1
        self.following += 1

user1 = User("001", "Alwa")
user2 = User("002", "Fitrah")

user1.follow(user2)

print(user1.following)
print(user1.followers)

print(user2.followers)
print(user2.following)

# user1.name = "Alwa"

# print(user1.username)
# print(user1.followers)