#!/usr/bin/env python3
import sys
import os
import re

def replace_idea_id(file_path, idea_id):
    """
    Replace all occurrences of the placeholder ${idea_id} with the provided idea_id
    """
    # Check if file exists
    if not os.path.exists(file_path):
        print(f"Error: File {file_path} does not exist.")
        return False
    
    try:
        # Read the file content
        with open(file_path, 'r') as file:
            content = file.read()
        
        # Replace all occurrences of "${idea_id}" with the provided idea_id
        new_content = content.replace('${idea_id}', str(idea_id))
        
        # Write the modified content back to the file
        with open(file_path, 'w') as file:
            file.write(new_content)
        
        return True
    except Exception as e:
        print(f"Error processing file {file_path}: {str(e)}")
        return False

def process_and_rename_file(file_path, idea_id):
    """
    Replace placeholders in a file and rename it if the filename contains ${idea_id}
    """
    # First replace content
    if not replace_idea_id(file_path, idea_id):
        return False
    
    # Check if filename contains the placeholder
    if '${idea_id}' in file_path:
        # Create new filename
        new_file_path = file_path.replace('${idea_id}', str(idea_id))
        
        try:
            # Rename the file
            os.rename(file_path, new_file_path)
            print(f"Renamed {file_path} to {new_file_path}")
            return True
        except Exception as e:
            print(f"Error renaming file {file_path}: {str(e)}")
            return False
    
    return True

def main():
    # Check command line arguments
    if len(sys.argv) != 2:
        print("Usage: python replace_idea_id.py <idea_id>")
        print("Example: python replace_idea_id.py 12345")
        return
    
    # Get the idea_id from command line arguments
    try:
        idea_id = int(sys.argv[1])
    except ValueError:
        print("Error: idea_id must be an integer.")
        return
    
    # Files to process
    files = [
        'docker-compose.dev.yml',
        'nginx/nginx.conf',
        '${idea_id}-v1.deepsphere.one'
    ]
    
    print(f"Replacing placeholders with idea_id: {idea_id}...")
    
    # Process each file
    for file_path in files:
        if '${idea_id}' in file_path:
            if process_and_rename_file(file_path, idea_id):
                print(f"Successfully processed and renamed {file_path}")
            else:
                print(f"Failed to process or rename {file_path}")
        else:
            if replace_idea_id(file_path, idea_id):
                print(f"Successfully processed {file_path}")
            else:
                print(f"Failed to process {file_path}")

if __name__ == "__main__":
    main() 