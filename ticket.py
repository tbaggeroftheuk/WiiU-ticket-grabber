import os
import subprocess

def main():
    title_id = input("Enter Wii U Title ID (e.g. 000500001010EC00): ").strip()
    if len(title_id) != 16:
        print("Error: Title ID should be 16 characters long.")
        return

    url = f"http://ccs.cdn.wup.shop.nintendo.net/ccs/ticket/{title_id}.tik"
    save_dir = os.path.join(os.getcwd(), "ticket")
    os.makedirs(save_dir, exist_ok=True)
    save_path = os.path.join(save_dir, f"{title_id}.tik")

    print(f"Downloading ticket for Title ID {title_id} using curl...")

    try:
        result = subprocess.run(
            ["curl", "-s", "-o", save_path, url],
            check=True
        )
        if os.path.exists(save_path) and os.path.getsize(save_path) > 0:
            print(f"Ticket saved to: {save_path}")
        else:
            print("Download failed or file is empty.")
    except subprocess.CalledProcessError as e:
        print(f"curl failed with error: {e}")

if __name__ == "__main__":
    main()