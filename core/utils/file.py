import re

def valid_filename(input_string: str) -> str:
    """ Transform string to valid file name. (Source: ChatGPT) """

    # Remove File Extension
    cleaned_string = input_string.split(".")[0]
    # Remove LaTeX specific symbols
    cleaned_string = re.sub(r'[${}\\]', '', cleaned_string)
    # Replace special characters with underscores
    cleaned_string = re.sub(r'[^\w\s-]', '', cleaned_string)
    # Replace spaces and hyphens with underscores
    cleaned_string = re.sub(r'[\s-]+', '_', cleaned_string)
    # Ensure the filename is lowercase (optional)
    cleaned_string = cleaned_string.lower()
    # Trim leading and trailing underscores
    cleaned_string = cleaned_string.strip('_')

    return cleaned_string