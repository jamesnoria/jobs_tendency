
class Data:
    """
    This class or local library is used as an 'ordered' way to store
    every name and regex to use as a filter into the text files.
    """

    def __init__(self):
        pass

    def programming_languages(self):
        programming_languages = {
            'python': '(P(?:YTHON|ython)|python)',
            'c': '\s[cC]\s',
            'java': '(J(?:AVA|ava)|java)[^\w?]',
            'c++': '[Cc](?:plusplus|\+\+?)',
            'c#': 'c(?: sharp|#)|C#',
            'r': '\s[\,?][Rr]\s',
            'javascript': 'J(?:AVASCRIPT|avascript)|javascript',
            'php': '(P(?:HP|hp)|php)[^\w]',
            'go': '[^\w](G(?:O(?:LANG)?|o(?:lang)?)|go(?:lang)?)[^\w]',
            'swift': 'S(?:WIFT|wift)|swift',
            'ruby': 'R(?:UBY|uby)|ruby',
            'scala': '[^\w](S(?:CALA|cala)|scala)[^\w]',
            'perl': 'P(?:ERL|erl)|perl',
            'html': 'H(?:TML|tml)|html',
            'css': 'C(?:SS|ss)|css',
            'Typescript': 'T(?:YPESCRIPT|ypescript)|typescript',
            'rust': 'R(?:UST|ust)|rust',
            'kotlin': 'K(?:OTLIN|otlin)|kotlin',
            'bash': 'B(?:ASH|ash)|bash',
        }

        return programming_languages

    def frameworks(self):
        frameworks = {
            'react': '(R(?:EACT|eact)|react)[^i]',
            'asp.net': 'A(?:SP\.NET|sp\.[Nn]et)|asp\.net',
            'angular': 'A(?:NGULAR|ngular)|angular',
            'ruby on rails': 'R(?:(?:UBY(?: ON |ON)R)?AILS|uby(?: on |on)rails|ails)|r(?:ubyonr)?ails',
            'vue': 'V(?:UE(?:\.JS)?|ue(?:\.js)?)|vue(?:\.js)?',
            'django': 'django|D(?:JANGO|jango)',
            'laravel': 'L(?:ARAVEL|aravel)|laravel',
            'express': 'E(?:XPRESS|xpress)|express',
            'code igniter': 'C(?:ODE ?IGNITER|ode ?Igniter)|code ?igniter',
            'ember': 'E(?:MBER|mber)|ember',
            'spring': 'S(?:PRING|pring)|spring',
            'flask': 'flask|F(?:LASK|lask)',
            'symfony': 'symfony|S(?:YMFONY|ymfony)',
        }

        return frameworks

    def complements(self):
        complements = {
            'git': 'G(?:IT|it)|git',
            'ingles': 'ingles|I(?:NGLES|ngles)',
            'linux': 'L(?:INUX|inux)|linux',
        }
        return complements

    def data_bases(self):
        data_bases = {
            'mysql': 'M(?:[Yy]SQL|ySql|ysql)|mysql',
            'postgresql': 'P(?:ostgresSql|(?:OSTGRE|ostgre)SQL|ostgresql)|postgresql',
            'mongodb': 'M(?:ONGODB|ongoD[Bb])|mongodb',
            'sqlite': 'S(?:QLITE|qlite)|sqlite',
            'oracle': 'O(?:RACLE|racle)|oracle',
            'sql server': 'S(?:QL SERVER|ql Server)|sql server',
        }
        return data_bases

    def cloud(self):
        cloud = {
            'azure': 'A(?:ZURE|zure)|azure',
            'aws': 'A(?:MAZON WEB SERVICE|WS|ws)|a(?:mazon web service|ws)',
            'salesforce': 'S(?:ALESFORCE|alesForce)|salesforce',
            'google cloud platform': 'G(?:OOGLE CLOUD PLATFORM|oogle Cloud Platform|CP|cp)|gcp',
        }
        return cloud
