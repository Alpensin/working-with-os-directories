import logging
import os
import re
import sys

SEARCH_FOLDER = "."
RESULT_FILE = os.path.join(SEARCH_FOLDER, "comments.txt")
COMMENTS_COLLECTION_SETUP = {
    "html": r"<!--\s*(.*)-->",
    "css": r"/\*\s*(.*)\*/",
    "js": r"//\s*(.*)",
}

logging.basicConfig(
    format="%(asctime)s, %(levelname)s, %(name)s, %(message)s",
    level=logging.INFO,
    stream=sys.stdout,
)


def search_in_files(cur_dir, files_list):
    results = dict()
    for file in files_list:
        if os.path.basename(file).split(".")[-1] in COMMENTS_COLLECTION_SETUP:
            filepath = os.path.join(cur_dir, file)
            with open(filepath, "r", encoding="utf8") as f:
                comments_collection = [
                    re.search(pattern, line).group(1)
                    for pattern in COMMENTS_COLLECTION_SETUP.values()
                    for line in f
                    if re.search(pattern, line)
                ]
            if comments_collection:
                results[file] = comments_collection
    return results


def walker(directory: str = "."):
    structure = os.walk(directory)
    results = dict()
    for folder in structure:
        cur_dir, folders_list, files_list = folder
        results.update(search_in_files(cur_dir, files_list))
    return results


if __name__ == "__main__":
    try:
        with open(RESULT_FILE, "w", encoding="utf8") as f:
            results = walker(SEARCH_FOLDER)
            for file, comments in results.items():
                f.write(f"{'='*20}\n{file}:\n")
                f.write("\n".join(comments))
                f.write(f"\n{'='*20}")
    except Exception as e:
        logging.exception(e)
        raise
