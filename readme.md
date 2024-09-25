## Project Overview

This project provides an OCR-based web application utilizing **Gradio** for the interface. The app uses **Tesseract** OCR for text recognition, with support from **pytesseract** and **transformers** for enhanced functionality.

## Application Features

- **Upload an image**: Users can upload images containing text. The app will extract the text using the Tesseract OCR engine.
- **Display Results**: The extracted text will be displayed directly in the Gradio interface for easy access.

## Requirements

To run this application, you'll need to install the following dependencies.

### Prerequisites

- **Python 3.8+**
- Ensure that **Tesseract-OCR** is installed in your environment. You can install it with the following command:

```
 sudo apt install tesseract-ocr
```

- Verify that `tesseract-ocr-all` is included in your installation based on the `packages.txt`.

### Install Dependencies

The `requirements.txt` lists the following Python packages:

- `gradio`
- `pytesseract`
- `Pillow`
- `transformers`
- `torch`

To install these dependencies, use:

```
pip install -r requirements.txt
```

## Setting Up the Environment

1.  **Clone or download the project repository**.
2.  **Install Tesseract-OCR**: This can be done using the following command (for Debian-based systems):

```
sudo apt-get install tesseract-ocr
```

3. **Install Python packages**: Install the dependencies listed in the `requirements.txt` file:

```
pip install -r requirements.txt
```

This command will install all necessary packages including `gradio`, `pytesseract`, `Pillow`, `transformers`, and `torch`.

4. **Verify Installation**: Check that **Tesseract** is properly installed by running:

```
tesseract --version
```

## Running the Application Locally

After setting up the environment, you can run the web application locally.

1.  **Run the Python Script**:

    Assuming the main script is `app.py`, run it with:

```
python app.py
```

2. **Access the Application**:

Gradio will spin up a web interface, and you will be provided with a local URL (e.g., `http://127.0.0.1:7860`). Open the URL in your web browser to use the app.
