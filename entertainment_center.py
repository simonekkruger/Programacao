# coding=utf-8

import media
import site_trailers_filmes_simone

# Aqui são listados as instancias da classe Movie

toy_story = media.Movie("Toy Story","Woody é um boneco" +\
" cowboy de bom coração que pertence a um jovem chamado Andy." +\
" Porém vê sua posição como o brinquedo favorito de Andy" +\
" comprometida quando seus pais lhe compram um outro brinquedo.",
"http://www.filmesonlinegratis.com/wp-content/uploads/2015/05/" +\
"Toy-Story-2-221x300.jpg", "https://www.youtube.com/watch?v=Bj4gS1JQzjk")

avatar = media.Movie("Avatar", "No mundo de Pandora vivem os Na'vi." +\
" Para humanos entrarem em Pandora, foram criados avatares, controlados" +\
" pela mente. Um ex-fuzileiro paralítico se apaixona por uma Na'vi" +\
" através de um avatar e acaba ajudando na sobrevivência de Pandora.",
"https://upload.wikimedia.org/wikipedia/pt/thumb/b/b0/Avatar-Teaser" +\
"-Poster.jpg/250px-Avatar-Teaser-Poster.jpg","https://www.youtube." +\
"com/watch?v=6ziBFh3V1aM")

titanic = media.Movie("Titanic", "Um artista pobre e uma jovem rica"+\
" se conhecem e se apaixonam na fatídica jornada do Titanic, em 1912."+\
" Embora esteja noiva do arrogante herdeiro de uma siderúrgica, a jovem" +\
" desafia sua família e amigos em busca do verdadeiro amor.",
"https://upload.wikimedia.org/wikipedia/en/2/22/Titanic_poster.jpg",
"https://www.youtube.com/watch?v=zCy5WQ9S4c0")

matrix = media.Movie("Matrix","Um jovem programador é seguido pelos" +\
" misteriosos Morpheus e Trinity, e acaba desconbrindo que está preso" +\
" em um sistema virtual chamado Matrix.",
"https://upload.wikimedia.org/wikipedia/pt/thumb/c/c1/The_Matrix" +\
"_Poster.jpg/200px-The_Matrix_Poster.jpg",
"https://www.youtube.com/watch?v=vKQi3bBA1y8")

it = media.Movie("It","Crianças começam a desaparecer na cidade de Derry," +\
" as crianças acabam descobrindo que os desaparecimentos estão relacionados" +\
" com Pennywise, um palhaço malvado cuja história de assassinato e" +\
" violência remonta a séculos.", "https://upload.wikimedia.org/wikipedia/pt/" +\
"thumb/5/5a/It_%282017%29_poster.jpg/250px-It_%282017%29_poster.jpg",
"https://www.youtube.com/watch?v=hAUTdjf9rko")

death_note = media.Movie("Death Note","Light Turner é um estudante brilhante" +\
" que, um dia, encontra um caderno que repentinamente cai do céu. Trata-se do" +\
" Death Note, que permite ao seu portador matar qualquer pessoa apenas" +\
" escrevendo o seu nome dentro dentro dele.",
"https://ia.media-imdb.com/images/M/MV5BMTUwOTgzMTEyOF5BMl5BanBnXkFtZTgwNTk3" +\
"MTM5MjI@._V1_UX182_CR0,0,182,268_AL_.jpg",
"https://www.youtube.com/watch?v=w5iOGZ1-oZs")


# A lista abaixo movies alimenta a função def create_movie_tiles_content(movies)
# e a função def open_movies_page(movies) "site_trailers_filmes_simone.py"
movies = [toy_story, avatar, titanic, matrix, it, death_note]

# essa função gera o arquivo em html do código
site_trailers_filmes_simone.open_movies_page(movies)




