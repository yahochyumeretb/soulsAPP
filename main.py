from fastapi import FastAPI, Query
from typing import Optional

app = FastAPI()

data = [
  {
    "id": "1",
    "attributes": {
        "name": "Artorias",
        "shortdescription": "Delicate cake with cocoa",
        "description": "350 kcal per serving",
        "image": "https://i.pinimg.com/736x/9b/36/f0/9b36f04319f5e4f615af7abc7679fe8d.jpg"
    }
  },
  {
    "id": "2",
    "attributes": {
         "name": "Artorias",
        "shortdescription": "Delicate cake with cocoa",
        "description": "350 kcal per serving",
        "image": "https://i.pinimg.com/736x/9b/36/f0/9b36f04319f5e4f615af7abc7679fe8d.jpg"
    }
  },
  {
    "id": "3",
    "attributes": {
         "name": "Artorias",
        "shortdescription": "Delicate cake with cocoa",
        "description": "350 kcal per serving",
        "image": "https://i.pinimg.com/736x/9b/36/f0/9b36f04319f5e4f615af7abc7679fe8d.jpg"
    }
  },
  {
    "id": "4",
    "attributes": {
         "name": "Artorias",
        "shortdescription": "Delicate cake with cocoa",
        "description": "350 kcal per serving",
        "image": "https://i.pinimg.com/736x/9b/36/f0/9b36f04319f5e4f615af7abc7679fe8d.jpg"
    }
  },
  {
    "id": "5",
    "attributes": {
         "name": "Artorias",
        "shortdescription": "Delicate cake with cocoa",
        "description": "350 kcal per serving",
        "image": "https://i.pinimg.com/736x/9b/36/f0/9b36f04319f5e4f615af7abc7679fe8d.jpg"
    }
  },
  {
    "id": "6",
    "attributes": {
          "name": "Artorias",
        "shortdescription": "Delicate cake with cocoa",
        "description": "350 kcal per serving",
        "image": "https://i.pinimg.com/736x/9b/36/f0/9b36f04319f5e4f615af7abc7679fe8d.jpg"
    }
  },
  {
    "id": "7",
    "attributes": {
         "name": "Artorias",
        "shortdescription": "Delicate cake with cocoa",
        "description": "350 kcal per serving",
        "image": "https://i.pinimg.com/736x/9b/36/f0/9b36f04319f5e4f615af7abc7679fe8d.jpg"
    }
  },
  {
    "id": "8",
    "attributes": {
        "name": "Artorias",
        "shortdescription": "Delicate cake with cocoa",
        "description": "350 kcal per serving",
        "image": "https://i.pinimg.com/736x/9b/36/f0/9b36f04319f5e4f615af7abc7679fe8d.jpg"
    }
  },
  {
    "id": "9",
    "attributes": {
         "name": "Artorias",
        "shortdescription": "Delicate cake with cocoa",
        "description": "350 kcal per serving",
        "image": "https://i.pinimg.com/736x/9b/36/f0/9b36f04319f5e4f615af7abc7679fe8d.jpg"
    }
  },
  {
    "id": "10",
    "attributes": {
         "name": "Artorias",
        "shortdescription": "Delicate cake with cocoa",
        "description": "350 kcal per serving",
        "image": "https://i.pinimg.com/736x/9b/36/f0/9b36f04319f5e4f615af7abc7679fe8d.jpg"
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
