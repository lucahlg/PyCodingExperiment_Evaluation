import os

def convert_crlf_to_lf(directory):
    for root, _, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            with open(file_path, 'rb') as f:
                content = f.read()
            content = content.replace(b'\r\n', b'\n')
            with open(file_path, 'wb') as f:
                f.write(content)

if __name__ == "__main__":
    directory = "./bench_items"
    convert_crlf_to_lf(directory)