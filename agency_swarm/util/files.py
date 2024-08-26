import mimetypes

code_interpreter_types = [
    "application/csv", "image/jpeg", "image/gif", "image/png",
    "application/x-tar", "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
    "application/xml", "text/xml", "application/zip"
]

dual_types = [
    "text/x-c", "text/x-csharp", "text/x-c++", "application/msword",
    "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
    "text/html", "text/x-java", "application/json", "text/markdown",
    "application/pdf", "text/x-php",
    "application/vnd.openxmlformats-officedocument.presentationml.presentation",
    "text/x-python", "text/x-script.python", "text/x-ruby", "text/x-tex",
    "text/plain", "text/css", "text/javascript", "application/x-sh",
    "application/typescript"
]

def determine_file_type(file_path):
    mime_type, _ = mimetypes.guess_type(file_path)
    if mime_type:
        if mime_type in code_interpreter_types:
            return "assistants.code_interpreter"
        elif mime_type.startswith('image/'):
            return "vision"
        elif mime_type in dual_types:
            return "assistants.file_search"
    raise ValueError(f"Unsupported file type: {mime_type}")

def get_tools(file_path):
    mime_type, _ = mimetypes.guess_type(file_path)
    if mime_type in code_interpreter_types:
        return [{"type": "code_interpreter"}]
    elif mime_type in dual_types:
        return [{"type": "code_interpreter"}, {"type": "retrieval"}]
    else:
        raise ValueError(f"Unsupported file type: {mime_type}")