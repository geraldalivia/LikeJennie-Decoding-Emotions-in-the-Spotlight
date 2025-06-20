#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Library
import pandas as pd
import requests
import json
from datetime import datetime
import time
import os

# Bagian youtube scraper google cloud
class YouTubeCommentScraper:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = "https://www.googleapis.com/youtube/v3"

    def extract_video_id(self, url):
        if "watch?v=" in url:
            return url.split("watch?v=")[1].split("&")[0]
        return None
    
    # Mendapatkan informasi video
    def get_video_info(self, video_id):
        url = f"{self.base_url}/videos"
        params = {
            'part': 'snippet,statistics',
            'id': video_id,
            'key': self.api_key
        }
        
        try:
            response = requests.get(url, params=params)
            print(response.text)
            response.raise_for_status()
            data = response.json()

            if 'items' in data and len(data['items']) > 0:
                video = data['items'][0]
                return {
                    'title': video['snippet']['title'],
                    'channel': video['snippet']['channelTitle'],
                    'published_at': video['snippet']['publishedAt'],
                    'view_count': video['statistics'].get('viewCount', 0),
                    'like_count': video['statistics'].get('likeCount', 0),
                    'comment_count': video['statistics'].get('commentCount', 0)
                }
        except requests.exceptions.RequestException as e:
            print(f"Error getting video info: {e}")
        return None
    
    # Mengambil komentar dari video
    def get_comments(self, video_id, max_results=10000):
        comments = []
        url = f"{self.base_url}/commentThreads"
        
        params = {
            'part': 'snippet',
            'videoId': video_id,
            'key': self.api_key,
            'maxResults': 100,
            'order': 'relevance'
        }
        
        print(f"Mengambil maksimal {max_results} komentar...")
        
        while len(comments) < max_results:
            try:
                response = requests.get(url, params=params)
                response.raise_for_status()
                data = response.json()
                
                if 'items' not in data:
                    print("Tidak ada komentar lagi")
                    break
                
                for item in data['items']:
                    comment = item['snippet']['topLevelComment']['snippet']
                    comments.append({
                        'comment_id': item['snippet']['topLevelComment']['id'],
                        'author': comment['authorDisplayName'],
                        'text': comment['textDisplay'],
                        'like_count': comment['likeCount'],
                        'published_at': comment['publishedAt'],
                        'updated_at': comment['updatedAt']
                    })
                
                print(f"Berhasil mengambil {len(comments)} komentar...")
                
                # Check halaman selanjutnya
                if 'nextPageToken' in data and len(comments) < max_results:
                    params['pageToken'] = data['nextPageToken']
                else:
                    break
                    
                # Rate limiting untuk menghindari quota limit
                time.sleep(0.1)
                
            except requests.exceptions.RequestException as e:
                print(f"Error: {e}")
                break
            except KeyError as e:
                print(f"Data structure error: {e}")
                break
        
        return comments[:max_results]
    
    # Menyimpan komentar ke CSV
    def save_to_csv(self, comments, filename=None):
        if not filename:
            filename = f"jennie_comments_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"
        
        df = pd.DataFrame(comments)
        df.to_csv(filename, index=False, encoding='utf-8')
        print(f"Data berhasil disimpan ke {filename}")
        return df, filename

# Bagian scraper untuk youtube profile jennie [JENNIE - like Jennie MV]
def main():
    API_KEY = "AIzaSyDGoLMLQLMY4HEvvyUnMeQ0sWA7Vjk2iVE"
    
    if not API_KEY or API_KEY.strip() == "":
        print("API KEY Salah, coba input lagi ya manis. Tetap semangat!")
        return
    
    # URL video LIKE JENNIE
    video_url = "https://www.youtube.com/watch?v=cdeKX7cs-r0"
    scraper = YouTubeCommentScraper(API_KEY)
    video_id = scraper.extract_video_id(video_url)
    
    print(f"Video ID: {video_id}")
    
    # Get video info
    print("Mengambil informasi video...")
    video_info = scraper.get_video_info(video_id)
    if video_info:
        print(f"Judul: {video_info['title']}")
        print(f"Channel: {video_info['channel']}")
        print(f"Jumlah komentar: {video_info['comment_count']}")
        print(f"Views: {video_info['view_count']}")
        print(f"Likes: {video_info['like_count']}")
    else:
        print("Gagal mengambil informasi video. Periksa API Key kamu.")
        return
    
    # Scrape comments
    max_comments = int(input("Berapa banyak komentar yang ingin diambil?") or "10000")
    
    print("Mulai scraping komentar...")
    comments = scraper.get_comments(video_id, max_results=max_comments)
    
    print(f"Berhasil mengambil {len(comments)} komentar")
    
    if comments:
        # Save to CSV
        df, filename = scraper.save_to_csv(comments)
        print(f"\nPreview data:")
        print(df.head())
        print(f"\nFile disimpan sebagai: {filename}")
    else:
        print("Tidak ada komentar yang berhasil diambil.")

if __name__ == "__main__":
    main()