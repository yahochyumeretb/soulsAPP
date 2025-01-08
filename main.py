from fastapi import FastAPI, Query
from typing import Optional

app = FastAPI()

data = [
  {
    "id": "1",
    "attributes": {
        "name": "Artorias",
        "shortdescription": "",
      "location":"",
      "soul":"",
      "items":"",
        "description": "",
        "image": "https://i.pinimg.com/originals/0c/66/2a/0c662acc15b63e3c30113ae6ed8e7af5.jpg"
    }
  },
  {
    "id": "2",
    "attributes": {
         "name": "Alvina",
         "shortdescription": "",
      "location":"",
      "soul":"",
      "items":"",
        "description": "",
        "image": "https://i.pinimg.com/originals/0c/66/2a/0c662acc15b63e3c30113ae6ed8e7af5.jpg"
    }
  },
  {
    "id": "3",
    "attributes": {
         "name": "Anastacia of Astora",
         "shortdescription": "",
      "location":"",
      "soul":"",
      "items":"",
        "description": "",
        "image": "https://i.pinimg.com/originals/0c/66/2a/0c662acc15b63e3c30113ae6ed8e7af5.jpg"
    }
  },
  {
    "id": "4",
    "attributes": {
         "name": " Andre of Astora",
         "shortdescription": "",
      "location":"",
      "soul":"",
      "items":"",
        "description": "",
        "image": "https://i.pinimg.com/originals/0c/66/2a/0c662acc15b63e3c30113ae6ed8e7af5.jpg"
    }
  },
  {
    "id": "5",
    "attributes": {
         "name": "Vamos",
         "shortdescription": "",
      "location":"",
      "soul":"",
      "items":"",
        "description": "",
        "image": "https://i.pinimg.com/originals/0c/66/2a/0c662acc15b63e3c30113ae6ed8e7af5.jpg"
    }
  },
  {
    "id": "6",
    "attributes": {
          "name": "Witch Beatrice",
        "shortdescription": "",
      "location":"",
      "soul":"",
      "items":"",
        "description": "",
        "image": "https://i.pinimg.com/originals/0c/66/2a/0c662acc15b63e3c30113ae6ed8e7af5.jpg"
    }
  },
  {
    "id": "7",
    "attributes": {
         "name": " Witch of Izalith",
         "shortdescription": "",
      "location":"",
      "soul":"",
      "items":"",
        "description": "",
        "image": "https://i.pinimg.com/originals/0c/66/2a/0c662acc15b63e3c30113ae6ed8e7af5.jpg"
    }
  },
  {
    "id": "8",
    "attributes": {
        "name": "Patches",
        "shortdescription": "",
      "location":"",
      "soul":"",
      "items":"",
        "description": "",
        "image": "https://i.pinimg.com/originals/0c/66/2a/0c662acc15b63e3c30113ae6ed8e7af5.jpg"
    }
  },
  {
    "id": "9",
    "attributes": {
         "name": "Vince of Thorolund",
        "shortdescription": "",
      "location":"",
      "soul":"",
      "items":"",
        "description": "",
        "image": "https://i.pinimg.com/originals/0c/66/2a/0c662acc15b63e3c30113ae6ed8e7af5.jpg"
    }
  },
  {
    "id": "10",
    "attributes": {
         "name": "Gwyn, Lord of Cinder",
        "shortdescription": "",
      "location":"",
      "soul":"",
      "items":"",
        "description": "",
        "image": "https://i.pinimg.com/originals/0c/66/2a/0c662acc15b63e3c30113ae6ed8e7af5.jpg"
    }
  },
  {
    "id": "11",
    "attributes": {
         "name": "Dark Sun Gwyndolin",
        "shortdescription": "",
      "location":"",
      "soul":"",
      "items":"",
        "description": "",
        "image": "https://i.pinimg.com/originals/0c/66/2a/0c662acc15b63e3c30113ae6ed8e7af5.jpg"
    }
  },
  {
    "id": "12",
    "attributes": {
         "name": "Gwynevere, Princess of Sunlight",
        "shortdescription": "",
      "location":"",
      "soul":"",
      "items":"",
        "description": "",
        "image": "https://i.pinimg.com/originals/0c/66/2a/0c662acc15b63e3c30113ae6ed8e7af5.jpg"
    }
  },
  {
    "id": "13",
    "attributes": {
         "name": "Hawkeye Gough",
       "shortdescription": "",
      "location":"",
      "soul":"",
      "items":"",
        "description": "",
        "image": "https://i.pinimg.com/originals/0c/66/2a/0c662acc15b63e3c30113ae6ed8e7af5.jpg"
    }
  },
  {
    "id": "14",
    "attributes": {
         "name": "Griggs of Vinheim",
       "shortdescription": "",
      "location":"",
      "soul":"",
      "items":"",
        "description": "",
        "image": "https://i.pinimg.com/originals/0c/66/2a/0c662acc15b63e3c30113ae6ed8e7af5.jpg"
    }
  },
  {
    "id": "15",
    "attributes": {
         "name": "Batwing Demon",
         "shortdescription": "",
      "location":"",
      "soul":"",
      "items":"",
        "description": "",
        "image": "https://i.pinimg.com/originals/0c/66/2a/0c662acc15b63e3c30113ae6ed8e7af5.jpg"
    }
  },
  {
    "id": "16",
    "attributes": {
         "name": "Domhnall of Zena",
        "shortdescription": "",
      "location":"",
      "soul":"",
      "items":"",
        "description": "",
        "image": "https://i.pinimg.com/originals/0c/66/2a/0c662acc15b63e3c30113ae6ed8e7af5.jpg"
    }
  },
  {
    "id": "17",
    "attributes": {
         "name": "Dusk of Oolacile",
        "shortdescription": "",
      "location":"",
      "soul":"",
      "items":"",
        "description": "",
        "image": "https://i.pinimg.com/originals/0c/66/2a/0c662acc15b63e3c30113ae6ed8e7af5.jpg"
    }
  },
  {
    "id": "18",
    "attributes": {
         "name": "Chosen Undead",
        "shortdescription": "",
      "location":"",
      "soul":"",
      "items":"",
        "description": "",
        "image": "https://i.pinimg.com/originals/0c/66/2a/0c662acc15b63e3c30113ae6ed8e7af5.jpg"
    }
  },
  {
    "id": "19",
    "attributes": {
         "name": "Ingward",
       "shortdescription": "",
      "location":"",
      "soul":"",
      "items":"",
        "description": "",
        "image": "https://i.pinimg.com/originals/0c/66/2a/0c662acc15b63e3c30113ae6ed8e7af5.jpg"
    }
  },
  {
    "id": "20",
    "attributes": {
         "name": "Darkstalker Kaathe",
        "shortdescription": "",
      "location":"",
      "soul":"",
      "items":"",
        "description": "",
        "image": "https://i.pinimg.com/originals/0c/66/2a/0c662acc15b63e3c30113ae6ed8e7af5.jpg"
    }
  },
  {
    "id": "21",
    "attributes": {
         "name": "Stone Dragon",
         "shortdescription": "",
      "location":"",
      "soul":"",
      "items":"",
        "description": "",
        "image": "https://i.pinimg.com/originals/0c/66/2a/0c662acc15b63e3c30113ae6ed8e7af5.jpg"
    }
  },
  {
    "id": "22",
    "attributes": {
         "name": "Quelana of Izalith",
        "shortdescription": "",
      "location":"",
      "soul":"",
      "items":"",
        "description": "",
        "image": "https://i.pinimg.com/originals/0c/66/2a/0c662acc15b63e3c30113ae6ed8e7af5.jpg"
    }
  },
  {
    "id": "23",
    "attributes": {
         "name": "Kirk, Knight of Thorns",
      "shortdescription": "",
      "location":"",
      "soul":"",
      "items":"",
        "description": "",
        "image": "https://i.pinimg.com/originals/0c/66/2a/0c662acc15b63e3c30113ae6ed8e7af5.jpg"
    }
  },
  {
    "id": "24",
    "attributes": {
         "name": "Xanthous King, Jeremiah",
        "shortdescription": "",
      "location":"",
      "soul":"",
      "items":"",
        "description": "",
        "image": "https://i.pinimg.com/originals/0c/66/2a/0c662acc15b63e3c30113ae6ed8e7af5.jpg"
    }
  },
  {
    "id": "25",
    "attributes": {
         "name": "Giant Blacksmith",
       "shortdescription": "",
      "location":"",
      "soul":"",
      "items":"",
        "description": "",
        "image": "https://i.pinimg.com/originals/0c/66/2a/0c662acc15b63e3c30113ae6ed8e7af5.jpg"
    }
  },
  {
    "id": "26",
    "attributes": {
         "name": "Laurentius of the Great Swamp",
        "shortdescription": "",
      "location":"",
      "soul":"",
      "items":"",
        "description": "",
        "image": "https://i.pinimg.com/originals/0c/66/2a/0c662acc15b63e3c30113ae6ed8e7af5.jpg"
    }
  },
  {
    "id": "27",
    "attributes": {
         "name": "Forest Hunter Thief",
      "shortdescription": "",
      "location":"",
      "soul":"",
      "items":"",
        "description": "",
        "image": "https://i.pinimg.com/originals/0c/66/2a/0c662acc15b63e3c30113ae6ed8e7af5.jpg"
    }
  },
  {
    "id": "28",
    "attributes": {
         "name": "Forest Hunter Cleric",
        "shortdescription": "",
      "location":"",
      "soul":"",
      "items":"",
        "description": "",
        "image": "https://i.pinimg.com/originals/0c/66/2a/0c662acc15b63e3c30113ae6ed8e7af5.jpg"
    }
  },
  {
    "id": "29",
    "attributes": {
         "name": " Forest Hunter Sorcerer",
       "shortdescription": "",
      "location":"",
      "soul":"",
      "items":"",
        "description": "",
        "image": "https://i.pinimg.com/originals/0c/66/2a/0c662acc15b63e3c30113ae6ed8e7af5.jpg"
    }
  },
  {
    "id": "30",
    "attributes": {
         "name": "Forest Hunter Bandit",
        "shortdescription": "",
      "location":"",
      "soul":"",
      "items":"",
        "description": "",
        "image": "https://i.pinimg.com/originals/0c/66/2a/0c662acc15b63e3c30113ae6ed8e7af5.jpg"
    }
  },
  {
    "id": "31",
    "attributes": {
         "name": "Forest Hunter Knight",
        "shortdescription": "",
      "location":"",
      "soul":"",
      "items":"",
        "description": "",
        "image": "https://i.pinimg.com/originals/0c/66/2a/0c662acc15b63e3c30113ae6ed8e7af5.jpg"
    }
  },
  {
    "id": "32",
    "attributes": {
         "name": "Big Hat Logan",
         "shortdescription": "",
      "location":"",
      "soul":"",
      "items":"",
        "description": "",
        "image": "https://i.pinimg.com/originals/0c/66/2a/0c662acc15b63e3c30113ae6ed8e7af5.jpg"
    }
  },
  {
    "id": "33",
    "attributes": {
         "name": "Knight Lautrec of Carim",
         "shortdescription": "",
      "location":"",
      "soul":"",
      "items":"",
        "description": "",
        "image": "https://i.pinimg.com/originals/0c/66/2a/0c662acc15b63e3c30113ae6ed8e7af5.jpg"
    }
  },
  {
    "id": "34",
    "attributes": {
         "name": "Archer",
        "shortdescription": "",
      "location":"",
      "soul":"",
      "items":"",
        "description": "",
        "image": "https://i.pinimg.com/originals/0c/66/2a/0c662acc15b63e3c30113ae6ed8e7af5.jpg"
    }
  },
  {
    "id": "35",
    "attributes": {
         "name": "Maneater Mildred",
        "shortdescription": "",
      "location":"",
      "soul":"",
      "items":"",
        "description": "",
        "image": "https://i.pinimg.com/originals/0c/66/2a/0c662acc15b63e3c30113ae6ed8e7af5.jpg"
    }
  },
  {
    "id": "40",
    "attributes": {
         "name": "Undead Male Merchant",
         "shortdescription": "",
      "location":"",
      "soul":"",
      "items":"",
        "description": "",
        "image": "https://i.pinimg.com/originals/0c/66/2a/0c662acc15b63e3c30113ae6ed8e7af5.jpg"
    }
  },
  {
    "id": "41",
    "attributes": {
         "name": "Nico of Thorolund",
        "shortdescription": "",
      "location":"",
      "soul":"",
      "items":"",
        "description": "",
        "image": "https://i.pinimg.com/originals/0c/66/2a/0c662acc15b63e3c30113ae6ed8e7af5.jpg"
    }
  },
  {
    "id": "42",
    "attributes": {
         "name": "Giant Crow",
        "shortdescription": "",
      "location":"",
      "soul":"",
      "items":"",
        "description": "",
        "image": "https://i.pinimg.com/originals/0c/66/2a/0c662acc15b63e3c30113ae6ed8e7af5.jpg"
    }
  },
  {
    "id": "43",
    "attributes": {
         "name": " Oswald of Carim",
       "shortdescription": "",
      "location":"",
      "soul":"",
      "items":"",
        "description": "",
        "image": "https://i.pinimg.com/originals/0c/66/2a/0c662acc15b63e3c30113ae6ed8e7af5.jpg"
    }
  },
  {
    "id": "44",
    "attributes": {
         "name": "Oscar, Knight of Astora",
        "shortdescription": "",
      "location":"",
      "soul":"",
      "items":"",
        "description": "",
        "image": "https://i.pinimg.com/originals/0c/66/2a/0c662acc15b63e3c30113ae6ed8e7af5.jpg"
    }
  },
  {
    "id": "45",
    "attributes": {
         "name": "Paladin Leeroy",
        "shortdescription": "",
      "location":"",
      "soul":"",
      "items":"",
        "description": "",
        "image": "https://i.pinimg.com/originals/0c/66/2a/0c662acc15b63e3c30113ae6ed8e7af5.jpg"
    }
  },
  {
    "id": "46",
    "attributes": {
         "name": "Petrus of Thorolund",
         "shortdescription": "",
      "location":"",
      "soul":"",
      "items":"",
        "description": "",
        "image": "https://i.pinimg.com/originals/0c/66/2a/0c662acc15b63e3c30113ae6ed8e7af5.jpg"
    }
  },
  {
    "id": "47",
    "attributes": {
         "name": "The Fair Lady",
         "shortdescription": "",
      "location":"",
      "soul":"",
      "items":"",
        "description": "",
        "image": "https://i.pinimg.com/originals/0c/66/2a/0c662acc15b63e3c30113ae6ed8e7af5.jpg"
    }
  },
  {
    "id": "48",
    "attributes": {
         "name": "Crossbreed Priscilla",
        "shortdescription": "",
      "location":"",
      "soul":"",
      "items":"",
        "description": "",
        "image": "https://i.pinimg.com/originals/0c/66/2a/0c662acc15b63e3c30113ae6ed8e7af5.jpg"
    }
  },
  {
    "id": "49",
    "attributes": {
         "name": " Reah of Thorolund",
        "shortdescription": "",
      "location":"",
      "soul":"",
      "items":"",
        "description": "",
        "image": "https://i.pinimg.com/originals/0c/66/2a/0c662acc15b63e3c30113ae6ed8e7af5.jpg"
    }
  },
  {
    "id": "50",
    "attributes": {
         "name": "Rickert of Vinheim",
        "shortdescription": "",
      "location":"",
      "soul":"",
      "items":"",
        "description": "",
        "image": "https://i.pinimg.com/originals/0c/66/2a/0c662acc15b63e3c30113ae6ed8e7af5.jpg"
    }
  },
  {
    "id": "51",
    "attributes": {
         "name": "Darkmoon Knightess",
        "shortdescription": "",
      "location":"",
      "soul":"",
      "items":"",
        "description": "",
        "image": "https://i.pinimg.com/originals/0c/66/2a/0c662acc15b63e3c30113ae6ed8e7af5.jpg"
    }
  },
  {
    "id": "52",
    "attributes": {
         "name": "Lord's Blade Ciaran",
        "shortdescription": "",
      "location":"",
      "soul":"",
      "items":"",
        "description": "",
        "image": "https://i.pinimg.com/originals/0c/66/2a/0c662acc15b63e3c30113ae6ed8e7af5.jpg"
    }
  },
  {
    "id": "53",
    "attributes": {
         "name": "Sieglinde of Catarina",
        "shortdescription": "",
      "location":"",
      "soul":"",
      "items":"",
        "description": "",
        "image": "https://i.pinimg.com/originals/0c/66/2a/0c662acc15b63e3c30113ae6ed8e7af5.jpg"
    }
  },
  {
    "id": "54",
    "attributes": {
         "name": "Siegmeyer of Catarina",
         "shortdescription": "",
      "location":"",
      "soul":"",
      "items":"",
        "description": "",
        "image": "https://i.pinimg.com/originals/0c/66/2a/0c662acc15b63e3c30113ae6ed8e7af5.jpg"
    }
  },
  {
    "id": "55",
    "attributes": {
         "name": "Great Grey Wolf Sif",
        "shortdescription": "",
      "location":"",
      "soul":"",
      "items":"",
        "description": "",
        "image": "https://i.pinimg.com/originals/0c/66/2a/0c662acc15b63e3c30113ae6ed8e7af5.jpg"
    }
  },
  {
    "id": "56",
    "attributes": {
         "name": " Snuggly the Crow",
       "shortdescription": "",
      "location":"",
      "soul":"",
      "items":"",
        "description": "",
        "image": "https://i.pinimg.com/originals/0c/66/2a/0c662acc15b63e3c30113ae6ed8e7af5.jpg"
    }
  },
  {
    "id": "57",
    "attributes": {
         "name": "Solaire of Astora",
        "shortdescription": "",
      "location":"",
      "soul":"",
      "items":"",
        "description": "",
        "image": "https://i.pinimg.com/originals/0c/66/2a/0c662acc15b63e3c30113ae6ed8e7af5.jpg"
    }
  },
  {
    "id": "58",
    "attributes": {
         "name": "Black Iron Tarkus",
        "shortdescription": "",
      "location":"",
      "soul":"",
      "items":"",
        "description": "",
        "image": "https://i.pinimg.com/originals/0c/66/2a/0c662acc15b63e3c30113ae6ed8e7af5.jpg"
    }
  },
  {
    "id": "59",
    "attributes": {
         "name": "Shiva's Bodyguard",
         "shortdescription": "",
      "location":"",
      "soul":"",
      "items":"",
        "description": "",
        "image": "https://i.pinimg.com/originals/0c/66/2a/0c662acc15b63e3c30113ae6ed8e7af5.jpg"
    }
  },
  {
    "id": "60",
    "attributes": {
         "name": " Undead Female Merchant",
         "shortdescription": "",
      "location":"",
      "soul":"",
      "items":"",
        "description": "",
        "image": "https://i.pinimg.com/originals/0c/66/2a/0c662acc15b63e3c30113ae6ed8e7af5.jpg"
    }
  },
  {
    "id": "61",
    "attributes": {
         "name": "Crestfallen Warrior",
        "shortdescription": "",
      "location":"",
      "soul":"",
      "items":"",
        "description": "",
        "image": "https://i.pinimg.com/originals/0c/66/2a/0c662acc15b63e3c30113ae6ed8e7af5.jpg"
    }
  },
  {
    "id": "62",
    "attributes": {
         "name": "Crestfallen Merchant",
         "shortdescription": "",
      "location":"",
      "soul":"",
      "items":"",
        "description": "",
        "image": "https://i.pinimg.com/originals/0c/66/2a/0c662acc15b63e3c30113ae6ed8e7af5.jpg"
    }
  },
  {
    "id": "63",
    "attributes": {
         "name": " Kingseeker Frampt",
        "shortdescription": "",
      "location":"",
      "soul":"",
      "items":"",
        "description": "",
        "image": "https://i.pinimg.com/originals/0c/66/2a/0c662acc15b63e3c30113ae6ed8e7af5.jpg"
    }
  },
  {
    "id": "64",
    "attributes": {
         "name": "Havel the Rock",
        "shortdescription": "",
      "location":"",
      "soul":"",
      "items":"",
        "description": "",
        "image": "https://i.pinimg.com/originals/0c/66/2a/0c662acc15b63e3c30113ae6ed8e7af5.jpg"
    }
  },
  {
    "id": "65",
    "attributes": {
         "name": " Marvellous Chester",
        "shortdescription": "",
      "location":"",
      "soul":"",
      "items":"",
        "description": "",
        "image": "https://i.pinimg.com/originals/0c/66/2a/0c662acc15b63e3c30113ae6ed8e7af5.jpg"
    }
  },
  {
    "id": "66",
    "attributes": {
         "name": "Shiva of the East",
         "shortdescription": "",
      "location":"",
      "soul":"",
      "items":"",
        "description": "",
        "image": "https://i.pinimg.com/originals/0c/66/2a/0c662acc15b63e3c30113ae6ed8e7af5.jpg"
    }
  },
  {
    "id": "67",
    "attributes": {
         "name": "Elizabeth",
        "shortdescription": "",
      "location":"",
      "soul":"",
      "items":"",
        "description": "",
        "image": "https://i.pinimg.com/originals/0c/66/2a/0c662acc15b63e3c30113ae6ed8e7af5.jpg"
    }
  },
  {
    "id": "68",
    "attributes": {
         "name": "Eingyi",
        "shortdescription": "",
      "location":"",
      "soul":"",
      "items":"",
        "description": "",
        "image": "https://i.pinimg.com/originals/0c/66/2a/0c662acc15b63e3c30113ae6ed8e7af5.jpg"
    }
  },
  {
    "id": "69",
    "attributes": {
         "name": "",
        "shortdescription": "",
      "location":"",
      "soul":"",
      "items":"",
        "description": "",
        "image": "https://i.pinimg.com/originals/0c/66/2a/0c662acc15b63e3c30113ae6ed8e7af5.jpg"
    }
  },
  {
    "id": "70",
    "attributes": {
         "name": "",
         "shortdescription": "",
      "location":"",
      "soul":"",
      "items":"",
        "description": "",
        "image": "https://i.pinimg.com/originals/0c/66/2a/0c662acc15b63e3c30113ae6ed8e7af5.jpg"
    }
  }
]


@app.get("/characters/")
async def get_characters(
    fullName: Optional[str] = Query(None, description="Поиск по имени"),
    page: int = Query(1, ge=1, description="Номер страницы"),
    size: int = Query(10, ge=1, description="Размер страницы")
) -> dict:
    filtered_data = (
        [item for item in data if fullName.lower() in item["attributes"]["name"].lower()]
        if fullName else data
    )

    start_index = (page-1) * size
    end_index = page * size
    paginated_data = filtered_data[start_index:end_index]

    return {
        "meta": {
          "pagination": {
              "next": page + 1
          }
        },
        "data": paginated_data
    }
