**--- Authored by Siddarth Singotam on 05.12.2024 ---**

# Finnish Translation App

This is a simple Flask application that translates text from English to Finnish using the [Helsinki-NLP Opus-MT](https://huggingface.co/Helsinki-NLP/opus-mt-en-fi) model provided by Hugging Face's Transformers library.

## Features
- Input an English text string in a web form.
- Translate the input text to Finnish using a pre-trained machine translation model.
- Display the translated text in real time.

## Installation

### Prerequisites
- Python 3.8 or higher
- `pip` package manager

### Steps
1. Clone this repository:
   ```bash
   git clone <repository_url>
   cd Live-AI-Finnish-Translator
   ```

2. Create a virtual environment (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install flask transformers torch
   ```

## Own Usage
1. Run the app:
   ```bash
   python app.py
   ```

2. Access the application:
   Open your web browser and navigate to [http://127.0.0.1:5000/](http://127.0.0.1:5000/).

3. Translate text:
   - Enter English text in the text box.
   - Click "Translate."
   - View the Finnish translation displayed on the page.

## Project Structure
```
flask_translation_app/
├── app.py                 # Main Flask app
├── static/
│   └── styles.css         # CSS styling for the project
├── templates/
│   └── index.html         # HTML template for the web interface
├── requirements.txt       # List of dependencies
├── README.md              # Project documentation (this file)
```

## API Endpoints

### `/`
- **Method**: `GET`
- **Description**: Serves the main page of the application.

### `/translate`
- **Method**: `POST`
- **Description**: Translates the input English text to Finnish.
- **Request Body**: 
  - Form field: `text` (string)
- **Response**:
  - On success: `{ "translated_text": "..." }`
  - On error: `{ "error": "..." }`

## Example
### Input:
```
Hello, how are you?
```

### Output:
```
Hei, kuinka voit?
```

## Dependencies
- **Flask**: Python web framework for serving the app.
- **Transformers**: Library for accessing the Helsinki-NLP translation model.
- **Torch**: Required for the Hugging Face Transformers library.

Install all dependencies using: (Install other dependencies if necessary)
```bash
pip install -r requirements.txt
```

## Notes
- Ensure that your Python version is compatible with the Hugging Face Transformers library.
- For production, consider using a WSGI server like Gunicorn to serve the app.

