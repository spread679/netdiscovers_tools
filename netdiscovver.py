#!/usr/bin/env python3
#
# find other host in your network
#
import argparse
import socket

def connect(ip):
    discover = socket.socket()
    try:
        discover.connect((ip, 80))
        discover.close()
        return True
    except Exception as exc:
         return False

if __name__ == '__main__':
    try:
        parser = argparse.ArgumentParser(description="Discover other hosts in your network.")
        parser.add_argument('-i', '--ip', help='The IP to test if it is present in your network')
        parser.add_argument('-r', '--range', help='Your network range')

        args = parser.parse_args()

        if args.ip:
            if connect(args.ip):
                print(f"[+] Connected to {args.ip}")
            else:
                print(f"[-] Not connected to {args.ip}")
        elif args.range:
            split_range = args.range.split(".")
            if len(split_range) == 4 and "-" in split_range[3]:
                min_range = int(split_range[3].split("-")[0])
                max_range = int(split_range[3].split("-")[1])
                   
                if max_range > 255:
                    max_range = 255

                for octet in range(min_range, max_range):
                    ip = ".".join(split_range[:3])
                    ip += "." + str(octet)

                    if connect(ip):
                        print(f"[+] Connected to {ip}")
        else:
            parser.print_help()
    except Exception as ex:
        print(f"[-] {ex}")
