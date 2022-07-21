import requests
from bs4 import BeautifulSoup
 # scraping com beautifulsoup os 100 filmes que voce deve ver antes de morrer
    
URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"  # url no web archive porque o site sofre atualizacoes

response = requests.get(URL)  # recebe a url
website_html = response.text  # transforma tudo em texto

soup = BeautifulSoup(website_html, "html.parser")  # alimenta o objeto do beautiful soup com o website


all_movies = soup.find_all(name="h3", class_="title")  # procurando todos os titulos dentro do H3 do html
movie_titles = [movie.getText() for movie in all_movies]  # lista de tudo que foi achado em all_movies e transformando tudo em texto(era um objeto beautiful soup)

movie_titles.reverse()  # inverte a lista dos filmes, ou seja o primeiro filme a ser mostrado e o primeiro e nao o centesimo filme
print(movie_titles)  # pritando todos os filmes

with open("movies.txt", mode="w", encoding="utf8") as file:  # abrindo um arquivo .txt para todos os filmes
    for movie in movie_titles:
        file.write(f"{movie}\n")
