# CLI-Based-login-Python

Welcome to the CLI-Based-login-Python repository! This project is a simple Python program that implements a command-line interface (CLI) based login system with OTP (One-Time Password) authentication using Gmail's SMTP server. Users can either log in with existing credentials or create a new account with a Gmail address and password.

## Prerequisites

Before using this program, ensure that you have the following:

1. Python installed on your machine.
2. Enable two-step verification for your Gmail account.
3. Create an "App Password" for your Gmail account to use in the program.
4. Create the "idpassword.txt" in same folder as python script.

## How to Use

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/CLI-Based-login-Python.git

2. Navigate to the project directory:

   ```bash
   cd CLI-Based-login-Python

3. Install the required dependencies:

   ```bash
   pip install smtplib

4. Run the program:

   ```bash
   python login_system.py

## Important Note

1. When prompted for credentials, use your Gmail address and the "App Password" generated during the setup.
2. If you don't have an "App Password," follow these instructions to create one.

## Contributing

If you'd like to contribute to the development of this project, please follow the standard GitHub flow: Fork the repository, create a branch, make changes, and submit a pull request.

## License

This project is licensed under the MIT License - see the LICENSE.md file for details.
