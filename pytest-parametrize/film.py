class FilmService:

    def __init__(self,store=None):
        self.store = store
    
    def get_film(self, anno=None, origine=None):
        if anno is None and origine is None:
            raise ValueError("Anno o paese di origine obbligatori")
        
        if anno and origine is None:
            return self._get_film_per_anno(anno)
        
        if origine and anno is None:
            return self._get_film_per_origine(origine)
        
        if origine and anno:
            return self._get_film(anno, origine)

    def _get_film_per_anno(self, anno):
        film_list = []
        for film in self.store:
            #print(film, film.get('anno'))
            if film.get('anno') == anno:
                film_list.append(film)
        return film_list
    
    def _get_film_per_origine(self, origine):
        film_list = []
        for film in self.store:
            if film.get('origine') == origine:
                film_list.append(film)
        return film_list
    
    def _get_film(self, anno, origine):
        film_list = []
        for film in self.store:
            if film.get('origine') == origine and film.get('anno') == anno:
                film_list.append(film)
        return film_list

    
# if __name__ == "__main__":
#     store = [
#     {'nome':'Amaliè', 'anno':2001, 'origine':'Francia'},
#     {'nome':'Ora ci arrabbiamo', 'anno':2001, 'origine':'Italia'},
#     {'nome':'Noi testiamo sempre', 'anno':2023, 'origine':'Svizzera'},
#     {'nome':'Benvenuti all''Est', 'anno':2021, 'origine':'Francia'},
#         ]
#     service = FilmService(store)
#     print(service.get_film(2001,None))
