import random
import requests
import matplotlib.pyplot as plt
from PIL import Image
from io import BytesIO


def summon_cat():
    response = requests.get("https://cataas.com/cat", timeout=15)
    response.raise_for_status()

    cat = Image.open(BytesIO(response.content))

    plt.imshow(cat)
    plt.axis("off")

    print("MEOW! 🐱")

    plt.show()
    plt.close()



while True:
    choice = input("Summon a cat? (yes/no/maybe): ").strip().lower()

    if choice == "yes":
        summon_cat()

    elif choice == "maybe":
        if random.random() < 0.5:
            print("Lucky! The cat gods approve!")
            summon_cat()
        else:
            print("No cat for you! MEOW!")

    elif choice == "no":
        print("Goodbye, human!")
        break

    else:
        print("Please type yes, no, or maybe!")

