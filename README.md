# EXEMSIExtractor
Overview
EXEMSIExtractor is a Python-based application that helps extract the contents of executable (.exe) and Microsoft Installer (.msi) files by converting them into ZIP archives. This tool simplifies the process of accessing files contained within EXE or MSI installers without running the installer or worrying about Windows Explorer's inability to view the contents.

Features:
Extract EXE/MSI files: Supports extraction of both .exe and .msi files into accessible folders.
Automatic Folder Creation: After extraction, the app generates a new folder with the same name as the original file inside %LocalAppData%.
Error-Free Extraction: Handles the extraction process to avoid common issues where Windows cannot display or interact with files inside certain EXE/MSI archives.
Simple Interface: Users just need to enter the path of the EXE or MSI file to begin the extraction.
No Need for 7-Zip for MSI: MSI files are automatically extracted without needing 7-Zip.
How to Use:
Start the Application: Run the EXEMSIExtractor executable file (EXEMSIDecompiler.exe).

Enter the File Path: You will be prompted to enter the path of the EXE or MSI file you wish to extract. Example input:

C:/path/to/yourfile.exe
C:/path/to/yourfile.msi
Extraction Process:

For EXE files: EXEMSIExtractor will use 7-Zip to extract the contents of the EXE file. Ensure that 7-Zip is installed and referenced in the application. If it's not found, you will receive an error message prompting you to install 7-Zip.
For MSI files: MSI files are automatically extracted without the need for 7-Zip. The app will handle the extraction process seamlessly.
Completion: Once the extraction is complete, the app will display a success message:

css
Copy
Edit
Success! The files have been extracted to:
%LocalAppData%\EXEMSIDecompiler\YourFileName
Requirements:
7-Zip: EXEMSIExtractor requires 7-Zip to extract EXE files. Ensure that 7-Zip is installed and properly referenced in the application. If 7-Zip is not found, it will trigger an error.

Python 3.x: EXEMSIExtractor is built using Python and requires Python 3.x to run. However, once compiled with PyInstaller, it can run as a standalone .exe.

Troubleshooting:
File Not Found Error: If you encounter errors related to missing files (like 7z.exe), ensure that 7-Zip is installed and the correct path is set in the application. You can manually specify the path to 7z.exe in the subprocess call if needed.

Permission Issues: Ensure you have proper permissions to access the directories involved, especially when extracting to %LocalAppData%.

Example Usage:
For an example of how to use the tool, follow these steps:

Enter the path of an EXE or MSI file when prompted.
Wait as the extraction process occurs.
Once completed, navigate to the extraction folder in %LocalAppData% to view the contents.
Contact and Support:
For more information or to report any issues, please contact the developer at [Your Contact Information or GitHub Repository URL].

Key Points:
7-Zip is only required for EXE files.
MSI files are automatically handled by the app without requiring 7-Zip.
The extracted files are saved to %LocalAppData%\EXEMSIDecompiler\<filename>.
