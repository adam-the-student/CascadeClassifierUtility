import os

def create_png_list_txt(folder_path, output_file):
    png_files = [file for file in os.listdir(folder_path) if file.lower().endswith('.png')]
    with open(output_file, 'w') as f:
        for png_file in png_files:
            png_path = os.path.join(folder_path, png_file)
            f.write(png_path + '\n')

def main():
    positive_folder = input("Enter the path to the positive folder: ")
    negative_folder = input("Enter the path to the negative folder: ")
    
    positive_output_file = os.path.join(positive_folder, "positive_png_paths.txt")
    negative_output_file = os.path.join(negative_folder, "negative_png_paths.txt")
    
    create_png_list_txt(positive_folder, positive_output_file)
    create_png_list_txt(negative_folder, negative_output_file)
    
    print(f"Positive PNG paths written to '{positive_output_file}'.")
    print(f"Negative PNG paths written to '{negative_output_file}'.")

if __name__ == "__main__":
    main()
