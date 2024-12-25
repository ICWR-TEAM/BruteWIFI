# WiFi Scanner and Cracker

This project is a Python-based tool that scans for nearby WiFi networks and attempts to connect to a specified network using a wordlist of potential passwords.

### Features

* **WiFi Scanning:** Scans for all available WiFi networks and displays their signal strength and SSID.
* **WiFi Password Cracking:** Attempts to log in to a specified WiFi network using a wordlist.
* **Interactive Interface:** Allows users to select a target network interactively

### Requirements

* Python 3.x
* [pywifi](https://github.com/awkman/pywifi) library

### Installation

1. Clone the repository:

```bash
git clone https://github.com/ICWR-TEAM/BruteWIFI
cd BruteWIFI
```

2. Install required dependencies:

```bash
pip install pywifi
```

Ensure your system has a wireless network interface card (NIC) and the necessary permissions to scan and connect to networks.

### Usage

#### Command Line Arguments

`-w` or `--wordlist`:  Path to the wordlist file containing potential passwords.

Example

```bash
sudo python3 script_name.py -w /path/to/wordlist.txt
```

### Steps

1. The script scans for available WiFi networks and displays them with their signal strength and SSID.
2. Press `Ctrl+C` to interrupt the scanning process and select a network by entering its corresponding number.
3. The script will attempt to log in to the selected network using passwords from the provided wordlist.

## Example Output

```bash
 _   _            _                _    __          _______ ______ _____
| \ | |          | |              | |   \ \        / /_   _|  ____|_   _|
|  \| | __ _  ___| |__  _ __ _   _| |_ __\ \  /\  / /  | | | |__    | |  
| . ` |/ _` |/ _ \ '_ \| '__| | | | __/ _ \ \/  \/ /   | | |  __|   | |  
| |\  | (_| |  __/ |_) | |  | |_| | ||  __/\  /\  /   _| |_| |     _| |_
|_| \_|\__, |\___|_.__/|_|   \__,_|\__\___| \/  \/   |_____|_|    |_____|
        __/ |                                                        
       |___/                                                         
----------------------------------------
No    Frequency    SSID
----------------------------------------
1     80           Network_1
2     75           Network_2
3     60           Hidden_SSID
----------------------------------------
Please select with the command press 'Ctrl+C' to select the target (Number)
```


## Notes

* Ensure the wordlist file is properly formatted with one password per line.
* The tool requires appropriate permissions to manage WiFi connections.

## Disclaimer

This tool is intended for educational purposes only. Unauthorized use of this tool on networks you do not own or have explicit permission to access is illegal and unethical. Use responsibly.
