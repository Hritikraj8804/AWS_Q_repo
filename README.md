# Hinglish Motivational Quotes

A simple Flask web application that displays random motivational quotes in Hinglish (a blend of Hindi and English).

## Features

- Displays a random motivational quote in Hinglish with English translation
- Clean, responsive user interface
- One-click refresh to get a new quote

## Technologies Used

- **Backend**: Python with Flask
- **Frontend**: HTML, CSS
- **Templating**: Jinja2

## Installation

1. Clone this repository:
   ```
   git clone https://github.com/Hritikraj8804/AWS_Q_repo.git
   cd AWS_Q_repo
   ```

2. Create and activate a virtual environment (recommended):
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install the required dependencies:
   ```
   pip install flask
   ```

## Usage

1. Run the application:
   ```
   python app.py
   ```

2. Open your web browser and navigate to:
   ```
   http://localhost:5000
   ```

3. Click the "Get Another Quote" button to display a new random quote.

## Project Structure

```
.
├── app.py              # Flask application with routes and quote data
├── templates/
│   └── index.html      # HTML template for the web interface
└── README.md           # This file
```

## How It Works

The application uses Flask to serve a web page that displays motivational quotes. When a user visits the site:

1. The Flask backend selects a random quote from a predefined list
2. The quote is passed to the HTML template using Jinja2
3. The template renders the quote in a visually appealing format
4. Users can refresh the page or click the button to get a new quote

## Customization

To add or modify quotes, edit the `quotes` list in `app.py`.

## Author

Hritik Raj

## Acknowledgments

- Inspiration for Hinglish quotes from various sources
