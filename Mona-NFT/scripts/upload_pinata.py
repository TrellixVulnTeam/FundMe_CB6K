import os
from pathlib import Path
import requests

PINATA_BASE_URL = "https://api.pinata.cloud/"
endpoint = "pinning/pinFileToIPFS"
filepath = "./img/pug.png"
filename = filepath.split("/")[-1:][0]
headers = {
    "pinata_api_key": os.getenv("PINATA_API_KEY"),
    "pinata_secret_api_key": os.getenv("PINATA_API_SECRET"),
}


def main():
    with Path(filepath).open("rb") as fb:
        image_binary = fp.read()
        response = requests.post(
            PINATA_BASE_URL + endpoint,
            file={"file": (filename, image_binary)},
            headers=headers,
        )
        print(response.json())


if __name__ == "__main__":
    main()
