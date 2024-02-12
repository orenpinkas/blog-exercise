import requests

url = "https://randomuser.me/api/"


def get_random_author():
    response = requests.get(url)
    data = response.json()
    author = data["results"][0]
    return {
        "name": f"{author['name']['first']} {author['name']['last']}",
        "email": author["email"],
    }


authors = [
    {"name": "Leif Morgenstern", "email": "leif.morgenstern@example.com"},
    {"name": "Imre Backes", "email": "imre.backes@example.com"},
    {"name": "Emilia Wiita", "email": "emilia.wiita@example.com"},
    {"name": "Keerthi Mugeraya", "email": "keerthi.mugeraya@example.com"},
    {"name": "Bushra Lundal", "email": "bushra.lundal@example.com"},
    {"name": "Ricardo Cruz", "email": "ricardo.cruz@example.com"},
    {"name": "Adolfo Montero", "email": "adolfo.montero@example.com"},
    {"name": "Justin Wong", "email": "justin.wong@example.com"},
    {"name": "Olivia Hakala", "email": "olivia.hakala@example.com"},
    {"name": "Asha Dijkers", "email": "asha.dijkers@example.com"},
    {"name": "Lisa Barrett", "email": "lisa.barrett@example.com"},
    {"name": "Byron Gordon", "email": "byron.gordon@example.com"},
    {"name": "Ashton Thomas", "email": "ashton.thomas@example.com"},
    {"name": "Illya Lapichak", "email": "illya.lapichak@example.com"},
    {"name": "Sergio Romero", "email": "sergio.romero@example.com"},
    {"name": "Elsa Kalm", "email": "elsa.kalm@example.com"},
    {"name": "Marit Lamens", "email": "marit.lamens@example.com"},
    {"name": "Ava Lévesque", "email": "ava.levesque@example.com"},
    {"name": "Chloe Clark", "email": "chloe.clark@example.com"},
    {"name": "Christine Pena", "email": "christine.pena@example.com"},
]


def get_author_data():
    return authors
