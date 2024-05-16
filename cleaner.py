import os
import shutil

directory_path = ""
def SearchAndDelete(root):
    for root_directory, subdirs, files in os.walk(root):
        for subdir in subdirs:
            # Check if we are in system32 to avoid touching it
            if 'system32' in root_directory.lower():
                continue

            # Check if the subdir name contains 'cache' or 'Cache'
            if 'cache' in subdir or 'Cache' in subdir:
                directory_path = os.path.join(root_directory, subdir)
                print(f"Attempting to delete: {directory_path}")
                try:
                    shutil.rmtree(directory_path)
                    print(f"Deletion successful: {directory_path}")
                except PermissionError:
                    print(f"Cannot delete {directory_path}: resource is in use")
                except Exception as e:
                    print(f"Error deleting {directory_path}: {e}")

