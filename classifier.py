import os
import shutil

# Define the source and destination directories
source_dir = "./persebaran"
destination_dir = "./sorted"

# Define the prefix-folder mapping
prefix_mapping = {
    "TIF": "TIF",
    "TKB": "TKB",
    "TKE": "TKB",
    "TKU": "TKU",
    "UNU": "UNU",
    "FIU": "FIU"
}

# Loop through each subfolder in the source directory
for semester_folder in os.listdir(source_dir):
    semester_path = os.path.join(source_dir, semester_folder)
    
    # Skip if it's not a directory
    if not os.path.isdir(semester_path):
        continue
    
    # Loop through each file in the semester folder
    for file_name in os.listdir(semester_path):
        file_path = os.path.join(semester_path, file_name)
        
        # Get the first three letters of the file name
        prefix = file_name[:3]
        
        # Find the destination folder based on the prefix
        destination_folder = prefix_mapping.get(prefix)
        
        # Skip if the prefix is not recognized
        if not destination_folder:
            continue
        
        # Create the destination directory if it doesn't exist
        dest_folder_path = os.path.join(destination_dir, destination_folder, semester_folder)
        os.makedirs(dest_folder_path, exist_ok=True)
        
        # Copy the file to the destination folder
        dest_file_path = os.path.join(dest_folder_path, file_name)
        shutil.copy(file_path, dest_file_path)
        
print("Files copied successfully!")