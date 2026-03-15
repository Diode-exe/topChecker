"""Checks for the reachability of 4-letter domains ending with .top"""

import socket
import itertools
import time

BASE_DOMAIN = "help.top"

def generate_prefixes(length=4):
    """Generates all possible combinations of lowercase letters for the given length."""
    letters = "abcdefghijklmnopqrstuvwxyz"
    return itertools.product(letters, repeat=length)

def domain_exists(domain):
    """Checks if the domain can be resolved to an IP address."""
    try:
        socket.gethostbyname(domain)
        return True
    except socket.gaierror:
        return False

def main():
    """Main function to check the reachability of domains."""
    reachable = []

    for prefix_tuple in generate_prefixes():
        prefix = "".join(prefix_tuple)
        domain = f"{prefix}{BASE_DOMAIN}"

        print(f"Checking {domain}")

        if domain_exists(domain):
            print(f"[+] Exists: {domain}")
            reachable.append(domain)
            with open("reachable.txt", "a", encoding="utf-8") as f:
                f.write(domain + "\n")

        time.sleep(0.5)

    print(f"Reachable domains: {reachable}")
    with open("reachable.txt", "w", encoding="utf-8") as f:
        for domain in reachable:
            f.write(domain + "\n")

if __name__ == "__main__":
    main()
