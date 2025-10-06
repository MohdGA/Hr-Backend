from models.user import UserModel


def create_test_users():
    user1 = UserModel(username="arjun_dev", email="arjun@devmail.in")
    user1.set_password("securepassword1")
    user2 = UserModel(username="emma_johnson", email="emma.johnson@email.com")
    user2.set_password("securepassword2")
    user3 = UserModel(username="fatima_ali", email="fatima.ali@mail.ae")
    user3.set_password("securepassword3")

    return [user1, user2, user3]

user_list = create_test_users()