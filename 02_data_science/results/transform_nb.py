import os
import json
import nbformat
from nbformat.v4 import new_notebook, new_code_cell

def extract_cells_from_txt(file_path):
    """
    Extract code cells from a .txt file. 
    Content between 'EXECUTE' and 'STDOUT/STDERR' is extracted.
    """
    cells = []
    with open(file_path, 'r') as file:
        lines = file.readlines()
    
    inside_cell = False
    cell_content = []
    
    for line in lines:
        if "EXECUTE" in line:
            inside_cell = True
            cell_content = []  # Start a new cell
        elif "STDOUT/STDERR" in line:
            if inside_cell:
                cells.append("".join(cell_content).strip())
                inside_cell = False
        elif inside_cell:
            cell_content.append(line)
    
    return cells

def create_notebook_from_cells(cells, output_file):
    """
    Create a Jupyter notebook from a list of cell contents.
    """
    notebook = new_notebook()
    notebook.cells = [new_code_cell(cell) for cell in cells]
    
    with open(output_file, 'w') as f:
        nbformat.write(notebook, f)

def txt_to_ipynb(input_dir, output_dir):
    """
    Convert all .txt files in the input directory to .ipynb files in the output directory.
    """
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    for file_name in os.listdir(input_dir):
        if file_name.endswith('.txt'):
            input_file = os.path.join(input_dir, file_name)
            output_file = os.path.join(output_dir, file_name.replace('.txt', '.ipynb'))
            
            print(f"Processing {input_file}...")
            cells = extract_cells_from_txt(input_file)
            create_notebook_from_cells(cells, output_file)
            print(f"Created {output_file}")

if __name__ == "__main__":
    import argparse
    
    parser = argparse.ArgumentParser(description="Convert .txt files to Jupyter Notebooks.")
    parser.add_argument("input_dir", help="Directory containing .txt files")
    parser.add_argument("output_dir", help="Directory to save .ipynb files")
    
    args = parser.parse_args()
    txt_to_ipynb(args.input_dir, args.output_dir)
