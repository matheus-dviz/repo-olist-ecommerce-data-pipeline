import os
from pathlib import Path
from kaggle.api.kaggle_api_extended import KaggleApi

RAW_DIR = Path("data/raw")
DATASET = "olistbr/brazilian-ecommerce"

def download_dataset():
    RAW_DIR.mkdir(parents=True, exist_ok=True)

    api = KaggleApi()
    api.authenticate()

    api.dataset_download_files(
        dataset=DATASET,
        path=str(RAW_DIR),
        unzip=True
    )

    print("Dataset downloaded to:", RAW_DIR)

if __name__ == "__main__":
    download_dataset()
