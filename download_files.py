# ----------- script to download daily transaction data incrementally from the GCP bucket ---------- #

from google.cloud import storage
import os
import json
import pandas as pd

# ---------- CONFIG ----------
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = r"D:\Srijan\Project (bade wale)\Bicycle assignment\bicycle-459616-c7b815deeee9.json"

DOWNLOAD_DIR = "D:\Srijan\Project (bade wale)\Bicycle assignment\download"
CHECKPOINT_FILE = "downloaded_files.json"
BUCKET_NAME = "implemention_engineer_interviews"
PROJECT_ID = "pivotal-canto-171605"

# ---------- SETUP ----------
os.makedirs(DOWNLOAD_DIR, exist_ok=True)

# Load checkpoint
if os.path.exists(CHECKPOINT_FILE):
    with open(CHECKPOINT_FILE, "r") as f:
        downloaded_files = set(json.load(f))
else:
    downloaded_files = set()

client = storage.Client(project=PROJECT_ID)
bucket = client.bucket(BUCKET_NAME)
blobs = list(bucket.list_blobs())

# ---------- DOWNLOAD ----------
newly_downloaded = []

for blob in blobs:
    if blob.name.endswith("transactions.csv") and blob.name not in downloaded_files:
        local_path = os.path.join(DOWNLOAD_DIR, blob.name.replace("/", "_"))
        print(f"\nDownloading {blob.name} → {local_path}")
        blob.download_to_filename(local_path)

        # Validation step: ensure file is valid and not corrupted
        try:
            if os.path.getsize(local_path) < 100 * 1024:
                raise ValueError("File too small – likely incomplete.")
            
            # Optional: try loading with pandas
            pd.read_csv(local_path, nrows=5)

            # Success: mark as downloaded
            downloaded_files.add(blob.name)
            newly_downloaded.append(blob.name)
            print(f"Successfully downloaded and validated: {blob.name}")

        except Exception as e:
            print(f"Validation failed for {blob.name}: {e}")
            os.remove(local_path)  # Delete the bad file

# ---------- UPDATE CHECKPOINT ----------
if newly_downloaded:
    with open(CHECKPOINT_FILE, "w") as f:
        json.dump(list(downloaded_files), f)
    print(f"\n Updated checkpoint file with {len(newly_downloaded)} new downloads.")
else:
    print("\n No new valid files to download.")
