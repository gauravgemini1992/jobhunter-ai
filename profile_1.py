def load_profile():

    try:
        file = open("profile.txt", "r")
        profile = file.read()
        file.close()

        return profile

    except:
        return None


def save_profile(name, role, location, experience):

    file = open("profile.txt", "w")

    file.write("Name: " + name + "\n")
    file.write("Role: " + role + "\n")
    file.write("Location: " + location + "\n")
    file.write("Experience: " + experience + "\n")

    file.close()

    print("✅ Profile saved successfully!")