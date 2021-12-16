from bs4 import BeautifulSoup


class startup_infos:
    @staticmethod
    def get_all_infos(body):
        soup = BeautifulSoup(body, "html.parser")

        # name
        name = soup.find(class_="publ-header__name").text

        # mercado  publico  Modelo   Momento
        # box[0]   box[1]   box[2]   box[3]
        box = soup.find_all(class_="startup-timely__data")

        # All the fields of localization
        try:
            localizacao = soup.find(class_="publ-card startup-addrr__grow")
            localizacao = localizacao.find_all(class_="publ-text")
        # cidade-estado
            estado = localizacao[-1].text
        except BaseException:
            estado = '--L--'

        try:
            side_box = soup.find('app-card-body')
            # URL   Segmento  Fundacao  Tamanho  Atualizacao
            # s[0]  s[1]      s[2]      s[3]     s[4]
            side_box = side_box.find_all('article')
        except BaseException:
            side_box = ["-----", "-----", "-----", "-----", "-----"]

        infos = [
            name, estado,
            box[0].text, box[1].text, box[2].text, box[3].text,
            side_box[3].p.text, side_box[1].p.text, "facetwitter.com"]

        return infos
