#!/usr/bin/python3
# Released under GPLv3+ License
# Kawan Najjar  <kawannajjar@gmil.com>, 2023.
import subprocess
import os

def read_servers(file_path):
    try:
        with open(file_path, 'r') as f:
            servers = [line.strip() for line in f.readlines()]
        return servers
    except FileNotFoundError:
        print("فایل مورد نظر یافت نشد.")
        return []

def select_server(servers):
    print("لطفاً یک سرور را از لیست زیر انتخاب کنید:")
    for idx, server in enumerate(servers):
        print(f"{idx + 1}. {server}")

    choice = int(input("\nشماره سرور را وارد کنید: ")) - 1
    if 0 <= choice < len(servers):
        return servers[choice]
    else:
        print("انتخاب نامعتبر!")
        return None

def connect_to_server(server):
    try:
        # دستور Bash برای اتصال به سرور با استفاده از openconnect
        subprocess.run(['sudo', 'openconnect', server])
    except Exception as e:
        print(f"خطایی رخ داد: {e}")

if __name__ == "__main__":
    # بدست آوردن مسیر فایل فعلی و فایل server.txt
    current_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(current_dir, 'server.txt')  # تغییر نام به server.txt

    servers = read_servers(file_path)

    if servers:
        selected_server = select_server(servers)
        if selected_server:
            connect_to_server(selected_server)

