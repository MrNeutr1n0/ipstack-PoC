import requests
import json
import argparse

def get_ip_info(ip_address, access_key):
    url = f"http://api.ipstack.com/{ip_address}?access_key={access_key}"
    headers = {"content-type": "application/json"}

    response = requests.get(url, headers=headers)
    return response.json()

def main():
    parser = argparse.ArgumentParser(description='ipstack.com IP info fetch PoC')
    parser.add_argument('-ip', type=str, required=True, help='IP address')
    parser.add_argument('-key', type=str, required=True, help='Access key of ipstack API')

    args = parser.parse_args()

    ip_info = get_ip_info(args.ip, args.key)
    print(json.dumps(ip_info, indent=4))

if __name__ == "__main__":
    main()
