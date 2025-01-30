from yt_dlp import YoutubeDL
import csv
import os
import re


def sanitize_filename(title):
    sanitized = re.sub(r'[<>:"/\\|?*]', '', title)
    sanitized = re.sub(r'\s+', '_', sanitized)
    sanitized = sanitized[:100].rstrip('.')
    return sanitized

def get_playlist_videos(playlist_url):
    ydl_opts = {
        'quiet': True,
        'extract_flat': True,
        'force_generic_extractor': False,
        'no_warnings': True
    }
    try:
        with YoutubeDL(ydl_opts) as ydl:
            result = ydl.extract_info(playlist_url, download=False)
            playlist_title = result.get('title', 'Unknown_Playlist')
            videos = []
            for entry in result['entries']:
                videos.append({
                    'title': entry['title'],
                    'url': f"https://www.youtube.com/watch?v={entry['id']}"
                })
            return playlist_title, videos
    except:
        return None, None

def process_playlists(input_file):
    output_dir = 'playlists_output'
    os.makedirs(output_dir, exist_ok=True)
    
    with open(input_file, 'r') as f:
        playlist_urls = f.read().splitlines()
    
    for url in playlist_urls:
        if url.strip():  
            playlist_title, videos = get_playlist_videos(url)
            if(playlist_title == None ):
                continue;
            safe_title = sanitize_filename(playlist_title)
            
            # Cria CSV compatível com Excel
            output_file = os.path.join(output_dir, f'{safe_title}.csv')
            with open(output_file, 'w', newline='', encoding='utf-16') as csvfile:
                writer = csv.DictWriter(csvfile, fieldnames=['title', 'url'], delimiter='\t')
                writer.writeheader()
                writer.writerows(videos)

            print(safe_title + ": " + str(len(videos)) + " videos" )

if __name__ == "__main__":
    process_playlists('playlists.txt')
