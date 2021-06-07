import requests
import bs4


def get_links(url):
        link_list = []
        resp = requests.get(url)

        soup = bs4.BeautifulSoup(resp.content,features = "html.parser")
        links = soup.find_all("a",attrs = {'class' : 'title'} )
        for i in links:
                link_list.append(i['href'])
        return link_list

def get_lyrics(url,search):
        lyric = []
        resp = requests. get(url)
        soup = bs4.BeautifulSoup(resp.content,features = "html.parser")
        verses = soup.find_all("p",attrs = {'class' : 'verse'})
        heads = soup.find_all("h1")
        
        if(search in heads[0].get_text().lower()):
                for i in verses:
                        lyric.append(i.get_text())
        return lyric
def get_file_name(url):
        return url.split("/")[-1].replace(".html",".txt")
                
        
def main():
        songlist = get_links("https://www.metrolyrics.com/billie-eilish-lyrics.html")
        search = input("Enter Billie Eilish song name to get the lyrics of that song : ")
        search = search.lower()
        for song in songlist:
                ans = get_lyrics(song,search)
                if ans != []:
                        break
        if ans == []:
                print("\n\nNot Found!")
        else:
                fname = get_file_name(song)
                print(f"\n\n{song}->{fname}")
                f = open(fname,'w')
                lyrics = "\n".join(ans)
                f.write(lyrics)
                f.close
                print("\nsuccess")

if __name__ == "__main__":
        main()
