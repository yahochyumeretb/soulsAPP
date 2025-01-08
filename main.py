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
        "shortdescription": "",
        "location":"",
        "health":"",
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
      "health":"",
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
      "health":"",
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
      "health":"",
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
      "health":"",
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
      "health":"",
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
      "health":"",
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
      "health":"",
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
      "health":"",
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
      "health":"",
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
      "health":"",
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
      "health":"",
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
      "health":"",
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
      "health":"",
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
      "health":"",
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
      "health":"",
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
      "health":"",
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
      "health":"",
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
      "health":"",
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
      "health":"",
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
      "health":"",
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
      "health":"",
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
      "health":"",
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
      "health":"",
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
      "health":"",
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
      "health":"",
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
      "health":"",
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
      "health":"",
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
      "health":"",
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
      "health":"",
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
      "health":"",
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
      "health":"",
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
      "health":"",
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
      "health":"",
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
      "health":"",
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
      "health":"",
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
      "health":"",
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
      "health":"",
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
      "health":"",
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
      "health":"",
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
      "health":"",
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
      "health":"",
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
      "health":"",
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
      "health":"",
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
      "health":"",
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
      "health":"",
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
      "health":"",
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
      "health":"",
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
      "health":"",
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
      "health":"",
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
      "health":"",
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
      "health":"",
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
      "health":"",
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
      "health":"",
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
      "health":"",
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
