# Fractal Visualizer

This project is a simple web application that generates and displays a visualization of the Mandelbrot set.

## Description

The application is built with Python and Flask, and it's containerized using Docker. It provides a web interface to view the fractal.

## Running the application

To run the application, you need to have Docker installed.

1. **Build the Docker image:**
   ```bash
   docker build -t fractal-visualizer .
   ```

2. **Run the Docker container:**
   ```bash
   docker run -p 5000:5000 fractal-visualizer
   ```

3. **View the fractal:**
   Open your web browser and navigate to `http://localhost:5000`. You should see the Mandelbrot set fractal.
