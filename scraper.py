import cloudscraper
from bs4 import BeautifulSoup

scraper = cloudscraper.create_scraper()
book_name=input("Enter Book/Novel name: ") + ".txt"
url = input("Enter any Chapter URL you want to start from: ")

while True:
    try:
        response = scraper.get(url)
    except:
        print("Error retrieving URL.")
        break
        
    soup = BeautifulSoup(response.text, 'html.parser')
    
    title = soup.title.text if soup.title else 'No title found'
    
    chapter_contents = soup.find_all('p', class_='chapter_content')
    
    with open(book_name,"a") as file:
        file.write(title+"\n"*2)
        for lines in chapter_contents:
            file.write(lines.text+"\n"*2)
    print(title,"Done...")        
    next=soup.find_all('a',class_="novel_nav_item")
    if next:
        url=str(next[2].get("href"))
    else:
        break
    print(" ")