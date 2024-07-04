import chardet


def detect_file_encoding(file_path):
    if file_path is not None:
        with open(file_path, 'rb') as f:
            rawdata = f.read()
        result = chardet.detect(rawdata)
        return 'utf-8' if result['encoding'] == 'ascii' else result['encoding']
    return 'utf-8'
