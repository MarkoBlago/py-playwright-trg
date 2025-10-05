import random
import string


class Utility:
    def generate_random_name(self):
        
        listOfRandomLetters = random.choices(string.ascii_letters, k=6)
        randomLetters = ''.join(listOfRandomLetters)

        listOfRandomNumbers = random.choices(string.digits, k=3)
        randomNumbers = ''.join(listOfRandomNumbers)

        combinedString = randomLetters + randomNumbers

        reversedString = ''.join(reversed(combinedString))

        return reversedString