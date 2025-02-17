import os
import zipfile
import shutil
import subprocess

def extract_file(file_path):
    # Get the file name from the path
    file_name = os.path.basename(file_path)
    file_dir = os.path.dirname(file_path)
    
    # Define LocalAppData path
    local_app_data = os.environ.get('LOCALAPPDATA')
    destination_dir = os.path.join(local_app_data, "EXEMSIDecompiler", f"TheExtracted{file_name}")
    
    # Create the destination directory if it does not exist
    if not os.path.exists(destination_dir):
        os.makedirs(destination_dir)
    
    # Path to the 7-Zip executable
    seven_zip_path = r"C:\Program Files\7-Zip\7z.exe"  # Change this path if necessary
    
    # Check if file is an EXE or MSI
    if file_path.lower().endswith(".exe"):
        print(f"Extracting EXE file: {file_name}")
        try:
            # Use 7-Zip to extract EXE files with the full path to 7z
            subprocess.run([seven_zip_path, "x", file_path, f"-o{destination_dir}"], check=True)
            print(f"Success, the path is: {destination_dir}")
        except subprocess.CalledProcessError as e:
            print(f"Error: Could not extract EXE file. {e}")
    elif file_path.lower().endswith(".msi"):
        print(f"Extracting MSI file: {file_name}")
        try:
            # Use msiexec to extract the MSI content
            subprocess.run(["msiexec", "/a", file_path, f"TARGETDIR={destination_dir}"], check=True)
            print(f"Success, the path is: {destination_dir}")
        except subprocess.CalledProcessError as e:
            print(f"Error: Could not extract MSI file. {e}")
    else:
        print("Error: The file is neither an EXE nor an MSI file.")

if __name__ == "__main__":
    file_path = input("Enter the path of the EXE or MSI (e.g., C:/path/yourexe.exe or C:/path/yourmsi.msi): ").strip()

    if os.path.exists(file_path):
        extract_file(file_path)
    else:
        print("Error: The specified file does not exist.")

