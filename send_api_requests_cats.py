
import requests
import matplotlib.pyplot as plt
from PIL import Image
from io import BytesIO

while True:
    command = input("Press ENTER for a random cat (or Q to quit): ")

    if command.lower() == "q":
        print("Goodbye, human! MEOW!")
        break

    response = requests.get("https://cataas.com/cat", timeout=15)
    response.raise_for_status()

    cat = Image.open(BytesIO(response.content))

    plt.imshow(cat)
    plt.axis("off")

    print("MEOW! 🐱")  # A CAT HAS APPEARED!

    plt.show()
    plt.close()
