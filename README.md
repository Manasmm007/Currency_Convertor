# Currency Converter Web App

A simple Flask-based web application for converting currencies using real-time exchange rates. The app fetches rates from the [Open Exchange Rates API](https://open.er-api.com/) and caches them locally for efficiency.

## Features
- Convert between multiple currencies
- Real-time exchange rates (with caching)
- User-friendly web interface
- Built with Flask and Bootstrap (customizable via `static/style.css`)

## Demo
![Screenshot](static/screenshot.png) <!-- Add a screenshot if available -->

## Getting Started

### Prerequisites
- Python 3.7+
- pip

### Installation
1. **Clone the repository:**
   ```bash
   git clone <your-repo-url>
   cd B
   ```
2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

### Running the App
```bash
python app.py
```
The app will be available at [http://127.0.0.1:5000](http://127.0.0.1:5000).

### Deployment
For production, use Gunicorn:
```bash
gunicorn app:app
```

## Project Structure
```
B/
├── app.py              # Main Flask app
├── utils.py            # Utility functions (API, caching)
├── rates.json          # Cached exchange rates
├── requirements.txt    # Python dependencies
├── static/
│   └── style.css       # Custom styles
├── templates/
│   └── index.html      # Main HTML template
```

## How It Works
- On startup or when rates expire, the app fetches the latest exchange rates from the API and caches them in `rates.json`.
- Users select currencies and enter an amount to convert.
- The app calculates the conversion using the cached rates and displays the result.

## Customization
- **Styling:** Edit `static/style.css` to change the look and feel.
- **Template:** Modify `templates/index.html` for UI changes.

## License
This project is licensed under the MIT License.

## Acknowledgements
- [Open Exchange Rates API](https://open.er-api.com/)
- [Flask](https://flask.palletsprojects.com/)

---
Feel free to contribute or suggest improvements!
