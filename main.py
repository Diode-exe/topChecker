import socket
import itertools
import time

BASE_DOMAIN = "help.top"

def generate_prefixes(length=4):
    letters = "abcdefghijklmnopqrstuvwxyz"
    return itertools.product(letters, repeat=length)

def domain_exists(domain):
    try:
        socket.gethostbyname(domain)
        return True
    except socket.gaierror:
        return False

def main():
    reachable = []

    for prefix_tuple in generate_prefixes():
        prefix = "".join(prefix_tuple)
        domain = f"{prefix}{BASE_DOMAIN}"

        print(f"Checking {domain}")

        if domain_exists(domain):
            print(f"[+] Exists: {domain}")
            reachable.append(domain)
            with open("reachable.txt", "a") as f:
                f.write(domain + "\n")

        time.sleep(0.5)

    print(f"Reachable domains: {reachable}")
    with open("reachable.txt", "w") as f:
        for domain in reachable:
            f.write(domain + "\n")

if __name__ == "__main__":
    main()
