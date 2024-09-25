import gradio as gr
import pytesseract
from PIL import Image

# Function to extract text using pytesseract
def extract_text(image_path):
    img = Image.open(image_path)
    # Extract text in both Hindi and English
    text = pytesseract.image_to_string(img, lang='eng+hin')  # Support for English and Hindi
    return text

# Function to return extracted text
def extract_text_formatted(image_path):
    text = extract_text(image_path)
    formatted_text = text.strip()  # Remove leading/trailing spaces
    return formatted_text

# Function to search for a keyword within the extracted text
def search_within_text(text, keyword):
    if keyword in text:
        highlighted = text.replace(keyword, f"<mark>{keyword}</mark>")
    else:
        highlighted = "Keyword not found"
    return highlighted

# Web app definition using Gradio
def web_app():
    with gr.Blocks() as demo:
        image_input = gr.Image(label="Upload Image", type="filepath")
        extract_button = gr.Button("Extract Text")
        extracted_output = gr.Textbox(label="Extracted Text", lines=10)
        keyword_input = gr.Textbox(label="Keyword Search")
        search_button = gr.Button("Search Keyword")
        search_output = gr.HTML(label="Search Results")
        
        # Button click triggers OCR text extraction and formatting
        extract_button.click(fn=extract_text_formatted, inputs=image_input, outputs=extracted_output)
        
        # Button click triggers keyword search within extracted text
        search_button.click(fn=search_within_text, inputs=[extracted_output, keyword_input], outputs=search_output)

    # Launch the app
    demo.launch()

if __name__ == "__main__":
    web_app()
