from pathlib import Path

import kagglehub

DATASET_NAME = "yeanzc/telco-customer-churn-ibm-dataset"

PROJECT_ROOT = Path(__file__).resolve().parents[1]
RAW_DATA_DIR = PROJECT_ROOT / "data" / "raw"

def download_data() -> None:
    """Download the Telco Customer Churn dataset from Kaggle and save it to the raw data directory."""

    RAW_DATA_DIR.mkdir(parents=True, exist_ok=True)

    path = kagglehub.dataset_download(DATASET_NAME, output_dir=str(RAW_DATA_DIR))
    print(f"Downloaded dataset to {path}")

if __name__ == "__main__":
    download_data()