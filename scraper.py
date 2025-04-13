import requests
from bs4 import BeautifulSoup
import json
from time import sleep

def scrape_wallpapers():
    url = "https://steamcommunity.com/workshop/browse/?appid=431960&browsesort=mostpopular§ion=readytouseitems"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }
    
    try:
        sleep(5)
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, "html.parser")
        
        wallpapers = []
        items = soup.find_all("div", class_="workshopItem")
        
        for item in items[:10]:
            title_tag = item.find("div", class_="workshopItemTitle")
            link_tag = item.find("a", class_="ugc")
            img_tag = item.find("img", class_="workshopItemPreviewImage")
            
            if title_tag and link_tag:
                title = title_tag.text.strip()
                link = link_tag["href"]
                img_url = img_tag["src"] if img_tag else ""
                
                wallpapers.append({
                    "title": title,
                    "link": link,
                    "image": img_url
                })
        
        with open("wallpapers.json", "w", encoding="utf-8") as f:
            json.dump(wallpapers, f, indent=4, ensure_ascii=False)
        
        print(f"Coletados {len(wallpapers)} wallpapers.")
        return wallpapers
    
    except Exception as e:
        print(f"Erro ao fazer scraping: {e}")
        return []

if __name__ == "__main__":
    scrape_wallpapers()