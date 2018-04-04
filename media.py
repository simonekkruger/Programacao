# coding=utf-8
import webbrowser

class Movie():
    """
    Esta classe recebe quatro argumentos (titulo, sinopse, poster e trailer)
    que servirão para construir todas as instancias de filmes em entertainment_center.
    Após isso, a lista das instancias alimentará a página site_trailers_filmes_simone
    que por fim irá gerar um arquivo html.
    """
    def __init__(self, movie_title, sinopse, poster_image, trailer_youtube):
        self.title= movie_title
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
        self.sinopse = sinopse

    def show_trailer(self):
        """
        Essa função é responsável por abrir o link do youtube com trailer
        após ser clicado pelo usuário.
        :return:
        """
        webbrowser.open(self.trailer_youtube_url)
