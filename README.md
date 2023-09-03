# ISS Overhead Notifier

## Overview

This Python script uses two APIs to notify you via email when the International Space Station (ISS) is directly above your location and it's nighttime. It's a great way to remind you to look up at the sky for a chance to see the ISS pass by!

## Features

- Checks the current position of the ISS.
- Determines whether it's currently night time at your location.
- Sends you an email notification when both conditions are met.

## Requirements

- Python 3.x
- `requests` package for API requests

## How to Install

1. Clone this repository to your local machine.

    ```bash
    git clone https://github.com/yourusername/iss-overhead-notifier.git
    ```

2. Navigate to the cloned directory.

    ```bash
    cd iss-overhead-notifier
    ```

3. Install the required packages.

    ```bash
    pip install requests
    ```

## Configuration

1. Open `iss_notifier.py` in a text editor.
2. Update the following variables with your information:

    ```python
    email="___YOUR_EMAIL_HERE____",
    password="___YOUR_PASSWORD_HERE___",
    latitude=51.507351,
    longitude=-0.127758,
    smtp_address="__YOUR_SMTP_ADDRESS_HERE___"
    ```

## Running the Script

Execute the script in your terminal:

```bash
python iss_notifier.py
