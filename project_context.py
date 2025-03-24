import os
import sys
from pathlib import Path
import pathspec

# Adjust this to the file name for the output file
OUTPUT_FILENAME = "project_context.md"

def load_gitignore_patterns(root_dir):
    gitignore_file = os.path.join(root_dir, ".ignore")
    if os.path.exists(gitignore_file):
        with open(gitignore_file, "r") as f:
            patterns = f.read().splitlines()
        # Create a pathspec from gitignore patterns
        spec = pathspec.PathSpec.from_lines("gitwildmatch", patterns)
        return spec
    return None

def should_ignore(file_path, spec, root_dir):
    # Get the relative path from the root directory
    rel_path = os.path.relpath(file_path, root_dir)
    # Check if the file should be ignored
    if spec and spec.match_file(rel_path):
        return True
    return False

def collect_project_context(root_dir):
    spec = load_gitignore_patterns(root_dir)
    project_data = []
    
    # Walk through the project directory
    for dirpath, dirnames, filenames in os.walk(root_dir):
        # Skip hidden directories like .venv or any directory matched by .gitignore
        # Copy dirnames so we can modify the list in-place to skip ignored directories
        for dirname in list(dirnames):
            full_dir_path = os.path.join(dirpath, dirname)
            if should_ignore(full_dir_path, spec, root_dir):
                dirnames.remove(dirname)

        for filename in filenames:
            full_path = os.path.join(dirpath, filename)
            if should_ignore(full_path, spec, root_dir):
                continue

            try:
                with open(full_path, "r", encoding="utf-8") as f:
                    content = f.read()
            except Exception as e:
                # Skip binary or unreadable files
                content = f"<<Cannot read file: {e}>>\n"
            
            rel_path = os.path.relpath(full_path, root_dir)
            project_data.append((rel_path, content))
    return project_data

def write_project_context(output_file, project_data):
    with open(output_file, "w", encoding="utf-8") as f:
        for file_path, content in project_data:
            # Write a header with the file path
            f.write(f"```{file_path.split(".")[-1]}\n")
            f.write(f"# filename: {file_path}\n")
            f.write(content)
            f.write("```\n\n")

def main():
    # You can set your project root to the current directory or specify a path.
    project_root = os.getcwd()
    project_data = collect_project_context(project_root)
    write_project_context(OUTPUT_FILENAME, project_data)
    print(f"Project context written to {OUTPUT_FILENAME}")

if __name__ == "__main__":
    main()
