
<!-- PROJECT SHIELDS -->
[![LinkedIn][linkedin-shield]][linkedin-url]

<!-- PROJECT LOGO -->
<div align="center">
   <h1>Weather WebApp  <img src="https://www.flaticon.com/svg/static/icons/svg/2937/2937985.svg" width="25px"> </h1>
   
  <p align="center">
    <br />
    <a href="https://github.com/flaviagfigueiredo/WeatherApp/tree/master/weather_django"><strong>Explore the docs »</strong></a>
    <br />
    <br />
  </p>
</p>
</div>

<!-- TABLE OF CONTENTS -->
## Table of Contents

* [About the Project](#about-the-project)
  * [Built With](#built-with)
* [Getting Started](#getting-started)
  * [Prerequisites](#prerequisites)
  * [Installation](#installation)
* [Usage](#usage)



<!-- ABOUT THE PROJECT -->
## About The Project

![Screenshot From Project](https://github.com/flaviagfigueiredo/Weather-App/blob/master/webpage.png?raw=true)


This project consists on a webpage where you can compare various weather informations (such as temperature (Celsius), sunrise time and sunset time) from different Portuguese cities in a graphics display. You'll be able to analyze the temperature of all the selected cities side by side in a bar chart and also compare the time for sunset and sunrise in those locations in a dataTable.


#### Visual Identity

<div align="center"><img src="https://github.com/flaviagfigueiredo/Weather-App/blob/master/colorpalette.png?raw=true"></div>


The color palette choice for this webpage was selected with the intent of representing the idea of weather elements (different shades of blue serving as the sky and shades of yellow and orange representing the sun).

### Built With
* [Bootstrap](https://getbootstrap.com)
* [JQuery](https://jquery.com)
* [Django](https://www.djangoproject.com/)
* [OpenWeatherMap](https://openweathermap.org/) 
* [FontAwesome](https://fontawesome.com/)
* [ApexCharts](https://apexcharts.com/)
* [DataTable](https://datatables.net/)
* ...


<!-- GETTING STARTED -->
## Getting Started

### Prerequisites

In order to run this project, you need to install the [last version of Docker](https://docs.docker.com/get-docker/) for your operating system.  
Before moving on to the next step, be sure that you [**start your Docker daemon properly.**](https://docs.docker.com/config/daemon/systemd/)

### How to run

There is a [Dockerfile](./weather_django/Dockerfile) inside the [weather_django](./weather_django) folder.  
To build the Docker image, just execute the following commands:  

```console
$ cd weather_django
$ docker build -t weather-django-image .
```

**Note:** Be sure that you have administrator privileges to execute this commands.  

After building the Docker image, just execute the following command to run the application:  

```console
$ docker run -p 8000:8000 weather-django-image
```

Finally, access this application on [http://localhost:8000](http://localhost:8000).


<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=flat-square&logo=linkedin&colorB=555
[linkedin-url]: https://www.linkedin.com/in/flavia-figueiredo/
