
# Weather App using OpenWeatherMap API in Django

This Weather App is a web application built with Django and integrated with the OpenWeatherMap API to provide real-time weather information. This README file will provide an overview of the Weather App, instructions on how to set it up, and information about its features.


## Features

- **Current Weather**: Provides current weather information, including temperature, humidity, wind speed, and conditions, for a specified location.

- **Weather Forecast**: Displays a 5-day weather forecast for the selected location, including temperature and weather conditions for each day.

- **Location Search**: Allows users to search for weather information for different locations worldwide.

- **Responsive Design**: The app is designed to work on both desktop and mobile devices, providing an optimal user experience.

## Installation

Before setting up the Weather App, ensure you have Python and Django installed on your system. If not, you can install Django using `pip`:

```bash
pip install django
```

Once you have Django installed, follow these steps to set up the Weather App:

1. Clone the repository or download the source code to your local machine.

2. Change to the project directory:

   ```bash
   cd weather_app
   ```

3. Run the migrations to create the database:

   ```bash
   python manage.py migrate
   ```

4. Start the Django development server:

   ```bash
   python manage.py runserver
   ```

5. Access the Weather App in your web browser at `http://localhost:8000` or the address specified by the development server.

## Configuration

To configure the Weather App to work with the OpenWeatherMap API, follow these steps:

1. Create an OpenWeatherMap API Key by signing up at [https://openweathermap.org/api](https://openweathermap.org/api).

2. Open the `settings.py` file in the project directory.

3. Find the `OPENWEATHERMAP_API_KEY` variable and replace `"YOUR_API_KEY"` with your actual OpenWeatherMap API key.

   ```python
   OPENWEATHERMAP_API_KEY = "YOUR_API_KEY"
   ```

4. Save the `settings.py` file.

## Usage

1. Open the Weather App in your web browser.

2. Enter a location in the search bar and click the "Search" button.

3. The app will display the current weather and a 5-day weather forecast for the selected location.

4. You can search for weather information for different locations by entering new locations in the search bar.

## Code Structure

The code for the Weather App is structured as a Django project with the following key components:

- `weatherapp/`: The main Django app that contains views, templates, and the app's logic.

- `weatherapp/templates/`: HTML templates for rendering the app's pages.

- `weatherapp/views.py`: Defines the views and API calls to fetch weather data from the OpenWeatherMap API.

- `weatherapp/forms.py`: Contains forms for location input.

## Contributing

If you'd like to contribute to the Weather App or improve its features, you are welcome to fork the repository, make your changes, and submit a pull request.

## License

This project is licensed under the MIT License. You are free to use, modify, and distribute the code as long as you adhere to the terms of the license. See the LICENSE file for more details.
