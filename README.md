# Python Multi-Utility Toolkit

## Overview

This project is a command-line Python application that provides multiple utilities through a menu-driven interface. It combines several networking, security, and productivity tools into a single program.

## Features

1. My IP Address Finder

   * Displays the system hostname and IP address.

2. Password Generator

   * Generates random passwords with customizable length.
   * Supports uppercase letters, lowercase letters, numbers, and symbols.

3. Wordlist Generator

   * Generates custom wordlists using character combinations.
   * Saves generated combinations to a file.

4. Barcode Generator

   * Creates barcode images from numeric input.

5. QR Code Generator

   * Generates QR codes from URLs or text.
   * Saves output as PNG and SVG files.

6. Phone Number Information Lookup

   * Retrieves carrier and geographic information for phone numbers.

7. Subdomain Scanner

   * Attempts to discover subdomains using a wordlist.

8. Port Scanner

   * Scans common TCP ports on a target host.

## Technologies Used

* Python 3
* requests
* phonenumbers
* pyqrcode
* tqdm
* tabulate

## Installation

Clone the repository and install dependencies:

```bash
pip install -r requirements.txt
```

## Usage

Run the program:

```bash
python multitool.py
```

Select an option from the menu and follow the prompts.

## Project Structure

```text
Assignment7/
├── multitool.py
├── README.md
```

## Note

This project is intended for educational and learning purposes. Use network-related features only on systems and domains for which you have permission.
