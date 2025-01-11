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
  {
    "id": "16",
    "attributes": {
         "name": "Domhnall of Zena",
        "shortdescription": "персонаж-торговец",
      "location":"Глубины → Храм Огня",
      "health":"-",
      "soul":"1000",
      "items":"-",
        "description": "персонаж-торговец",
        "image": "https://static.wikia.nocookie.net/darksouls/images/d/dc/Домналл_из_Зены.png/revision/latest?cb=20130327105547&path-prefix=ru"
    }
  },
  {
    "id": "17",
    "attributes": {
         "name": "Dusk of Oolacile",
        "shortdescription": "персонаж-торговец",
      "location":"Озеро Темных Корней → Ущелье Бездны",
      "health":"-",
      "soul":"1000",
      "items":"",
        "description": "персонаж-торговец",
        "image": "https://static.wikia.nocookie.net/darksouls/images/c/cf/Заря_Олачиля.jpg/revision/latest?cb=20161013180646&path-prefix=ru"
    }
  },
  {
    "id": "18",
    "attributes": {
         "name": "Chosen Undead",
        "shortdescription": "протагонист игры",
      "location":"-",
      "health":"-",
      "soul":"-",
      "items":"-",
        "description": "Избранный Мертвец был заточен в Северном Прибежище Нежити и доживал свои последние дни, будучи опустошённым, но ещё сохранившим остатки разума, в окружении полых, к которым он скоро присоединился, если бы не помощь Оскара, который помог ему выбраться из камеры. Выбравшись, он пошел искать своего спасителя, но опоздал — герой находит Оскара умирающим от ран в результате падения. Избранный успел дойти до рыцаря и тот, на смертном одре, попросил Избранного об одном одолжении. Рыцарь рассказал ему о пророчестве, об Избранном Мертвеце, который изменит судьбу всей нежити и избавит её от проклятия. Для этого нужно было отправиться в земли древних Повелителей, в Лордран, и, ударив в Колокол, узнать судьбу нежити. Рассказав это и отдав Избранному Флягу с Эстусом, Оскар скончался. Возле выхода из Прибежища перед Избранным появляется Демон. После победы ему ничто не препятствовало, и Мертвец отправился в древние земли Повелителей, Лордран, чтобы найти свою судьбу.",
        "image": "https://static.wikia.nocookie.net/darksouls/images/5/5e/Избранный_Немертвый.png/revision/latest?cb=20171105205903&path-prefix=ru"
    }
  },
  {
    "id": "19",
    "attributes": {
         "name": "Ingward",
       "shortdescription": "Последний из трех Хранителей Печати, оставшийся в Руинах Нового Лондо",
      "location":"Руины Нового Лондо → Храм Огня",
      "health":"-",
      "soul":"1000",
      "items":"Ключ от Печати",
        "description": "Последний из трех Хранителей Печати, оставшийся в Руинах Нового Лондо, дабы сдерживать Темных духов и Четырех Королей. Он даст вам Ключ от Печати после получения Великой Чаши. Он нужен, чтобы слить воду из Руин и открыть путь к Четырем королям.",
        "image": "https://static.wikia.nocookie.net/darksouls/images/b/b7/Ингвард.jpg/revision/latest?cb=20130421140422&path-prefix=ru"
    }
  },
  {
    "id": "20",
    "attributes": {
         "name": "Darkstalker Kaathe",
        "shortdescription": "один из двух изначальных змеев, которых игрок может встретить в игре.",
      "location":"Бездна",
      "health":"-",
      "soul":"-",
      "items":"-",
        "description": " один из двух изначальных змеев, которых игрок может встретить в игре. В отличие от другого змея, Фрампта, он преследует совсем другую цель и не заинтересован в продлении Эры Огня. Все действия змея направлены на усиление Бездны, свержение богов Анор Лондо и возвышение нового Темного Повелителя среди людей.",
        "image": "https://static.wikia.nocookie.net/darksouls/images/2/28/Каас.jpg/revision/latest?cb=20130327105816&path-prefix=ru"
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
        "shortdescription": "персонаж-торговец",
      "location":"Чумной Город",
      "health":"-",
      "soul":"1000",
      "items":"Огненная буря",
        "description": "Бойся пламени, иначе оно пожрёт тебя и испепелит твою душу. Не хотелось бы увидеть это ещё раз...",
        "image": "https://uploads.worldanvil.com/uploads/images/63d6d1f05df69e9ba685d5b56d724a73.jpg"
    }
  },
  {
    "id": "23",
    "attributes": {
         "name": "Kirk, Knight of Thorns",
      "shortdescription": "враждебный фантом",
      "location":"Глубины, Руины Демонов, Забытый Изалит",
      "health":"689",
      "soul":"5,938 (Глубины),26,950 (Руины Демонов и Забытый Изалит)",
      "items":"Зазубренный прямой меч,Шипастый щит",
        "description": "Тёмный дух Кирка будет пытаться убить вас трижды за всю игру. Он экипирован в сет брони и оружия из шипов, которые вызывают кровотечение. После трёх его поражений его труп будет находиться около Прекрасной Госпожи, из чего можно сделать вывод, что он охотился на других мертвецов, дабы добывать человечность для облегчения страданий Прекрасной Госпожи.",
        "image": "https://static.wikia.nocookie.net/darksouls/images/7/77/Kirk01.jpg/revision/latest?cb=20130326060500&path-prefix=ru"
    }
  },
  {
    "id": "24",
    "attributes": {
         "name": "Xanthous King, Jeremiah",
        "shortdescription": "враждебный фантом",
      "location":"Нарисованный мир Ариамиса",
      "health":"-",
      "soul":"3000",
      "items":"Шипастый кнут, Человечность",
        "description": "Король Иеремия был изгнан в Нарисованный мир вместе с остальными людьми с уродствами, но неизвестно по какой причине. Можно предположить, что оказавшись внутри он прислуживал Присцилле (или пытался добиться ее расположения) — его труп сидит на скамье за ее спиной, стало быть, она его пропустила, но он не стал уходить. То что он использует пиромантию хаоса наводит на мысль о том, что он, возможно, когда-то был связан с ведьмой Изалита.",
        "image": "https://static.wikia.nocookie.net/darksouls/images/f/fe/Фантом_Иеримия.png/revision/latest?cb=20130602185224&path-prefix=ru"
    }
  },
  {
    "id": "25",
    "attributes": {
         "name": "Giant Blacksmith",
      "shortdescription": "кузнец-торговец",
      "location":"Анор Лондо",
      "health":"-",
      "soul":"3000",
      "items":"Великанский молот",
        "description": "В своём роде - уникальный кузнец, который может ковать оружие из душ. Также, при наличии кристального угля, он может ковать и улучшать кристальное оружие.",
        "image": "https://static.wikia.nocookie.net/darksouls/images/3/36/Кузнец_Великан.jpg/revision/latest?cb=20130327105504&path-prefix=ru"
    }
  },
  {
    "id": "26",
    "attributes": {
         "name": "Laurentius of the Great Swamp",
        "shortdescription": "персонаж-торговец",
      "location":"Глубины → Храм Огня → Чумной Город",
      "health":"-",
      "soul":"1000",
      "items":"-",
        "description": "Его можно найти в бочке в начале прохождения в Глубины, и освобожденный, Лаврентий уйдет в Храм Огня.",
        "image": "https://static.wikia.nocookie.net/darksouls/images/c/cb/Лаврентий_в_Храме_огня.jpg/revision/latest?cb=20130321062817&path-prefix=ru"
    }
  },
  {
    "id": "27",
    "attributes": {
         "name": "Forest Hunter Thief",
      "shortdescription": "",
      "location":"Сад Темных Корней",
      "health":"900",
      "soul":"2,000,  6,000 NG+",
      "items":"-",
        "description": "",
        "image": "https://static.wikia.nocookie.net/darksouls/images/1/1f/Лесной_охотник_вор.jpg/revision/latest?cb=20140215121614&path-prefix=ru"
    }
  },
  {
    "id": "28",
    "attributes": {
         "name": "Forest Hunter Cleric",
        "shortdescription": "",
      "location":"Сад Темных Корней",
      "health":"767",
      "soul":"2,000,  6,000 NG+",
      "items":"-",
        "description": "",
        "image": "https://static.wikia.nocookie.net/darksouls/images/9/9a/Лесной_охотник_клирик.jpg/revision/latest?cb=20140215114759&path-prefix=ru"
    }
  },
  {
    "id": "29",
    "attributes": {
         "name": " Forest Hunter Sorcerer",
       "shortdescription": "",
      "location":"Сад Темных Корней",
      "health":"719",
      "soul":"2,000,  6,000 NG+",
      "items":"-",
        "description": "",
        "image": "https://static.wikia.nocookie.net/darksouls/images/c/c7/Лесной_охотник_маг.jpg/revision/latest?cb=20140215120444&path-prefix=ru"
    }
  },
  {
    "id": "30",
    "attributes": {
         "name": "Forest Hunter Bandit",
        "shortdescription": "",
      "location":"Сад Темных Корней",
      "health":"900",
      "soul":"1,000, 3,000 NG+",
      "items":"-",
        "description": "",
        "image": "https://static.wikia.nocookie.net/darksouls/images/6/67/Лесной_охотник_бандит.jpg/revision/latest?cb=20140215115403&path-prefix=ru"
    }
  },
  {
    "id": "31",
    "attributes": {
         "name": "Forest Hunter Knight",
        "shortdescription": "",
      "location":"Сад Темных Корней",
      "health":"849",
      "soul":"3,000",
      "items":"-",
        "description": "",
        "image": "https://static.wikia.nocookie.net/darksouls/images/c/c4/Лесной_охотник_рыцарь.jpg/revision/latest?cb=20140215122605&path-prefix=ru"
    }
  },
  {
    "id": "32",
    "attributes": {
      "name": "Big Hat Logan",
      "shortdescription": "Логан был знаменитым волшебником родом из Винхеймcкой Школы Драконов. Его легко узнать по фирменной большой шляпе.",
      "location":"Крепость Сена → Храм Огня → Архивы Герцога",
      "health":"1000",
      "soul":"1,000",
      "items":"Большая шляпа Железный, кристальный посох, Дыхание белого дракона",
      "description": "Великий волшебник встречается несколько раз за игру и практически всегда требует нашей помощи.",
      "image": "https://avatars.mds.yandex.net/i?id=481c0975936d7fb1cb463d8587df3af5_l-5238322-images-thumbs&n=13"
         
    }
  },
  {
    "id": "33",
    "attributes": {
      "name": "Knight Lautrec of Carim",
      "shortdescription": "Рыцарь из Карима. ",
      "location":"Уезд Нежити → Храм Огня → Анор Лондо",
      "health":"1500",
      "soul":" 1,000, 4000 NG+",
      "items":"Кольцо защиты и поддержки Человечность x5 Душа Анастасии (убить в Анор Лондо) ",
      "description": "Рыцарь из Карима. Сам представляется как Лотрек Исповедник. Мотивы Лотрека не ясны, но известно, что он отправился в паломничество во имя любви к богине Фине. Неизвестно, кто запер его в камере Уезда Нежити, и тем более, за что он там оказался. Его обещание спустить шкуру с Лоскутика наводит на некоторые подозрения.",
      "image": "https://static.wikia.nocookie.net/darksouls/images/4/40/Лотрек_из_Карима.png/revision/latest?cb=20130122135904&path-prefix=ru"
    }
  },
  {
    "id": "34",
    "attributes": {
         "name": "Archer",
        "shortdescription": "персонаж и мини-босс",
      "location":"Сад Темных Корней",
      "health":"1200",
      "soul":"5,000",
      "items":"Черный лук, Шляпа Фарис, Двойная человечность",
        "description": "Является членом ковенанта Лесные Охотники и нападает на любого, кто вторгся без разрешения в Сад Темных Корней. С ней нельзя поговорить или как-либо взаимодействовать, кроме как напасть.",
        "image": "https://static.wikia.nocookie.net/darksouls/images/f/ff/Фарис.jpg/revision/latest?cb=20131130173834&path-prefix=ru"
    }
  },
  {
    "id": "35",
    "attributes": {
         "name": "Maneater Mildred",
        "shortdescription": "Бродячая женщина-каннибал",
      "location":"Чумной Город, Владение Квилег",
      "health":" 742, 1,424 [NG+], 1,780[NG+6]",
      "soul":"8,748, 8,748[NG+], 8,748[NG+6]",
      "items":"Мясницкий нож,Человечность х3",
        "description": "Бродячая женщина-каннибал, которая обитает в районе ядовитой топи Чумного Города, отчаянно пытается найти себе жертву среди путников, чудом забредающих в этот забытый уголок. Судя по тощему голодному животу людоедки, она не слишком удачлива в своей охоте, в отличие от своих коллег мясников, хотя благодаря этому двигается достаточно быстро и довольно опасна.",
        "image": "https://static.wikia.nocookie.net/darksouls/images/7/70/Людоедка_Милдред.png/revision/latest?cb=20180530095409&path-prefix=ru"
    }
  },
  {
    "id": "36",
    "attributes": {
         "name": "Undead Male Merchant",
         "shortdescription": "",
      "location":"",
      "health":"",
      "soul":"",
      "items":"",
        "description": "",
        "image": ""
    }
  },
  {
    "id": "37",
    "attributes": {
         "name": "Nico of Thorolund",
        "shortdescription": "",
      "location":"",
      "health":"",
      "soul":"",
      "items":"",
        "description": "",
        "image": ""
    }
  },
  {
    "id": "38",
    "attributes": {
         "name": "Giant Crow",
        "shortdescription": "",
      "location":"",
      "health":"",
      "soul":"",
      "items":"",
        "description": "",
        "image": ""
    }
  },
  {
    "id": "39",
    "attributes": {
         "name": " Oswald of Carim",
       "shortdescription": "",
      "location":"",
      "health":"",
      "soul":"",
      "items":"",
        "description": "",
        "image": ""
    }
  },
  {
    "id": "40",
    "attributes": {
         "name": "Oscar, Knight of Astora",
        "shortdescription": "",
      "location":"",
      "health":"",
      "soul":"",
      "items":"",
        "description": "",
        "image": ""
    }
  },
  {
    "id": "41",
    "attributes": {
         "name": "Paladin Leeroy",
        "shortdescription": "",
      "location":"",
      "health":"",
      "soul":"",
      "items":"",
        "description": "",
        "image": ""
    }
  },
  {
    "id": "42",
    "attributes": {
         "name": "Petrus of Thorolund",
         "shortdescription": "",
      "location":"",
      "health":"",
      "soul":"",
      "items":"",
        "description": "",
        "image": ""
    }
  },
  {
    "id": "43",
    "attributes": {
         "name": "The Fair Lady",
         "shortdescription": "",
      "location":"",
      "health":"",
      "soul":"",
      "items":"",
        "description": "",
        "image": ""
    }
  },
  {
    "id": "44",
    "attributes": {
         "name": "Crossbreed Priscilla",
        "shortdescription": "",
      "location":"",
      "health":"",
      "soul":"",
      "items":"",
        "description": "",
        "image": ""
    }
  },
  {
    "id": "45",
    "attributes": {
         "name": " Reah of Thorolund",
        "shortdescription": "",
      "location":"",
      "health":"",
      "soul":"",
      "items":"",
        "description": "",
        "image": ""
    }
  },
  {
    "id": "46",
    "attributes": {
         "name": "Rickert of Vinheim",
        "shortdescription": "",
      "location":"",
      "health":"",
      "soul":"",
      "items":"",
        "description": "",
        "image": ""
    }
  },
  {
    "id": "47",
    "attributes": {
         "name": "Darkmoon Knightess",
        "shortdescription": "",
      "location":"",
      "health":"",
      "soul":"",
      "items":"",
        "description": "",
        "image": ""
    }
  },
  {
    "id": "48",
    "attributes": {
         "name": "Lord's Blade Ciaran",
        "shortdescription": "",
      "location":"",
      "health":"",
      "soul":"",
      "items":"",
        "description": "",
        "image": ""
    }
  },
  {
    "id": "49",
    "attributes": {
         "name": "Sieglinde of Catarina",
        "shortdescription": "",
      "location":"",
      "health":"",
      "soul":"",
      "items":"",
        "description": "",
        "image": ""
    }
  },
  {
    "id": "50",
    "attributes": {
         "name": "Siegmeyer of Catarina",
         "shortdescription": "",
      "location":"",
      "health":"",
      "soul":"",
      "items":"",
        "description": "",
        "image": ""
    }
  },
  {
    "id": "51",
    "attributes": {
         "name": "Great Grey Wolf Sif",
        "shortdescription": "",
      "location":"",
      "health":"",
      "soul":"",
      "items":"",
        "description": "",
        "image": ""
    }
  },
  {
    "id": "52",
    "attributes": {
         "name": " Snuggly the Crow",
       "shortdescription": "",
      "location":"",
      "health":"",
      "soul":"",
      "items":"",
        "description": "",
        "image": ""
    }
  },
  {
    "id": "53",
    "attributes": {
         "name": "Solaire of Astora",
        "shortdescription": "",
      "location":"",
      "health":"",
      "soul":"",
      "items":"",
        "description": "",
        "image": ""
    }
  },
  {
    "id": "54",
    "attributes": {
         "name": "Black Iron Tarkus",
        "shortdescription": "",
      "location":"",
      "health":"",
      "soul":"",
      "items":"",
        "description": "",
        "image": ""
    }
  },
  {
    "id": "55",
    "attributes": {
         "name": "Shiva's Bodyguard",
         "shortdescription": "",
      "location":"",
      "health":"",
      "soul":"",
      "items":"",
        "description": "",
        "image": ""
    }
  },
  {
    "id": "56",
    "attributes": {
         "name": " Undead Female Merchant",
         "shortdescription": "",
      "location":"",
      "health":"",
      "soul":"",
      "items":"",
        "description": "",
        "image": ""
    }
  },
  {
    "id": "57",
    "attributes": {
         "name": "Crestfallen Warrior",
        "shortdescription": "",
      "location":"",
      "health":"",
      "soul":"",
      "items":"",
        "description": "",
        "image": ""
    }
  },
  {
    "id": "58",
    "attributes": {
         "name": "Crestfallen Merchant",
         "shortdescription": "",
      "location":"",
      "health":"",
      "soul":"",
      "items":"",
        "description": "",
        "image": ""
    }
  },
  {
    "id": "59",
    "attributes": {
         "name": " Kingseeker Frampt",
        "shortdescription": "",
      "location":"",
      "health":"",
      "soul":"",
      "items":"",
        "description": "",
        "image": ""
    }
  },
  {
    "id": "60",
    "attributes": {
         "name": "Havel the Rock",
        "shortdescription": "",
      "location":"",
      "health":"",
      "soul":"",
      "items":"",
        "description": "",
        "image": ""
    }
  },
  {
    "id": "61",
    "attributes": {
         "name": " Marvellous Chester",
        "shortdescription": "",
      "location":"",
      "health":"",
      "soul":"",
      "items":"",
        "description": "",
        "image": ""
    }
  },
  {
    "id": "62",
    "attributes": {
         "name": "Shiva of the East",
         "shortdescription": "",
      "location":"",
      "health":"",
      "soul":"",
      "items":"",
        "description": "",
        "image": ""
    }
  },
  {
    "id": "63",
    "attributes": {
         "name": "Elizabeth",
        "shortdescription": "",
      "location":"",
      "health":"",
      "soul":"",
      "items":"",
        "description": "",
        "image": ""
    }
  },
  {
    "id": "64",
    "attributes": {
         "name": "Eingyi",
        "shortdescription": "",
      "location":"",
      "health":"",
      "soul":"",
      "items":"",
        "description": "",
        "image": ""
    }
  },
  {
    "id": "65",
    "attributes": {
         "name": "",
        "shortdescription": "",
      "location":"",
      "health":"",
      "soul":"",
      "items":"",
        "description": "",
        "image": ""
    }
  },
  {
    "id": "66",
    "attributes": {
         "name": "",
         "shortdescription": "",
      "location":"",
      "health":"",
      "soul":"",
      "items":"",
        "description": "",
        "image": ""
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
