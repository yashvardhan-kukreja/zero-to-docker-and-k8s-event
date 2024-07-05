# Mandelbrot ASCII Visualization

This project generates an ASCII representation of the Mandelbrot set and displays it in the terminal. The script uses Python to compute and render the set, with enhanced visuals using the `rich` library.

## Prerequisites

To run this project, you need the following software installed on your computer:

1. Python (version 3.6 or higher)
2. Pip (Python package installer)

## Installation Guide

### Step 1: Install Python

#### Windows

1. Download the Python installer from the official [Python website](https://www.python.org/downloads/).
2. Run the installer and follow the setup steps.
3. Make sure to check the box that says "Add Python to PATH" during installation.
4. Verify the installation by opening a command prompt and running:
   ```sh
   python --version
   ```

#### macOS

1. Open the Terminal.
2. Install Homebrew if you don't have it already:
   ```sh
   /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
   ```
3. Install Python using Homebrew:
   ```sh
   brew install python
   ```
4. Verify the installation:
   ```sh
   python3 --version
   ```

#### Linux

1. Open the Terminal.
2. Update the package list:
   ```sh
   sudo apt update
   ```
3. Install Python:
   ```sh
   sudo apt install python3 python3-pip
   ```
4. Verify the installation:
   ```sh
   python3 --version
   ```

### Step 2: Set Up a Virtual Environment

It's a good practice to use a virtual environment to manage project dependencies.

1. Open a terminal or command prompt.
2. Create a new directory for the project and navigate into it:
   ```sh
   mkdir mandelbrot-ascii
   cd mandelbrot-ascii
   ```
3. Create a virtual environment:
   ```sh
   python3 -m venv venv
   ```
4. Activate the virtual environment:

   - On Windows:
     ```sh
     venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```sh
     source venv/bin/activate
     ```

### Step 3: Install Required Python Packages

Install the necessary Python packages using pip.

1. Install the `rich` library:
   ```sh
   pip install rich
   ```

### Step 4: Run the Script

1. Ensure the virtual environment is activated.
2. Run the Python script:
   ```sh
   python mandelbrot.py
   ```

You should see an ASCII visualization of the Mandelbrot set in your terminal, updating and zooming in every 5 seconds.

## Summary

Running this project from scratch involves:
- Installing Python and pip.
- Setting up a virtual environment.
- Installing required Python packages.
- Creating and running the Python script.

While these steps are manageable, they demonstrate the multiple installations and configurations needed to run a simple script. Using Docker can simplify this process by encapsulating all dependencies and configurations within a container, making it easier to run applications consistently across different environments.
