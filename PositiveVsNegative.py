import glob
import os
import subprocess

def Renamer(Directory):
    os.chdir(Directory)
    png_files = glob.glob("*.png")
    for idx, file in enumerate(png_files, start=1):
        image_path = os.path.abspath(file)
        subprocess.run(["start", image_path], shell=True)  # Opens image with the default viewer
        user_input = input("Enter 'P' for Positive or 'N' for Negative: ").upper()
        if user_input == 'P':
            new_filename = f"Positive{idx}.png"
        elif user_input == 'N':
            new_filename = f"Negative{idx}.png"
        else:
            print("Invalid input. Skipping file.")
            continue
        os.rename(file, new_filename)
        print(f"Renamed {file} to {new_filename}")

# Provide the directory path as an argument to the function
directory_path = "C:\\Users\\Adam\\Repos\\ML\\ModleTraining\\MinecraftCraftingTable"
Renamer(directory_path)
