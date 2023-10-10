azure_key = "YOUR_AZURE_KEY"

print(azure_key)

# Path: secret_test.py

# Genereate a random string
import random
import string


def randomString(stringLength=10):
    """Generate a random string of fixed length"""
    letters = string.ascii_lowercase
    return "".join(random.choice(letters) for i in range(stringLength))


best_key = "?sv=2022-11-02&ss=bfqt&srt=c&sp=rwdlacupiytfx&se=2023-10-11T06:24:53Z&st=2023-10-10T22:24:53Z&spr=https&sig=X%2BKypEjLTi081FeXzJqGwwbixBZEuro1e4Zi1WxKuX8%3D"

print(best_key)
