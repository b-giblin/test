import os

def rename_files(directory_path, prefix):
  files = os.listdir(directory_path) # Get a list of all files in the directory
  
  count = 1 # counter for numbering of files

  for filename in files:
    filename_extension = os.path.splitext(filename)[1] # extract the file extension
    new_name = f"{prefix}_{count}{filename_extension}"
    source = os.path.join(directory_path, filename) # construct the source path
    destination = os.path.join(directory_path, new_name) # construct the destination path

    os.rename(source, destination) # rename the file

    count += 1

  print(f"Renamed {count-1} files in {directory_path} with prefix '{prefix}'.")


# Define the path and desired prefix
dir_path = input("Enter the directory path: ").strip()
prefix = input("Enter the desired prefix: ").strip()

rename_files(dir_path, prefix)