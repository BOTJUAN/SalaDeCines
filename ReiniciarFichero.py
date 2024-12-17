import json
peliculas = [
    {
        "ruta": "Carteleras\\DB.jpg",
        "nombre": "Dragon Ball Super: Broly",
        "sinopsis": "Goku y Vegeta encuentran a Broly, un guerrero Saiyajin. Pero, \u00bfc\u00f3mo sobrevivi\u00f3 a la destrucci\u00f3n de su planeta  y d\u00f3nde estuvo todo ese tiempo? La situaci\u00f3n empeora todav\u00eda m\u00e1s cuando Freezer vuelve al mundo de los vivos desde el infierno.",
        "asientos": [
            [
            [{"text": "L", "fg_color": "#1f6aa5"}, {"text": "L", "fg_color": "#1f6aa5"}, {"text": "L", "fg_color": "#1f6aa5"}, {"text": "L", "fg_color": "#1f6aa5"}, {"text": "L", "fg_color": "#1f6aa5"}, {"text": "L", "fg_color": "#1f6aa5"}, {"text": "L", "fg_color": "#1f6aa5"}],
            [{"text": "L", "fg_color": "#1f6aa5"}, {"text": "L", "fg_color": "#1f6aa5"}, {"text": "L", "fg_color": "#1f6aa5"}, {"text": "L", "fg_color": "#1f6aa5"}, {"text": "L", "fg_color": "#1f6aa5"}, {"text": "L", "fg_color": "#1f6aa5"}, {"text": "L", "fg_color": "#1f6aa5"}],
            [{"text": "L", "fg_color": "#1f6aa5"}, {"text": "L", "fg_color": "#1f6aa5"}, {"text": "L", "fg_color": "#1f6aa5"}, {"text": "L", "fg_color": "#1f6aa5"}, {"text": "L", "fg_color": "#1f6aa5"}, {"text": "L", "fg_color": "#1f6aa5"}, {"text": "L", "fg_color": "#1f6aa5"}],
            [{"text": "L", "fg_color": "#1f6aa5"}, {"text": "L", "fg_color": "#1f6aa5"}, {"text": "L", "fg_color": "#1f6aa5"}, {"text": "L", "fg_color": "#1f6aa5"}, {"text": "L", "fg_color": "#1f6aa5"}, {"text": "L", "fg_color": "#1f6aa5"}, {"text": "L", "fg_color": "#1f6aa5"}],
            [{"text": "L", "fg_color": "#1f6aa5"}, {"text": "L", "fg_color": "#1f6aa5"}, {"text": "L", "fg_color": "#1f6aa5"}, {"text": "L", "fg_color": "#1f6aa5"}, {"text": "L", "fg_color": "#1f6aa5"}, {"text": "L", "fg_color": "#1f6aa5"}, {"text": "L", "fg_color": "#1f6aa5"}],
            [{"text": "L", "fg_color": "#1f6aa5"}, {"text": "L", "fg_color": "#1f6aa5"}, {"text": "L", "fg_color": "#1f6aa5"}, {"text": "L", "fg_color": "#1f6aa5"}, {"text": "L", "fg_color": "#1f6aa5"}, {"text": "L", "fg_color": "#1f6aa5"}, {"text": "L", "fg_color": "#1f6aa5"}],
            [{"text": "L", "fg_color": "#1f6aa5"}, {"text": "L", "fg_color": "#1f6aa5"}, {"text": "L", "fg_color": "#1f6aa5"}, {"text": "L", "fg_color": "#1f6aa5"}, {"text": "L", "fg_color": "#1f6aa5"}, {"text": "L", "fg_color": "#1f6aa5"}, {"text": "L", "fg_color": "#1f6aa5"}]
            ]
        ]
    },
    {
        "ruta": "Carteleras\\batman.jpg",
        "nombre": "The Batman",
        "sinopsis": "En su segundo a\u00f1o luchando contra el crimen, Batman explora la corrupci\u00f3n existente en la ciudad de Gotham y el v\u00ednculo de esta con su propia familia. Adem\u00e1s, entrar\u00e1 en conflicto con un asesino en serie conocido como el Acertijo.",
        "asientos": [
            [
                [{"text": "L", "fg_color": "#1f6aa5"}, {"text": "L", "fg_color": "#1f6aa5"}, {"text": "L", "fg_color": "#1f6aa5"}, {"text": "L", "fg_color": "#1f6aa5"}, {"text": "L", "fg_color": "#1f6aa5"}, {"text": "L", "fg_color": "#1f6aa5"}, {"text": "L", "fg_color": "#1f6aa5"}],
                [{"text": "L", "fg_color": "#1f6aa5"}, {"text": "L", "fg_color": "#1f6aa5"}, {"text": "L", "fg_color": "#1f6aa5"}, {"text": "L", "fg_color": "#1f6aa5"}, {"text": "L", "fg_color": "#1f6aa5"}, {"text": "L", "fg_color": "#1f6aa5"}, {"text": "L", "fg_color": "#1f6aa5"}],
                [{"text": "L", "fg_color": "#1f6aa5"}, {"text": "L", "fg_color": "#1f6aa5"}, {"text": "L", "fg_color": "#1f6aa5"}, {"text": "L", "fg_color": "#1f6aa5"}, {"text": "L", "fg_color": "#1f6aa5"}, {"text": "L", "fg_color": "#1f6aa5"}, {"text": "L", "fg_color": "#1f6aa5"}],
                [{"text": "L", "fg_color": "#1f6aa5"}, {"text": "L", "fg_color": "#1f6aa5"}, {"text": "L", "fg_color": "#1f6aa5"}, {"text": "L", "fg_color": "#1f6aa5"}, {"text": "L", "fg_color": "#1f6aa5"}, {"text": "L", "fg_color": "#1f6aa5"}, {"text": "L", "fg_color": "#1f6aa5"}],
                [{"text": "L", "fg_color": "#1f6aa5"}, {"text": "L", "fg_color": "#1f6aa5"}, {"text": "L", "fg_color": "#1f6aa5"}, {"text": "L", "fg_color": "#1f6aa5"}, {"text": "L", "fg_color": "#1f6aa5"}, {"text": "L", "fg_color": "#1f6aa5"}, {"text": "L", "fg_color": "#1f6aa5"}],
                [{"text": "L", "fg_color": "#1f6aa5"}, {"text": "L", "fg_color": "#1f6aa5"}, {"text": "L", "fg_color": "#1f6aa5"}, {"text": "L", "fg_color": "#1f6aa5"}, {"text": "L", "fg_color": "#1f6aa5"}, {"text": "L", "fg_color": "#1f6aa5"}, {"text": "L", "fg_color": "#1f6aa5"}],
                [{"text": "L", "fg_color": "#1f6aa5"}, {"text": "L", "fg_color": "#1f6aa5"}, {"text": "L", "fg_color": "#1f6aa5"}, {"text": "L", "fg_color": "#1f6aa5"}, {"text": "L", "fg_color": "#1f6aa5"}, {"text": "L", "fg_color": "#1f6aa5"}, {"text": "L", "fg_color": "#1f6aa5"}]
            ],
            [
                [{"text": "L", "fg_color": "#1f6aa5"}, {"text": "L", "fg_color": "#1f6aa5"}, {"text": "L", "fg_color": "#1f6aa5"}, {"text": "L", "fg_color": "#1f6aa5"}, {"text": "L", "fg_color": "#1f6aa5"}, {"text": "L", "fg_color": "#1f6aa5"}, {"text": "L", "fg_color": "#1f6aa5"}],
                [{"text": "L", "fg_color": "#1f6aa5"}, {"text": "L", "fg_color": "#1f6aa5"}, {"text": "L", "fg_color": "#1f6aa5"}, {"text": "L", "fg_color": "#1f6aa5"}, {"text": "L", "fg_color": "#1f6aa5"}, {"text": "L", "fg_color": "#1f6aa5"}, {"text": "L", "fg_color": "#1f6aa5"}],
                [{"text": "L", "fg_color": "#1f6aa5"}, {"text": "L", "fg_color": "#1f6aa5"}, {"text": "L", "fg_color": "#1f6aa5"}, {"text": "L", "fg_color": "#1f6aa5"}, {"text": "L", "fg_color": "#1f6aa5"}, {"text": "L", "fg_color": "#1f6aa5"}, {"text": "L", "fg_color": "#1f6aa5"}],
                [{"text": "L", "fg_color": "#1f6aa5"}, {"text": "L", "fg_color": "#1f6aa5"}, {"text": "L", "fg_color": "#1f6aa5"}, {"text": "L", "fg_color": "#1f6aa5"}, {"text": "L", "fg_color": "#1f6aa5"}, {"text": "L", "fg_color": "#1f6aa5"}, {"text": "L", "fg_color": "#1f6aa5"}],
                [{"text": "L", "fg_color": "#1f6aa5"}, {"text": "L", "fg_color": "#1f6aa5"}, {"text": "L", "fg_color": "#1f6aa5"}, {"text": "L", "fg_color": "#1f6aa5"}, {"text": "L", "fg_color": "#1f6aa5"}, {"text": "L", "fg_color": "#1f6aa5"}, {"text": "L", "fg_color": "#1f6aa5"}],
                [{"text": "L", "fg_color": "#1f6aa5"}, {"text": "L", "fg_color": "#1f6aa5"}, {"text": "L", "fg_color": "#1f6aa5"}, {"text": "L", "fg_color": "#1f6aa5"}, {"text": "L", "fg_color": "#1f6aa5"}, {"text": "L", "fg_color": "#1f6aa5"}, {"text": "L", "fg_color": "#1f6aa5"}],
                [{"text": "L", "fg_color": "#1f6aa5"}, {"text": "L", "fg_color": "#1f6aa5"}, {"text": "L", "fg_color": "#1f6aa5"}, {"text": "L", "fg_color": "#1f6aa5"}, {"text": "L", "fg_color": "#1f6aa5"}, {"text": "L", "fg_color": "#1f6aa5"}, {"text": "L", "fg_color": "#1f6aa5"}]
            ]
        ]
    },
    {
        "ruta": "Carteleras\\fury.jpg",
        "nombre": "Fury",
        "sinopsis": "Durante la Segunda Guerra Mundial, un aguerrido sargento del ej\u00e9rcito encabeza el equipo de un tanque Sherman en una misi\u00f3n mortal detr\u00e1s de l\u00edneas enemigas para golpear el coraz\u00f3n de la Alemania nazi.",
        "asientos": [
            [
                [{"text": "L", "fg_color": "#1f6aa5"}, {"text": "L", "fg_color": "#1f6aa5"}, {"text": "L", "fg_color": "#1f6aa5"}, {"text": "L", "fg_color": "#1f6aa5"}, {"text": "L", "fg_color": "#1f6aa5"}, {"text": "L", "fg_color": "#1f6aa5"}, {"text": "L", "fg_color": "#1f6aa5"}],
                [{"text": "L", "fg_color": "#1f6aa5"}, {"text": "L", "fg_color": "#1f6aa5"}, {"text": "L", "fg_color": "#1f6aa5"}, {"text": "L", "fg_color": "#1f6aa5"}, {"text": "L", "fg_color": "#1f6aa5"}, {"text": "L", "fg_color": "#1f6aa5"}, {"text": "L", "fg_color": "#1f6aa5"}],
                [{"text": "L", "fg_color": "#1f6aa5"}, {"text": "L", "fg_color": "#1f6aa5"}, {"text": "L", "fg_color": "#1f6aa5"}, {"text": "L", "fg_color": "#1f6aa5"}, {"text": "L", "fg_color": "#1f6aa5"}, {"text": "L", "fg_color": "#1f6aa5"}, {"text": "L", "fg_color": "#1f6aa5"}],
                [{"text": "L", "fg_color": "#1f6aa5"}, {"text": "L", "fg_color": "#1f6aa5"}, {"text": "L", "fg_color": "#1f6aa5"}, {"text": "L", "fg_color": "#1f6aa5"}, {"text": "L", "fg_color": "#1f6aa5"}, {"text": "L", "fg_color": "#1f6aa5"}, {"text": "L", "fg_color": "#1f6aa5"}],
                [{"text": "L", "fg_color": "#1f6aa5"}, {"text": "L", "fg_color": "#1f6aa5"}, {"text": "L", "fg_color": "#1f6aa5"}, {"text": "L", "fg_color": "#1f6aa5"}, {"text": "L", "fg_color": "#1f6aa5"}, {"text": "L", "fg_color": "#1f6aa5"}, {"text": "L", "fg_color": "#1f6aa5"}],
                [{"text": "L", "fg_color": "#1f6aa5"}, {"text": "L", "fg_color": "#1f6aa5"}, {"text": "L", "fg_color": "#1f6aa5"}, {"text": "L", "fg_color": "#1f6aa5"}, {"text": "L", "fg_color": "#1f6aa5"}, {"text": "L", "fg_color": "#1f6aa5"}, {"text": "L", "fg_color": "#1f6aa5"}],
                [{"text": "L", "fg_color": "#1f6aa5"}, {"text": "L", "fg_color": "#1f6aa5"}, {"text": "L", "fg_color": "#1f6aa5"}, {"text": "L", "fg_color": "#1f6aa5"}, {"text": "L", "fg_color": "#1f6aa5"}, {"text": "L", "fg_color": "#1f6aa5"}, {"text": "L", "fg_color": "#1f6aa5"}]
            ],
            [
                [{"text": "L", "fg_color": "#1f6aa5"}, {"text": "L", "fg_color": "#1f6aa5"}, {"text": "L", "fg_color": "#1f6aa5"}, {"text": "L", "fg_color": "#1f6aa5"}, {"text": "L", "fg_color": "#1f6aa5"}, {"text": "L", "fg_color": "#1f6aa5"}, {"text": "L", "fg_color": "#1f6aa5"}],
                [{"text": "L", "fg_color": "#1f6aa5"}, {"text": "L", "fg_color": "#1f6aa5"}, {"text": "L", "fg_color": "#1f6aa5"}, {"text": "L", "fg_color": "#1f6aa5"}, {"text": "L", "fg_color": "#1f6aa5"}, {"text": "L", "fg_color": "#1f6aa5"}, {"text": "L", "fg_color": "#1f6aa5"}],
                [{"text": "L", "fg_color": "#1f6aa5"}, {"text": "L", "fg_color": "#1f6aa5"}, {"text": "L", "fg_color": "#1f6aa5"}, {"text": "L", "fg_color": "#1f6aa5"}, {"text": "L", "fg_color": "#1f6aa5"}, {"text": "L", "fg_color": "#1f6aa5"}, {"text": "L", "fg_color": "#1f6aa5"}],
                [{"text": "L", "fg_color": "#1f6aa5"}, {"text": "L", "fg_color": "#1f6aa5"}, {"text": "L", "fg_color": "#1f6aa5"}, {"text": "L", "fg_color": "#1f6aa5"}, {"text": "L", "fg_color": "#1f6aa5"}, {"text": "L", "fg_color": "#1f6aa5"}, {"text": "L", "fg_color": "#1f6aa5"}],
                [{"text": "L", "fg_color": "#1f6aa5"}, {"text": "L", "fg_color": "#1f6aa5"}, {"text": "L", "fg_color": "#1f6aa5"}, {"text": "L", "fg_color": "#1f6aa5"}, {"text": "L", "fg_color": "#1f6aa5"}, {"text": "L", "fg_color": "#1f6aa5"}, {"text": "L", "fg_color": "#1f6aa5"}],
                [{"text": "L", "fg_color": "#1f6aa5"}, {"text": "L", "fg_color": "#1f6aa5"}, {"text": "L", "fg_color": "#1f6aa5"}, {"text": "L", "fg_color": "#1f6aa5"}, {"text": "L", "fg_color": "#1f6aa5"}, {"text": "L", "fg_color": "#1f6aa5"}, {"text": "L", "fg_color": "#1f6aa5"}],
                [{"text": "L", "fg_color": "#1f6aa5"}, {"text": "L", "fg_color": "#1f6aa5"}, {"text": "L", "fg_color": "#1f6aa5"}, {"text": "L", "fg_color": "#1f6aa5"}, {"text": "L", "fg_color": "#1f6aa5"}, {"text": "L", "fg_color": "#1f6aa5"}, {"text": "L", "fg_color": "#1f6aa5"}]
            ]
        ]
    },
    {
        "ruta": "Carteleras\\joker.jpg",
        "nombre": "Joker",
        "sinopsis": "Arthur Fleck adora hacer re\u00edr a la gente, pero su carrera como comediante es un fracaso. El repudio social, la marginaci\u00f3n y una serie de tr\u00e1gicos acontecimientos lo conducen por el sendero de la locura y, finalmente, cae en el mundo del crimen.",
        "asientos": [
            [
                [{"text": "L", "fg_color": "#1f6aa5"}, {"text": "L", "fg_color": "#1f6aa5"}, {"text": "L", "fg_color": "#1f6aa5"}, {"text": "L", "fg_color": "#1f6aa5"}, {"text": "L", "fg_color": "#1f6aa5"}, {"text": "L", "fg_color": "#1f6aa5"}, {"text": "L", "fg_color": "#1f6aa5"}],
                [{"text": "L", "fg_color": "#1f6aa5"}, {"text": "L", "fg_color": "#1f6aa5"}, {"text": "L", "fg_color": "#1f6aa5"}, {"text": "L", "fg_color": "#1f6aa5"}, {"text": "L", "fg_color": "#1f6aa5"}, {"text": "L", "fg_color": "#1f6aa5"}, {"text": "L", "fg_color": "#1f6aa5"}],
                [{"text": "L", "fg_color": "#1f6aa5"}, {"text": "L", "fg_color": "#1f6aa5"}, {"text": "L", "fg_color": "#1f6aa5"}, {"text": "L", "fg_color": "#1f6aa5"}, {"text": "L", "fg_color": "#1f6aa5"}, {"text": "L", "fg_color": "#1f6aa5"}, {"text": "L", "fg_color": "#1f6aa5"}],
                [{"text": "L", "fg_color": "#1f6aa5"}, {"text": "L", "fg_color": "#1f6aa5"}, {"text": "L", "fg_color": "#1f6aa5"}, {"text": "L", "fg_color": "#1f6aa5"}, {"text": "L", "fg_color": "#1f6aa5"}, {"text": "L", "fg_color": "#1f6aa5"}, {"text": "L", "fg_color": "#1f6aa5"}],
                [{"text": "L", "fg_color": "#1f6aa5"}, {"text": "L", "fg_color": "#1f6aa5"}, {"text": "L", "fg_color": "#1f6aa5"}, {"text": "L", "fg_color": "#1f6aa5"}, {"text": "L", "fg_color": "#1f6aa5"}, {"text": "L", "fg_color": "#1f6aa5"}, {"text": "L", "fg_color": "#1f6aa5"}],
                [{"text": "L", "fg_color": "#1f6aa5"}, {"text": "L", "fg_color": "#1f6aa5"}, {"text": "L", "fg_color": "#1f6aa5"}, {"text": "L", "fg_color": "#1f6aa5"}, {"text": "L", "fg_color": "#1f6aa5"}, {"text": "L", "fg_color": "#1f6aa5"}, {"text": "L", "fg_color": "#1f6aa5"}],
                [{"text": "L", "fg_color": "#1f6aa5"}, {"text": "L", "fg_color": "#1f6aa5"}, {"text": "L", "fg_color": "#1f6aa5"}, {"text": "L", "fg_color": "#1f6aa5"}, {"text": "L", "fg_color": "#1f6aa5"}, {"text": "L", "fg_color": "#1f6aa5"}, {"text": "L", "fg_color": "#1f6aa5"}]
            ]
        ]
    },
    {
        "ruta": "Carteleras\\creed.jpg",
        "nombre": "Creed III",
        "sinopsis": "Adonis Creed, a\u00fan dominando el mundo del boxeo, prospera en su carrera y en su vida familiar, pero un amigo de la infancia y antiguo prodigio del boxeo reaparece tras salir de la c\u00e1rcel y est\u00e1 ansioso por demostrar que merece otra oportunidad.",
        "asientos": [
            [
                [{"text": "L", "fg_color": "#1f6aa5"}, {"text": "L", "fg_color": "#1f6aa5"}, {"text": "L", "fg_color": "#1f6aa5"}, {"text": "L", "fg_color": "#1f6aa5"}, {"text": "L", "fg_color": "#1f6aa5"}, {"text": "L", "fg_color": "#1f6aa5"}, {"text": "L", "fg_color": "#1f6aa5"}],
                [{"text": "L", "fg_color": "#1f6aa5"}, {"text": "L", "fg_color": "#1f6aa5"}, {"text": "L", "fg_color": "#1f6aa5"}, {"text": "L", "fg_color": "#1f6aa5"}, {"text": "L", "fg_color": "#1f6aa5"}, {"text": "L", "fg_color": "#1f6aa5"}, {"text": "L", "fg_color": "#1f6aa5"}],
                [{"text": "L", "fg_color": "#1f6aa5"}, {"text": "L", "fg_color": "#1f6aa5"}, {"text": "L", "fg_color": "#1f6aa5"}, {"text": "L", "fg_color": "#1f6aa5"}, {"text": "L", "fg_color": "#1f6aa5"}, {"text": "L", "fg_color": "#1f6aa5"}, {"text": "L", "fg_color": "#1f6aa5"}],
                [{"text": "L", "fg_color": "#1f6aa5"}, {"text": "L", "fg_color": "#1f6aa5"}, {"text": "L", "fg_color": "#1f6aa5"}, {"text": "L", "fg_color": "#1f6aa5"}, {"text": "L", "fg_color": "#1f6aa5"}, {"text": "L", "fg_color": "#1f6aa5"}, {"text": "L", "fg_color": "#1f6aa5"}],
                [{"text": "L", "fg_color": "#1f6aa5"}, {"text": "L", "fg_color": "#1f6aa5"}, {"text": "L", "fg_color": "#1f6aa5"}, {"text": "L", "fg_color": "#1f6aa5"}, {"text": "L", "fg_color": "#1f6aa5"}, {"text": "L", "fg_color": "#1f6aa5"}, {"text": "L", "fg_color": "#1f6aa5"}],
                [{"text": "L", "fg_color": "#1f6aa5"}, {"text": "L", "fg_color": "#1f6aa5"}, {"text": "L", "fg_color": "#1f6aa5"}, {"text": "L", "fg_color": "#1f6aa5"}, {"text": "L", "fg_color": "#1f6aa5"}, {"text": "L", "fg_color": "#1f6aa5"}, {"text": "L", "fg_color": "#1f6aa5"}],
                [{"text": "L", "fg_color": "#1f6aa5"}, {"text": "L", "fg_color": "#1f6aa5"}, {"text": "L", "fg_color": "#1f6aa5"}, {"text": "L", "fg_color": "#1f6aa5"}, {"text": "L", "fg_color": "#1f6aa5"}, {"text": "L", "fg_color": "#1f6aa5"}, {"text": "L", "fg_color": "#1f6aa5"}]
            ]
        ]
    },
    {
        "ruta": "Carteleras\\shrek.jpg",
        "nombre": "Shrek",
        "sinopsis": "Un ogro llamado Shrek vive en su pantano, pero su preciada soledad se ve s\u00fabitamente interrumpida por la invasi\u00f3n de los ruidosos personajes de los cuentos de hadas. Todos fueron expulsados de sus reinos por el malvado Lord Farquaad. Decidido a salvar su hogar, Shrek hace un trato con Farquaad y se prepara para rescatar a la princesa Fiona, quien ser\u00e1 la esposa de Farquaad.",
        "asientos": [
            [
                [{"text": "L", "fg_color": "#1f6aa5"}, {"text": "L", "fg_color": "#1f6aa5"}, {"text": "L", "fg_color": "#1f6aa5"}, {"text": "L", "fg_color": "#1f6aa5"}, {"text": "L", "fg_color": "#1f6aa5"}, {"text": "L", "fg_color": "#1f6aa5"}, {"text": "L", "fg_color": "#1f6aa5"}],
                [{"text": "L", "fg_color": "#1f6aa5"}, {"text": "L", "fg_color": "#1f6aa5"}, {"text": "L", "fg_color": "#1f6aa5"}, {"text": "L", "fg_color": "#1f6aa5"}, {"text": "L", "fg_color": "#1f6aa5"}, {"text": "L", "fg_color": "#1f6aa5"}, {"text": "L", "fg_color": "#1f6aa5"}],
                [{"text": "L", "fg_color": "#1f6aa5"}, {"text": "L", "fg_color": "#1f6aa5"}, {"text": "L", "fg_color": "#1f6aa5"}, {"text": "L", "fg_color": "#1f6aa5"}, {"text": "L", "fg_color": "#1f6aa5"}, {"text": "L", "fg_color": "#1f6aa5"}, {"text": "L", "fg_color": "#1f6aa5"}],
                [{"text": "L", "fg_color": "#1f6aa5"}, {"text": "L", "fg_color": "#1f6aa5"}, {"text": "L", "fg_color": "#1f6aa5"}, {"text": "L", "fg_color": "#1f6aa5"}, {"text": "L", "fg_color": "#1f6aa5"}, {"text": "L", "fg_color": "#1f6aa5"}, {"text": "L", "fg_color": "#1f6aa5"}],
                [{"text": "L", "fg_color": "#1f6aa5"}, {"text": "L", "fg_color": "#1f6aa5"}, {"text": "L", "fg_color": "#1f6aa5"}, {"text": "L", "fg_color": "#1f6aa5"}, {"text": "L", "fg_color": "#1f6aa5"}, {"text": "L", "fg_color": "#1f6aa5"}, {"text": "L", "fg_color": "#1f6aa5"}],
                [{"text": "L", "fg_color": "#1f6aa5"}, {"text": "L", "fg_color": "#1f6aa5"}, {"text": "L", "fg_color": "#1f6aa5"}, {"text": "L", "fg_color": "#1f6aa5"}, {"text": "L", "fg_color": "#1f6aa5"}, {"text": "L", "fg_color": "#1f6aa5"}, {"text": "L", "fg_color": "#1f6aa5"}],
                [{"text": "L", "fg_color": "#1f6aa5"}, {"text": "L", "fg_color": "#1f6aa5"}, {"text": "L", "fg_color": "#1f6aa5"}, {"text": "L", "fg_color": "#1f6aa5"}, {"text": "L", "fg_color": "#1f6aa5"}, {"text": "L", "fg_color": "#1f6aa5"}, {"text": "L", "fg_color": "#1f6aa5"}]
            ]
        ]
    },
    {
        "ruta": "Carteleras\\spiderman.jpg",
        "nombre": "El Hombre Ara\u00f1a 3",
        "sinopsis": "Peter Parker sufre una terrible transformaci\u00f3n cuando su traje de Hombre Ara\u00f1a se vuelve negro y libera una personalidad oscura y vengativa.",
        "asientos": [
            [
                [{"text": "L", "fg_color": "#1f6aa5"}, {"text": "L", "fg_color": "#1f6aa5"}, {"text": "L", "fg_color": "#1f6aa5"}, {"text": "L", "fg_color": "#1f6aa5"}, {"text": "L", "fg_color": "#1f6aa5"}, {"text": "L", "fg_color": "#1f6aa5"}, {"text": "L", "fg_color": "#1f6aa5"}],
                [{"text": "L", "fg_color": "#1f6aa5"}, {"text": "L", "fg_color": "#1f6aa5"}, {"text": "L", "fg_color": "#1f6aa5"}, {"text": "L", "fg_color": "#1f6aa5"}, {"text": "L", "fg_color": "#1f6aa5"}, {"text": "L", "fg_color": "#1f6aa5"}, {"text": "L", "fg_color": "#1f6aa5"}],
                [{"text": "L", "fg_color": "#1f6aa5"}, {"text": "L", "fg_color": "#1f6aa5"}, {"text": "L", "fg_color": "#1f6aa5"}, {"text": "L", "fg_color": "#1f6aa5"}, {"text": "L", "fg_color": "#1f6aa5"}, {"text": "L", "fg_color": "#1f6aa5"}, {"text": "L", "fg_color": "#1f6aa5"}],
                [{"text": "L", "fg_color": "#1f6aa5"}, {"text": "L", "fg_color": "#1f6aa5"}, {"text": "L", "fg_color": "#1f6aa5"}, {"text": "L", "fg_color": "#1f6aa5"}, {"text": "L", "fg_color": "#1f6aa5"}, {"text": "L", "fg_color": "#1f6aa5"}, {"text": "L", "fg_color": "#1f6aa5"}],
                [{"text": "L", "fg_color": "#1f6aa5"}, {"text": "L", "fg_color": "#1f6aa5"}, {"text": "L", "fg_color": "#1f6aa5"}, {"text": "L", "fg_color": "#1f6aa5"}, {"text": "L", "fg_color": "#1f6aa5"}, {"text": "L", "fg_color": "#1f6aa5"}, {"text": "L", "fg_color": "#1f6aa5"}],
                [{"text": "L", "fg_color": "#1f6aa5"}, {"text": "L", "fg_color": "#1f6aa5"}, {"text": "L", "fg_color": "#1f6aa5"}, {"text": "L", "fg_color": "#1f6aa5"}, {"text": "L", "fg_color": "#1f6aa5"}, {"text": "L", "fg_color": "#1f6aa5"}, {"text": "L", "fg_color": "#1f6aa5"}],
                [{"text": "L", "fg_color": "#1f6aa5"}, {"text": "L", "fg_color": "#1f6aa5"}, {"text": "L", "fg_color": "#1f6aa5"}, {"text": "L", "fg_color": "#1f6aa5"}, {"text": "L", "fg_color": "#1f6aa5"}, {"text": "L", "fg_color": "#1f6aa5"}, {"text": "L", "fg_color": "#1f6aa5"}]
            ]
        ]
    },
    {
        "ruta": "Carteleras\\300.jpg",
        "nombre": "300",
        "sinopsis": "En el a\u00f1o 480 antes de Cristo, existe un estado de guerra entre Persia, dirigida por el rey Jerjes, y Grecia. En la batalla de la Term\u00f3pilas, Leonidas, rey de la ciudad griega de Esparta, encabeza a sus 300 bravos soldados en contra del numeroso ej\u00e9rcito persa. A pesar de que la muerte aguarda a los espartanos, su sacrificio inspira a toda Grecia para unirla en contra de su enemigo com\u00fan.",
        "asientos": [
            [
                [{"text": "L", "fg_color": "#1f6aa5"}, {"text": "L", "fg_color": "#1f6aa5"}, {"text": "L", "fg_color": "#1f6aa5"}, {"text": "L", "fg_color": "#1f6aa5"}, {"text": "L", "fg_color": "#1f6aa5"}, {"text": "L", "fg_color": "#1f6aa5"}, {"text": "L", "fg_color": "#1f6aa5"}],
                [{"text": "L", "fg_color": "#1f6aa5"}, {"text": "L", "fg_color": "#1f6aa5"}, {"text": "L", "fg_color": "#1f6aa5"}, {"text": "L", "fg_color": "#1f6aa5"}, {"text": "L", "fg_color": "#1f6aa5"}, {"text": "L", "fg_color": "#1f6aa5"}, {"text": "L", "fg_color": "#1f6aa5"}],
                [{"text": "L", "fg_color": "#1f6aa5"}, {"text": "L", "fg_color": "#1f6aa5"}, {"text": "L", "fg_color": "#1f6aa5"}, {"text": "L", "fg_color": "#1f6aa5"}, {"text": "L", "fg_color": "#1f6aa5"}, {"text": "L", "fg_color": "#1f6aa5"}, {"text": "L", "fg_color": "#1f6aa5"}],
                [{"text": "L", "fg_color": "#1f6aa5"}, {"text": "L", "fg_color": "#1f6aa5"}, {"text": "L", "fg_color": "#1f6aa5"}, {"text": "L", "fg_color": "#1f6aa5"}, {"text": "L", "fg_color": "#1f6aa5"}, {"text": "L", "fg_color": "#1f6aa5"}, {"text": "L", "fg_color": "#1f6aa5"}],
                [{"text": "L", "fg_color": "#1f6aa5"}, {"text": "L", "fg_color": "#1f6aa5"}, {"text": "L", "fg_color": "#1f6aa5"}, {"text": "L", "fg_color": "#1f6aa5"}, {"text": "L", "fg_color": "#1f6aa5"}, {"text": "L", "fg_color": "#1f6aa5"}, {"text": "L", "fg_color": "#1f6aa5"}],
                [{"text": "L", "fg_color": "#1f6aa5"}, {"text": "L", "fg_color": "#1f6aa5"}, {"text": "L", "fg_color": "#1f6aa5"}, {"text": "L", "fg_color": "#1f6aa5"}, {"text": "L", "fg_color": "#1f6aa5"}, {"text": "L", "fg_color": "#1f6aa5"}, {"text": "L", "fg_color": "#1f6aa5"}],
                [{"text": "L", "fg_color": "#1f6aa5"}, {"text": "L", "fg_color": "#1f6aa5"}, {"text": "L", "fg_color": "#1f6aa5"}, {"text": "L", "fg_color": "#1f6aa5"}, {"text": "L", "fg_color": "#1f6aa5"}, {"text": "L", "fg_color": "#1f6aa5"}, {"text": "L", "fg_color": "#1f6aa5"}]
            ]
        ]
    },
    {
        "ruta": "Carteleras\\rango.jpg",
        "nombre": "Rango",
        "sinopsis": "Rango es un camale\u00f3n que lleva toda su vida viviendo como mascota en un terrario. Sin embargo, un buen d\u00eda, mientras transportan su terrario, el recipiente se cae del auto en medio del desierto y acaba en un pueblo salvaje donde lo nombran alguacil.",
        "asientos": [
            [
                [{"text": "L", "fg_color": "#1f6aa5"}, {"text": "L", "fg_color": "#1f6aa5"}, {"text": "L", "fg_color": "#1f6aa5"}, {"text": "L", "fg_color": "#1f6aa5"}, {"text": "L", "fg_color": "#1f6aa5"}, {"text": "L", "fg_color": "#1f6aa5"}, {"text": "L", "fg_color": "#1f6aa5"}],
                [{"text": "L", "fg_color": "#1f6aa5"}, {"text": "L", "fg_color": "#1f6aa5"}, {"text": "L", "fg_color": "#1f6aa5"}, {"text": "L", "fg_color": "#1f6aa5"}, {"text": "L", "fg_color": "#1f6aa5"}, {"text": "L", "fg_color": "#1f6aa5"}, {"text": "L", "fg_color": "#1f6aa5"}],
                [{"text": "L", "fg_color": "#1f6aa5"}, {"text": "L", "fg_color": "#1f6aa5"}, {"text": "L", "fg_color": "#1f6aa5"}, {"text": "L", "fg_color": "#1f6aa5"}, {"text": "L", "fg_color": "#1f6aa5"}, {"text": "L", "fg_color": "#1f6aa5"}, {"text": "L", "fg_color": "#1f6aa5"}],
                [{"text": "L", "fg_color": "#1f6aa5"}, {"text": "L", "fg_color": "#1f6aa5"}, {"text": "L", "fg_color": "#1f6aa5"}, {"text": "L", "fg_color": "#1f6aa5"}, {"text": "L", "fg_color": "#1f6aa5"}, {"text": "L", "fg_color": "#1f6aa5"}, {"text": "L", "fg_color": "#1f6aa5"}],
                [{"text": "L", "fg_color": "#1f6aa5"}, {"text": "L", "fg_color": "#1f6aa5"}, {"text": "L", "fg_color": "#1f6aa5"}, {"text": "L", "fg_color": "#1f6aa5"}, {"text": "L", "fg_color": "#1f6aa5"}, {"text": "L", "fg_color": "#1f6aa5"}, {"text": "L", "fg_color": "#1f6aa5"}],
                [{"text": "L", "fg_color": "#1f6aa5"}, {"text": "L", "fg_color": "#1f6aa5"}, {"text": "L", "fg_color": "#1f6aa5"}, {"text": "L", "fg_color": "#1f6aa5"}, {"text": "L", "fg_color": "#1f6aa5"}, {"text": "L", "fg_color": "#1f6aa5"}, {"text": "L", "fg_color": "#1f6aa5"}],
                [{"text": "L", "fg_color": "#1f6aa5"}, {"text": "L", "fg_color": "#1f6aa5"}, {"text": "L", "fg_color": "#1f6aa5"}, {"text": "L", "fg_color": "#1f6aa5"}, {"text": "L", "fg_color": "#1f6aa5"}, {"text": "L", "fg_color": "#1f6aa5"}, {"text": "L", "fg_color": "#1f6aa5"}]
            ]
        ]
    }
]

with open("info_peliculas", "w") as f:
    json.dump(peliculas, f, indent=4, ensure_ascii=False, separators=(',', ': '))