import os


def replace_strings_in_file(file_path, _from, _to):
    with open(file_path) as f:
        file_contents = f.read()

    if (modified_contents := file_contents.replace(_from, _to)) != file_contents:
        with open(file_path, "w") as f:
            f.write(modified_contents)
        print(f"Updated {file_path}")


def crawl_directory(directory, _from, _to):
    for root, _, files in os.walk(directory):
        for file_name in files:
            if file_name.endswith((".py", ".md")):
                file_path = os.path.join(root, file_name)
                replace_strings_in_file(file_path, _from, _to)


if __name__ == "__main__":
    start_directory = "/Users/max/code/governator/"  # Replace with your directory path
    crawl_directory(start_directory, "GOVERNATOR", "GOVERNATOR")
