import json
import base64
import os
import json
import subprocess

os.environ["SPOTIPY_CLIENT_ID"] = "bbf20a124ab74d1c8bbc48bf4fd56942"
os.environ["SPOTIPY_CLIENT_SECRET"] = "1be0ddedbb2445549dcb6951a2a05de3"

# Set the output directory
output_dir = "./result"

list_song_url = []

with open("file_v1.txt", "r", encoding="utf-8") as f: 
        for line in f:
            # Tách dòng thành các phần riêng biệt bằng khoảng trắng
            # parts = line.split()

            # Lấy liên kết Spotify cuối cùng của dòng và thêm nó vào danh sách
            list_song_url.append((line.strip()).split(" ")[-1]) # parts[-1]

for song_url in list_song_url[997:]: 
    # tải track songs
    subprocess.run(["spotify_dl", "-V", "-l", song_url, "--output", output_dir])

# print(list_song_url[997])