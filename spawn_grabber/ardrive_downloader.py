import sys
import subprocess
import argparse
import os

from spawn_grabber.decrypt_concat import process_directory_or_file

def parse_m3u_file(m3u_path):
    folder_ids = []
    with open(m3u_path, 'r') as file:
        for line in file:
            if line.startswith('#EXTINF:'):
                _, folder_id = line.strip().split(',')
                folder_ids.append(folder_id)
    return folder_ids

def download_folder(folder_id, ardrive_wallet_path, music_path):
    folder_download_path = f"{music_path}/{folder_id}"
    command = [
        "ardrive",
        "download-folder",
        "-f", folder_id,
        "--local-path", folder_download_path,
        "-w", ardrive_wallet_path
    ]
    subprocess.run(command)
    print(f"Folder with ID \"{folder_id}\" was successfully downloaded to \"{folder_download_path}\"")

def run_decrypt_script(music_path):
    process_directory_or_file(music_path, music_path)

def resolve_path(path):
    return os.path.abspath(os.path.expanduser(path))

def main():
    parser = argparse.ArgumentParser(description='ArDrive Downloader Script')
    parser.add_argument('m3u_path', help='Path to the M3U file')
    parser.add_argument('ardrive_wallet_path', help='Path to the ArDrive wallet file')
    parser.add_argument('--music-path', default=os.getcwd(),
                    help='Path where the folders will be downloaded and decrypted (default: current working directory)')

    args = parser.parse_args()

    m3u_path = resolve_path(args.m3u_path)
    ardrive_wallet_path = resolve_path(args.ardrive_wallet_path)
    music_path = resolve_path(args.music_path)

    folder_ids = parse_m3u_file(m3u_path)

    for folder_id in folder_ids:
        download_folder(folder_id, ardrive_wallet_path, music_path)
        run_decrypt_script(music_path)
        print(f"Processed folder: {folder_id}")

if __name__ == "__main__":
    main()
