import os
def print_banner():
    banner = """
===========================================
           Made by Mr-Dev404  :)
   My Github : https://github.com/Mr-Dev404      
============================================
    """
    print(banner)

def install_packages():
    packages = [
        "php", "python", "git", "golang", "python2", "host", "nano", "havij", "hydra",
        "wireshark", "cmatrix", "figlet", "wget", "cowsay", "toilet", "ruby", "help", "lolcat",
        "curl", "wgetrc", "unzip", "openssh", "tor", "net-tools", "unrar", "clang", "w3m", "proot"
    ]
    os.system("termux-setup-storage")
    os.system("apt update -y && apt upgrade -y")
    os.system("pkg install -y " + " ".join(packages))
    os.system("pip2 install wget requests")
    os.system("clear")
    print("All packages have been installed successfully!")

if __name__ == "__main__":
    print_banner()
    print("Starting installation...")
    install_packages()
    
