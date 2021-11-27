from instagramy import InstagramUser

USERS = ['imalisajid_']


def scrap_user(usr):
    user = InstagramUser(usr)
    print('FullName:', user.fullname)
    print('Biography', user.biography)

    print('Followers:', user.number_of_followers)
    print('Following:', user.number_of_followings)
    print('Posts:', user.number_of_posts)

    print("=======================================")


if __name__ == '__main__':
    for user in USERS:
        scrap_user(user)
