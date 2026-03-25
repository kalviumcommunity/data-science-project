# Data Organization Dictionary

To ensure reproducibility and prevent data corruption, this project strictly separates data stages:

* **`/raw`**: This is the immutable, original source data. **Files in this folder must NEVER be modified, cleaned, or overwritten.** Treat it as read-only evidence.
* **`/processed`**: This contains cleaned, transformed datasets ready for modeling. If these files are deleted, they can always be perfectly recreated by running our scripts on the `/raw` data.
* **`../outputs`**: This folder sits outside the data directory. It holds final artifacts like trained Machine Learning models, exported charts (`/figures`), and prediction reports.