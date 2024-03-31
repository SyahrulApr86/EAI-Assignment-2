
# Assignment 2 - Consume API
## Enterprise Application Integration - Even Semester 2023/2024

This Flask application demonstrates how to consume two different APIs:
- The Cat API for fetching random cat images.
- OpenWeatherMap API for fetching daily weather summaries based on date and location.

### APIs Documentation

#### 1. [The Cat API](https://thecatapi.com/)

#### 2. [OpenWeatherMap API](https://openweathermap.org/api)

### How to Run This Project

1. Ensure you have Python installed on your system.

2. Clone this repository to your local machine.

3. Navigate to the project directory and install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run the Flask application:
   ```bash
   flask run
   ```

5. Access the application via web browser:
   - Home Page: `http://127.0.0.1:5000/`
   - Random Cat Image: `http://127.0.0.1:5000/cat`
   - Daily Weather Summary: `http://127.0.0.1:5000/daily_summary`

### Notes

- Ensure you have an internet connection as this application consumes real-time data from external APIs.
- Replace the placeholder API keys in the source code with your own valid keys to fetch data successfully.

For more detailed information on how to obtain API keys and use these APIs, please refer to their official documentation.
