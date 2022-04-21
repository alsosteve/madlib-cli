import re

def read_template(path):
    with open(path, "r") as file:
        return file.read()

def parse_template(string):
    pattern = r"\{(\w+\s*\w+\s*\w+\s*\w+)\}"
    actual_stripped = re.sub(pattern, "{}", string)
    actual_parts = tuple(re.findall(pattern, string))
    return (actual_stripped, actual_parts)

def merge(string, list):
    return string.format(*list)
