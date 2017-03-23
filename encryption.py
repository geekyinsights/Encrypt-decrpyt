import random
import string


def plaintext_decoded(text):

    # converts text to a list
    encryption = []
    decrypted_list = list(text)

    for letter in decrypted_list:
        # Generates a random string of lower letters and numbers
        # This is a better method than creating an array of letters and numbers and randomly selecting from those

        char = string.ascii_lowercase + string.digits

        # generates a random length
        length = random.randint(0,9)

        # creates a sample
        rand_gen = random.sample(char, length)

        # Joins on the space to make the random characters a list
        rand_gen_join =  " ".join(rand_gen)

        # Concatenates all of the elements together and appends to list
        new_letter = str(len(rand_gen)) + rand_gen_join + str(letter)

        # Eliminates all whitespace and then appends the result to the list encryption
        new_letter = new_letter.replace(' ', '')
        encryption.append(new_letter)

        # Joins each element in the list to a string
        encrypted_text = ''.join(encryption)
    return encrypted_text


# ask for input then calls the function
user_input = input(" Give me a string to encode:")
print(plaintext(user_input))
