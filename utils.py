import os, shutil

def get_files(path: str) -> list:
    all_files = os.listdir(path)
    print("\nEVERY FILES: ", len(all_files))
    files = [file for file in all_files if not os.path.isdir(os.path.join(path, file))]
    print(f"ORGANISER FOUND FILES: {len(files)}\n\n")
    return files
def get_extension(file: str) -> str:
    _, ext = os.path.splitext(file)
    return ext

DEFAULT_CATEGORY = "UNKNOWN"

categories = {
        ".png": "PHOTOS",
        ".py": "PYTHON",
        ".txt": "TEXT",
    }

def get_category(ext: str) -> str:
    return categories.get(ext, DEFAULT_CATEGORY)
def show_report(path):
    files = get_files(path)
    count_files = {}
    for file in files:
        ext = get_extension(file)
        category = get_category(ext)
        print(f"{file}: {category}")

        if ext in count_files:
            count_files[ext] += 1
        else:
            count_files[ext] = 1

    print("Moved files:\n")
    for ext, count in count_files.items():
        print(f"{ext.upper().strip(".")} -> {count}")

def organiser(input_path: str, output_path: str) -> None:
    files = get_files(input_path)

    for file in files:
        ext = get_extension(file)

        print(f"\nfile name: {file}")

        category = get_category(ext)
        category_folder = os.path.join(output_path, category)

        if not os.path.exists(category_folder):
            os.makedirs(category_folder, exist_ok=True)

        full_input_path = os.path.join(input_path, file)

        full_output_path = os.path.join(category_folder, file)

        if os.path.exists(full_output_path):
            print("File already organised❗❗❗\n")
            continue
        shutil.move(full_input_path, full_output_path)
    print("Organiser complete.🤖")


