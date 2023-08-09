# PDF Speaker Program

The PDF Speaker Program is a Python script that allows you to interact with PDF files in different ways. It provides several options, including reading specific pages, navigating through pages, and breaking the program.
This README will guide you through the features and how to use them effectively.

## Features

1. **Show Index**: Displays an index of the available options. While not always accurate, it provides a quick reference for the available functionalities.

2. **Read Specific Page**: Allows you to read the content of a single specified page within the PDF.

3. **Start from Specific Page to Last Page**: Reads the content starting from a specific page and continues reading until the last page of the PDF.

4. **Exit Program**: Terminates the PDF Speaker Program.

## Getting Started

1. Clone or download the repository to your local machine.

2. Install the required Python dependencies. This program uses the following libraries:

3.  `PyPDF2` for working with PDF files.


 -----  You can install them using the following command:
   
   pip install PyPDF2
   pip install pyttsx3

4. Run the program:

## Usage

Upon running the program, you will be presented with the following options:

1. **Show Index**: Display a simple index of the available options.
2. **Read Specific Page**: Enter the page number you want to read. The program will display the text content of that page.
3. **Start from Specific Page to Last Page**: Enter the page number you want to start reading from. The program will read the content from that page to the last page.
4. **Exit Program**: Terminate the program.

Follow the on-screen prompts and provide the required input when prompted.

## Note

- The accuracy of text extraction from PDFs may vary based on the quality and formatting of the PDF. Complex layouts may lead to less accurate text extraction.
- The program uses the `PyPDF2` library for reading PDFs. Be aware that certain PDF features may not be supported or extracted accurately.

## Contributing

Contributions to this project are welcome! Feel free to fork the repository, make improvements, and submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).

---

Feel free to modify and expand this template according to your program's structure and additional details you want to include.
Make sure to replace placeholders like `enter your pdf path name` with the actual filename of your program and provide accurate instructions for running the program and installing dependencies.
