# README: AWS Resources Without Specific Tag Fetcher

This Python script retrieve AWS resources from various regions that do not have a specific tag. By default, the script checks for the absence of the "owner" tag, but you can easily modify it to check for any other tag by replacing "owner" with the desired tag name. The script then saves the details of these resources, including their ARN, type, and region, into a CSV file.

## Prerequisites

1. **Required Libraries** :

To install the required libraries, use pip:

```bash
pip install boto3
```

## Usage

### 1. Clone or Download the Script

Download or clone the script to your local machine.
```bash
git clone https://github.com/santoshPagire/aws_task.git
```

### 2. Modify the Script for a Custom Tag (Optional)

By default, the script checks for resources without the **"owner"** tag. If you want to check for resources without a different tag, you can modify the tag name in the script.

Find the line:

```python
if not tags or all(tag['Key'] != 'owner' for tag in tags):
```

And replace `'owner'` with your desired tag name. For example, to check for resources without the "project" tag, update it as follows:

```python
if not tags or all(tag['Key'] != 'project' for tag in tags):
```

### 3. Run the Script

Run the script using Python.

```bash
python resources_without_owner_tag.py
```

### 4. Example Output:

```bash
Fetching resources from region: us-east-1
Fetching resources from region: us-west-2
...
Data saved to aws_resources_without_owner_tag.csv
```

