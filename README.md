# DNS Traffic Monitor (ARP Spoofing Based)

A simple tool based on `Scapy` to monitor DNS queries of a specific target on a local network by performing an ARP Spoofing (Man-in-the-Middle) attack.

## ⚠️ Legal Disclaimer
**This tool is for educational and security research purposes only.** It should only be used in isolated laboratory environments or on devices where you have explicit permission to test. Unauthorized use of this tool against networks or devices without express permission is **illegal** and may result in legal action. The developer is not responsible for any misuse of this tool.

## Prerequisites
* An operating system that supports `Scapy` (Kali Linux is recommended).
* Python 3.x
* Root/Administrator privileges (required for ARP packet manipulation).

## Install in linux
* `git clone https://github.com/lofyop91-web/DNS-Sniffer-Tool.git`.
* `pip install -r requirements.txt` OR `apt-get install libpcap-dev AND` AND  `pip install scapy`.
* `sudo python3 main.py`.

## How use
* Enter the ip tarr: (Enter your ip) example : '10.10.0.0/24'.
* Enter the ip getway: example: '10.10.0.1'.

