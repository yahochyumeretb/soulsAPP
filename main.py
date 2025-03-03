from fastapi import FastAPI, Query
from typing import Optional

app = FastAPI()

data = [
  {
    "id": "1",
    "attributes": {
      "name": "Artorias",
      "shortdescription": "Один из четырёх Рыцарей Гвина, легендарный Путник Бездны.",
      "location":"Поселок Олачиль",
      "health":"3750, 5887 (NG+1), 6300 (NG+2), 6476 (NG+3), 7359 (NG+6)",
      "soul":" 50.000 100.000 (NG+1)107.000 (NG+2)110.000 (NG+3) 114.000 (NG+4)119.000 (NG+5) 125.000 (NG+6)",
      "items":"Душа Арториаса",
      "description": "После падения Четырёх Королей во Тьму, задачей рыцаря стала борьба с тёмными духами. Однако с угрозой, идущей уже из поселка Олачиль, он так и не смог справиться, и Бездна поглотила его. последним жестом, отдав свой щит, он лишь успел защитить своего товарища, волка Сифа.Так мы и встречаем его, избитого и одержимого, но всё ещё внушающего страх. Арториас сражается с нами только правой рукой, так как левая рука сломана. Доспехи искажены Бездной, а поножи и вовсе рассыпаются. Теперь легендарный рыцарь богов, искалеченный и сломленный, дерется, как бешеный зверь, и использует Тьму для усиления себя. Единственный способ спасти его от Бездны — убить.",
      "image": "https://i.pinimg.com/originals/0c/66/2a/0c662acc15b63e3c30113ae6ed8e7af5.jpg"
    }
  },
  {
    "id": "2",
    "attributes": {
        "name": "Alvina",
        "shortdescription": "Живет с начала Эры Огня.",
        "location":"Сад Темных Корней",
        "health":"-",
        "soul":"-",
        "items":"-",
        "description": "Сиф Великий Волк, Альвина и Арториас Путник Бездны — старые близкие друзья. Вероятно, они познакомились в Королевском лесу, когда рыцарь Гвина прибыл в Олачиль, или намного раньше. Кроме того, возможно, Альвина также, как и маленький Сиф, сопровождала Путника Бездны в его непростой миссии. Когда Арториас пал, а Сиф был оставлен в Ущелье Бездны под защитой магического щита, именно Альвина отводит протагониста к волчонку. Она говорит на человеческом языке, хотя можно услышать еще и кошачье мурчанье",
        "image": "https://static.wikia.nocookie.net/darksouls/images/7/74/Альвина.jpg/revision/latest/scale-to-width-down/1200?cb=20130329075649&path-prefix=ru"
    }
  },
  
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
