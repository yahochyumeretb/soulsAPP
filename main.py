from fastapi import FastAPI, Query
from typing import List, Optional

app = FastAPI()

data = [
{
"id": 0,
"firstName": "Artorias",
"lastName": "The Abysswalker",
"fullName": "Artorias the Abysswalker",
"title": "Knight of Gwyn",
"family": "Knight",
"image": "artorias.jpg",
"imageUrl": "https://avatars.mds.yandex.net/i?id=6f98fd5062453d73cdf62874cb0493ea_l-5234162-images-thumbs&n=13"
},
{
"id": 1,
"firstName": "Solaire",
"lastName": "of Astora",
"fullName": "Solaire of Astora",
"title": "Warrior of Sunlight",
"family": "Astora",
"image": "solaire.jpg",
"imageUrl": "https://avatars.mds.yandex.net/i?id=6f98fd5062453d73cdf62874cb0493ea_l-5234162-images-thumbs&n=13"
},
{
"id": 2,
"firstName": "Gwyn",
"lastName": "Lord of Sunlight",
"fullName": "Gwyn, Lord of Sunlight",
"title": "Lord of Cinder",
"family": "Lord",
"image": "gwyn.jpg",
"imageUrl": "https://avatars.mds.yandex.net/i?id=6f98fd5062453d73cdf62874cb0493ea_l-5234162-images-thumbs&n=13"
},
{
"id": 3,
"firstName": "Gwynevere",
"lastName": "Princess of Sunlight",
"fullName": "Gwynevere, Princess of Sunlight",
"title": "Daughter of Gwyn",
"family": "Lord",
"image": "gwynevere.jpg",
"imageUrl": "https://avatars.mds.yandex.net/i?id=6f98fd5062453d73cdf62874cb0493ea_l-5234162-images-thumbs&n=13"
},
{
"id": 4,
"firstName": "Sif",
"lastName": "The Great Grey Wolf",
"fullName": "Sif, the Great Grey Wolf",
"title": "Guardian of Artorias",
"family": "Wolf",
"image": "sif.jpg",
"imageUrl": "https://avatars.mds.yandex.net/i?id=6f98fd5062453d73cdf62874cb0493ea_l-5234162-images-thumbs&n=13"
},
{
"id": 5,
"firstName": "Seath",
"lastName": "The Scaleless",
"fullName": "Seath the Scaleless",
"title": "Duke of the Crystal",
"family": "Dragon",
"image": "seath.jpg",
"imageUrl": "https://avatars.mds.yandex.net/i?id=6f98fd5062453d73cdf62874cb0493ea_l-5234162-images-thumbs&n=13"
},
{
"id": 6,
"firstName": "Manus",
"lastName": "The Furtive Pygmy",
"fullName": "Manus, the Furtive Pygmy",
"title": "Father of the Abyss",
"family": "Human",
"image": "manus.jpg",
"imageUrl": "https://avatars.mds.yandex.net/i?id=6f98fd5062453d73cdf62874cb0493ea_l-5234162-images-thumbs&n=13"
},
{
"id": 7,
"firstName": "Ornstein",
"lastName": "The Dragonslayer",
"fullName": "Ornstein, the Dragonslayer",
"title": "Knight of the Cathedral",
"family": "Knight",
"image": "ornstein.jpg",
"imageUrl": "https://avatars.mds.yandex.net/i?id=6f98fd5062453d73cdf62874cb0493ea_l-5234162-images-thumbs&n=13"
},
{
"id": 8,
"firstName": "Smough",
"lastName": "The Executioner",
"fullName": "Smough, the Executioner",
"title": "Executioner of the Cathedral",
"family": "Knight",
"image": "smough.jpg",
"imageUrl": "https://avatars.mds.yandex.net/i?id=6f98fd5062453d73cdf62874cb0493ea_l-5234162-images-thumbs&n=13"
},
{
"id": 9,
"firstName": "Nito",
"lastName": "The First Dead",
"fullName": "Nito, the First Dead",
"title": "Lord of Death",
"family": "Lord",
"image": "nito.jpg",
"imageUrl": "https://avatars.mds.yandex.net/i?id=6f98fd5062453d73cdf62874cb0493ea_l-5234162-images-thumbs&n=13"
},
{
"id": 10,
"firstName": "Priscilla",
"lastName": "The Crossbreed",
"fullName": "Priscilla, the Crossbreed",
"title": "Lady of the Painted World",
"family": "Hybrid",
"image": "priscilla.jpg",
"imageUrl": "https://avatars.mds.yandex.net/i?id=6f98fd5062453d73cdf62874cb0493ea_l-5234162-images-thumbs&n=13"
},
{
"id": 11,
"firstName": "Hawkeye",
"lastName": "Gough",
"fullName": "Hawkeye Gough",
"title": "Great Archer",
"family": "Knight",
"image": "gough.jpg",
"imageUrl": "https://avatars.mds.yandex.net/i?id=6f98fd5062453d73cdf62874cb0493ea_l-5234162-images-thumbs&n=13"
},
{
"id": 12,
"firstName": "Yhorm",
"lastName": "The Giant",
"fullName": "Yhorm the Giant",
"title": "Lord of the Profaned Capital",
"family": "Giant",
"image": "yhorm.jpg",
"imageUrl": "https://avatars.mds.yandex.net/i?id=6f98fd5062453d73cdf62874cb0493ea_l-5234162-images-thumbs&n=13"
},
{
"id": 13,
"firstName": "Lothric",
"lastName": "The Exiled Prince",
"fullName": "Lothric, the Exiled Prince",
"title": "Prince of Lothric",
"family": "Royalty",
"image": "lothric.jpg",
"imageUrl": "https://avatars.mds.yandex.net/i?id=6f98fd5062453d73cdf62874cb0493ea_l-5234162-images-thumbs&n=13"
},
{
"id": 14,
"firstName": "Emma",
"lastName": "The Fire Keeper",
"fullName": "Emma, the Fire Keeper",
"title": "Keeper of the Flame",
"family": "Fire",
"image": "emma.jpg",
"imageUrl": "https://avatars.mds.yandex.net/i?id=6f98fd5062453d73cdf62874cb0493ea_l-5234162-images-thumbs&n=13"
},
{
"id": 15,
"firstName": "Farron",
"lastName": "The Abyss Watchers",
"fullName": "Farron, the Abyss Watchers",
"title": "Watchers of the Abyss",
"family": "Knight",
"image": "farron.jpg",
"imageUrl": "https://avatars.mds.yandex.net/i?id=6f98fd5062453d73cdf62874cb0493ea_l-5234162-images-thumbs&n=13"
},
{
"id": 16,
"firstName": "Gundyr",
"lastName": "The Champion",
"fullName": "Gundyr, the Champion",
"title": "Champion of Ash",
"family": "Ash",
"image": "gundyr.jpg",
"imageUrl": "https://avatars.mds.yandex.net/i?id=6f98fd5062453d73cdf62874cb0493ea_l-5234162-images-thumbs&n=13"
},
{
"id": 17,
"firstName": "Lorian",
"lastName": "Eldest Prince",
"fullName": "Lorian, the Eldest Prince",
"title": "Eldest of Lothric",
"family": "Royalty",
"image": "lorian.jpg",
"imageUrl": "https://avatars.mds.yandex.net/i?id=6f98fd5062453d73cdf62874cb0493ea_l-5234162-images-thumbs&n=13"
},
{
"id": 18,
"firstName": "Midir",
"lastName": "The Black Dragon",
"fullName": "Midir, the Black Dragon",
"title": "Ancient Dragon",
"family": "Dragon",
"image": "midir.jpg",
"imageUrl": "https://avatars.mds.yandex.net/i?id=6f98fd5062453d73cdf62874cb0493ea_l-5234162-images-thumbs&n=13"
},
{
"id": 19,
"firstName": "Vinheim",
"lastName": "The Great Sage",
"fullName": "Vinheim, the Great Sage",
"title": "Master of Sorcery",
"family": "Sage",
"image": "vinheim.jpg",
"imageUrl": "https://avatars.mds.yandex.net/i?id=6f98fd5062453d73cdf62874cb0493ea_l-5234162-images-thumbs&n=13"
},
{
"id": 20,
"firstName": "Lothric",
"lastName": "The Exiled Prince",
"fullName": "Lothric, the Exiled Prince",
"title": "Prince of Lothric",
"family": "Royalty",
"image": "lothric.jpg",
"imageUrl": "https://avatars.mds.yandex.net/i?id=6f98fd5062453d73cdf62874cb0493ea_l-5234162-images-thumbs&n=13"
}
]



app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Adjust as necessary for your use case
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/characters/")
async def get_characters(
    fullName: Optional[str] = Query(None, description="Поиск по имени"),
    page: int = Query(1, ge=1, description="Номер страницы"),
    size: int = Query(10, ge=1, description="Размер страницы")
) -> List[dict]:
    filtered_data = (
        [item for item in data if fullName.lower() in item["fullName"].lower()]
        if fullName else data
    )

    start_index = (page - 1) * size
    end_index = page * size
    paginated_data = filtered_data[start_index:end_index]

    return paginated_data


