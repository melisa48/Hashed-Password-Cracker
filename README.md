#  Hashed Password Cracker

## Description

This is a Python-based MD5 password cracker that implements both dictionary and brute force attacks. It uses multi-threading to improve performance, making it efficient for educational and testing purposes.

## Features

- MD5 hash cracking
- Dictionary attack
- Brute force attack
- Multi-threaded for improved performance
- Simple command-line interface

## Requirements

- Python 3.x

## Installation

1. Clone this repository or download the source code.
2. Ensure you have Python 3.x installed on your system.

## Usage

1. Open a terminal or command prompt.
2. Navigate to the directory containing the script.
3. Run the script using Python: `python password_cracker.py`
4. Enter the MD5 hash you want to crack when prompted.
5. Choose the attack type:
- Enter '1' for brute force attack
- Enter '2' for dictionary attack

## Dictionary File

The dictionary attack uses a file named `common_passwords.txt`. This file should be in the same directory as the script. You can modify this file to include additional passwords or use a different dictionary file.

## Customization

- You can adjust the number of threads used by modifying the `num_threads` parameter in the `threaded_brute_force_attack` and `threaded_dictionary_attack` function calls.
- For the brute force attack, you can change the `max_length` parameter to search for longer passwords.

## Limitations

- The brute force attack is limited to lowercase letters and digits. Modify the `chars` variable in the `brute_force_worker` function to include more characters if needed.
- This tool is designed for educational purposes and should only be used on systems you own or have explicit permission to test.

## Ethical Considerations

This tool is intended for educational purposes, security testing of your own systems, or systems you have explicit permission to test. Unauthorized use of this tool against systems you do not own or have permission to test is illegal and unethical.

## Contributing

Contributions to improve the tool are welcome. Please feel free to fork the repository and submit pull requests.

## License

[Specify your chosen license here, e.g., MIT License, GNU General Public License, etc.]

## Disclaimer

The authors of this tool are not responsible for any misuse or damage caused by this program. Use at your own risk and only on systems you own or have permission to test.
