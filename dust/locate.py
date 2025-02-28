import platform, socket, psutil, sys, time, requests, os, uuid, hashlib
from datetime import datetime

# ANSI escape codes for colors
RED = "\033[91m"
RESET = "\033[0m"

def print_slow(text, delay=0.02):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def roast_user():
    pc_name = platform.node()
    user_ip = socket.gethostbyname(socket.gethostname())
    os_version = f"{platform.system()} {platform.release()}"
    cpu_count = psutil.cpu_count(logical=True)
    total_memory = round(psutil.virtual_memory().total / (1024 ** 3), 2)
    used_memory = round(psutil.virtual_memory().used / (1024 ** 3), 2)
    free_disk = round(psutil.disk_usage('/').free / (1024 ** 3), 2)
    time_now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    mac_address = ':'.join(['{:02x}'.format((uuid.getnode() >> i) & 0xff) for i in range(0, 8 * 6, 8)][::-1])

    print_slow(f"PC Name: {pc_name}... default much? 🐕")
    print_slow(f"IP: {user_ip}... microwave-assigned? 🍳")
    print_slow(f"OS: {os_version}... ancient relic! 💻")
    print_slow(f"CPU Cores: {cpu_count}... more than your friends 💀")
    print_slow(f"Memory: {used_memory}/{total_memory} GB... meme hoarder! 🧠")
    print_slow(f"Free Disk: {free_disk} GB... lonelier than your calendar 📅")
    print_slow(f"Time: {time_now}... wasting it, huh? 🕒")
    print_slow(f"MAC: {mac_address}... we’ve got your scent 🕵️‍♂️")

def simulate_attacks():
    print_slow("Launching *cyber attacks*... all in jest 😈")
    time.sleep(1)
    for attack in [
        "DDoS... packets raining down 🤖",
        "SQL Injection... login table *poof* 🔍",
        "Ransomware... encrypting vacation pics 🏖️",
        "MITM... intercepting your texts 🕶️",
        "Firewall bypass... none to bypass? 🚧",
        "Rootkit... or maybe not? 🤖"
    ]:
        print_slow(attack)
        time.sleep(1)

def download_image():
    image_url = "https://i.ibb.co/dLPVjTv/Findme.jpg"
    image_name = "Findme.jpg"
    try:
        print_slow("Fetching secret image... 📡")
        with open(image_name, 'wb') as file:
            file.write(requests.get(image_url).content)
        img_path = os.path.abspath(image_name)
        print_slow(f"Image saved: {RED}{img_path}{RESET} 🖼️")
        return img_path
    except Exception as e:
        print_slow(f"Download failed: {e}")
        return None

def challenge_intro(image_path):
    print_slow("Profile found, but the flag’s a hunt! 🐊😎")
    print_slow(f"Image: {RED}{image_path}{RESET}—analyze it 🖼️")
    print_slow("Find the place and nearest metro station 🚇")
    print_slow(f"{RED}If place is Sarojini Market and metro is Sarojini Nagar:{RESET}")
    print_slow(f"{RED}Step 1: Format as Sarojini_Market_Sarojini_Nagar{RESET}")
    print_slow(f"{RED}Step 2: Convert to MD5 hash (e.g., hashlib.md5('Sarojini_Market_Sarojini_Nagar'.encode()).hexdigest()){RESET}")
    print_slow(f"{RED}Flag format: flag{{MD5_hash}}{RESET} 🏆")
    print_slow(f"{RED}Hint: Delhi’s famous electronics market{RESET} 🔍")

def main():
    print_slow("Hacking your system... 🕵️‍♂️")
    roast_user()
    print_slow("\nSimulating attacks... 💻")
    simulate_attacks()
    image_path = download_image()
    if image_path:
        challenge_intro(image_path)
    else:
        print_slow("Image failed. Retry later.")

if __name__ == "__main__":
    main()
