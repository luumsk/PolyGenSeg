# PolyGenSeg

A tool for generating data for polyp semantic segmentation.

## Usage Instructions

### Step 1: Install Pipenv

Make sure you have the `pipenv` package installed.

### Step 2: Install Dependencies

Use `pipenv` to install all necessary dependencies:

```bash
pipenv install
```

### Step 3: Update Polyp JSON Paths (optional)

If your polyp images are not stored in the root directory, you need to update the paths in your polyp JSON files. By default, the script verifies that the new path points to a file. If the path does not exist, an error will be raised. To disable this verification, use the `--disable-checkpath` argument.

Run the following command to update the paths:

```bash
pipenv run python update_paths.py --json polyp_train.json polyp_valid.json polyp_test.json --newDir YOUR_DATA_DIR
```

### Arguments

- `--json`: List of JSON files to update.
- `--newDir`: The new root directory for your data.
- `--disable-checkpath`: Optional flag to disable path existence check.

Replace `YOUR_DATA_DIR` with the actual path to your data directory.