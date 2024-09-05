import requests

def get_nordvpn_servers(country_id=228):
    response = requests.get(f"https://api.nordvpn.com/v1/servers/recommendations?&limit=20&filters[country_id]={country_id}")
    server_list = response.json()
    hostname = None

    for server in server_list:
        hostname = server['hostname']
        print(f"{hostname}")

if __name__ == '__main__':
    get_nordvpn_servers()