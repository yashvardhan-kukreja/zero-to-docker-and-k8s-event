
# Hello World website

This is a simple "Hello World" web application built with Node.js and Express. This guide provides the steps to install and run the application from scratch.

## Prerequisites

- Node.js (version 14.x recommended)
- npm (Node Package Manager)

## Getting Started

### Step 1: Install Node.js and npm

If you don't have Node.js and npm installed, you will need to install them. Here are the steps for different operating systems:

#### Windows

1. Download the Node.js installer from [nodejs.org](https://nodejs.org/).
2. Run the installer and follow the setup steps.
3. Verify the installation by opening a command prompt and running:
   ```sh
   node -v
   npm -v
   ```

#### macOS

1. Install Homebrew if you don't have it already:
   ```sh
   /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
   ```
2. Install Node.js and npm:
   ```sh
   brew install node
   ```
3. Verify the installation:
   ```sh
   node -v
   npm -v
   ```

#### Linux

1. Update your package index:
   ```sh
   sudo apt update
   ```
2. Install Node.js and npm:
   ```sh
   sudo apt install nodejs npm
   ```
3. Verify the installation:
   ```sh
   node -v
   npm -v
   ```

### Step 2: Clone the Repository

Clone the repository to your local machine. If you don't have `git` installed, you can download the repository as a ZIP file and extract it.

```sh
git clone https://github.com/yashvardhan-kukreja/hello-world-website.git
cd hello-world-website
```

### Step 3: Install Dependencies

Install the required Node.js dependencies using npm.

```sh
npm install
```

### Step 4: Run the Application

Start the Node.js application.

```sh
node app.js
```

### Step 5: Access the Application

Open your web browser and navigate to `http://localhost:3000`. You should see the "Hello, World!" message displayed on the page.



