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
 {
    "id": "3",
     "attributes": {
         "name": "Anastacia of Astora",
         "shortdescription": "Немая хранительница огня находится в темнице, расположенной под костром, который она оберегает.",
          "location":"Храм Огня",
          "health":"-",
          "soul":"-",
          "items":"-",
          "description": "Анастасия из Асторы – хранительница огня локации Храм Огня. Найти её можно запертой на один уровень ниже костра. При поднесении ей душ Хранительнец Огня, будет усиливать эффективность фляг с эстусом. В первой половине игры она будет молчать при попытке поговорить с ней. ",
          "image": "https://static.wikia.nocookie.net/darksouls/images/2/2e/Анастасия_из_Асторы.png/revision/latest?cb=20140208183714&path-prefix=ru"
    }
  },
 {
    "id": "4",
    "attributes": {
        "name": "Andre of Astora",
        "shortdescription": "Родом из Асторы, он поселился в подвале старой церкви, которая соединяет Уезд Нежити с Садом Тёмных Корней.",
        "location": "Уезд Нежити",
        "soul": "1,000",
        "items": "Кузнечный молот, Человечность х3, Символ Арториаса (если еще не приобретен)",
        "description": "Родом из Асторы, он поселился в подвале старой церкви, которая соединяет Уезд Нежити с Садом Тёмных Корней. Он умеет ремонтировать и модернизировать ваше оружие и броню в обмен на души и материалы. Также может изменить определённое оружие, если получит подходящий Уголь.",
        "image": "https://i.ytimg.com/vi/oG-FqAmGbkc/hqdefault.jpg"
    }
  },
  {
    "id": "5",
    "attributes": {
        "name": "Vamos",
        "shortdescription": "ворчливый кузнец-скелет, который обитает в локации Катакомбы",
        "location":"Катакомбы",
        "health":"-",
        "soul":"1,000",
        "items":"Королевский шлем, Вамосов молот, Человечность",
        "description": "Может создавать оружие огня и хаоса при наличии огненного угля хаоса и большого огненного угля, а также улучшать его.",
        "image": "https://i.playground.ru/p/RitXWtQKESP2lDZBr7yjXg.jpeg"
    }
  },
  {
    "id": "6",
    "attributes": {
        "name": "Witch Beatrice",
        "shortdescription": "дружественный фантом ",
        "location":"Сад Темных Корней, Руины Нового Лондо",
        "health":"-",
        "soul":"-",
        "items":"-",
        "description": "Почти все волшебники, которые пользуются катализаторами, обучались в Школе Драконов, но Беатрис — исключение. Она бросила вызов Бездне для того, чтобы рассказать об этом сложном испытании, но погибла от рук Четырёх Королей, а именно умерла от полученных ранений в Долине Драконов, поскольку именно там находится её сет.",
        "image": "https://static.wikia.nocookie.net/darksouls/images/c/c7/Ведьма_Беатрис.png/revision/latest/scale-to-width-down/1000?cb=20180530095109&path-prefix=ru"
    }
  },
  {
    "id": "7",
    "attributes": {
        "name": "Chaos Witch Quelaag",
        "shortdescription": "Одна из дочерей ведьмы Изалита.",
        "location":"Владение Квилег",
        "health":"3.139, 6.027 (NG+1), 7.534 (NG+6)",
        "soul":"20.000 60.000 (NG+1), 64.200 (NG+2), 66.000 (NG+3), 68.400 (NG+4), 71.400 (NG+5), 75.000 (NG+6), 108.000 (NG+6)",
        "items":"Душа Квилег, Двойная человечность",
        "description": "Вместе со своей сестрой бежала из Изалита, когда город охватило Пламя Хаоса. К несчастью, их затронули мутации, хотя и не полностью. Нижние части тел сестер превратились в огромных пауков. Квилег обосновалась в нижней части Чумного Города, где ей и её сестре стала служить зараженная Черногноем нежить.",
        "image": "https://static.wikia.nocookie.net/darksouls/images/6/67/Quelaag_battle.jpg/revision/latest?cb=20130405231049"
    }
  },
  {
    "id": "8",
    "attributes": {
        "name": "Patches",
        "shortdescription": "Мародёр, авантюрист и обманщик, ненавидящий священнослужителей.",
        "location":"Катакомбы, Склеп Великанов, Храм Огня",
        "health":"1,200",
        "soul":"2,000",
        "items":"Полукруглый топор, Человечность х4",
        "description": "Добро пожаловать в лавку сокровищ Верного Лоскутика! Мы скидываем цены, а не людей в пропасть!",
        "image": "https://avatars.mds.yandex.net/i?id=946ecb053d7fdd144f4f8a4f29435497_sr-13101499-images-thumbs&n=13"
    }
  },
  {
    "id": "9",
    "attributes": {
         "name": "Vince of Thorolund",
        "shortdescription": "Телохранитель Реи из Торолунда.",
      "health":"638-Храм Огня, 821-Склеп Великанов",
      "location":"Храм Огня,Склеп Великанов",
      "soul":"1.000",
      "items":"Человечность x5",
        "description": "Винс, как и Нико, были друзьями детства Реи из Торолунда.Они сопровождают Рею в поисках Обряда Возжигания.Появятся вместе с ней рядом с Петрусом в Храме Огня.",
        "image": "https://static.wikia.nocookie.net/darksouls/images/a/ae/Винс_из_Торолунда.jpg/revision/latest?cb=20131129183050&path-prefix=ru"
    }
  },
  {
    "id": "10",
    "attributes": {
         "name": "Gwyn, Lord of Cinder",
          "shortdescription": "На закате эры Древних Драконов Гвин нашёл одну из душ Повелителей, давшую ему божественное могущество.",
          "location":"Горнило Первого Пламени",
          "health":"4.250,6.545 (NG+1), 8.185 (NG+6)",
          "soul":"70.000, 140.000 (NG+1), 149.800 (NG+2), 154.000 (NG+3), 159.600 (NG+4), 166.600 (NG+5), 175.000 (NG+6)",
          "items":"Душа Гвина",
          "description": "Гвин, Повелитель Пепла, который связан с Первым Пламенем. Повелитель Гвин завещал большую часть силы богам и сгорел дотла ради Первого Пламени. Однако его душа всё равно насыщена мощной энергией.",
        "image": "https://avatars.mds.yandex.net/i?id=98bf139e61b767dd6be86a057499f8d7_l-5221497-images-thumbs&n=13"
    }
  },
  {
    "id": "11",
    "attributes": {
         "name": "Dark Sun Gwyndolin",
        "shortdescription": "Младший сын Повелителя Гвина",
      "location":"Анор Лондо",
      "health":"",
      "soul":"40.000, 120.000 (NG+1), 128.400 (NG+2), 132.000 (NG+3), 136.800 (NG+4), 142.800 (NG+5), 150.000 (NG+6)",
      "items":"Душа Гвиндолина",
        "description": "Гвиндолин — талантливый иллюзионист, так как в городском дворце он создал иллюзию своей сестры и поддерживал во всём Анор Лондо иллюзорный дневной свет. На момент событий игры Гвиндолин — последнее божество, оставшееся в Анор Лондо.",
        "image": "https://avatars.mds.yandex.net/i?id=db289eecaf2c23a973bf26f527c3de68754c70ef-6598320-images-thumbs&n=13"
    }
  },
  {
    "id": "12",
    "attributes": {
        "name": "Gwynevere, Princess of Sunlight",
        "shortdescription": "Дочь Повелителя Пепла и лидер ковенанта Стражи Принцессы.",
        "location":"Анор Лондо",
        "health":"-",
        "soul":"-",
        "items":"Великая Чаша",
        "description": "Одна из трёх детей Гвина и глава ковенанта Стражи Принцессы. Найти её можно во время прохождения игры в локации Анор Лондо",
        "image": "https://i.playground.ru/p/dsQO2EP_vCWvJibdzGsSNA.jpeg"
    }
  },
  {
    "id": "13",
    "attributes": {
         "name": "Hawkeye Gough",
       "shortdescription": "Командир великих лучников, которые в начале Эры Огня успешно сражались с драконами",
      "location":"Поселок Олачиль",
      "health":"-",
      "soul":"20,000",
      "items":"Сет Гоха,Большой лук Гоха",
        "description": "вое умение мастерски стрелять великан подтверждает, когда, будучи ослепленным, одним точным выстрелом сбивает Каламита. Причина ослепления в том, что щели для глаз в его шлеме запечатали древесной смолой те, кто ошибочно считал его жестоким великаном. На самом деле Гох очень миролюбив, уважительно обращается к игроку и довольно тепло отзывается о Кузнеце великане из Анор Лондо. Подтверждением их знакомства является спрятанное за великаном Кольцо с ястребом, собственность Соколиного Глаза.",
        "image": "https://avatars.mds.yandex.net/i?id=4f58c3b6ed78c35785d7453223d2854a_l-5255188-images-thumbs&n=13"
    }
  },
  {
    "id": "14",
    "attributes": {
         "name": "Griggs of Vinheim",
       "shortdescription": "Тихий, скромный волшебник из Винхейма. Является учеником Логана Большой Шляпы.",
      "location":"Нижний Город Нежити → Храм Огня → Крепость Сена",
      "health":"-",
      "soul":"1000",
      "items":"Кольцо с дремлющим драконом, Бесшумность, Человечность",
        "description": "Заперт в комнате в нижней части Города Нежити — как спуститесь с лестницы сразу направо, за заросший колодец. Он искал своего учителя, но не смог найти. Когда подойдёте к его двери, он позовёт на помощь. Дверь открывается с помощью ключа от жилища, который продаётся у Нежити-торговца.",
        "image": "https://avatars.mds.yandex.net/i?id=5d9d1389f6cc7386eaed765e23d39f7a_l-4558237-images-thumbs&n=13"
    }
  },
  {
    "id": "15",
    "attributes": {
         "name": "Batwing Demon",
         "shortdescription": "Небольшой летающий демон, который имеет опасное оружие — Демоническое копьё.",
      "location":"Анор Лондо",
      "health":"419, 734 (NG+)",
      "soul":"500,1500 (NG+),1875 (NG+6)",
      "items":"Демоническое копье",
        "description": "Небольшой летающий демон, который имеет опасное оружие — Демоническое копьё. При первой встрече дружественные демоны переносят протагониста в кат-сцене из Крепости Сена в Анор Лондо. Позднее встретятся такие же демоны, уже враждебно настроенные, которые являются довольно неприятными противниками.",
        "image": "https://i.playground.ru/p/AUI6ZPbU27UJLlGdxW1ttQ.jpeg"
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
