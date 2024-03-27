const kraje = [
    {
        "nazev": "Celá ČR",
        "kod": "19",
        "okresy": [
            {
                "nazev": "Celá ČR",
                "kod": "19"
            }
        ]
    },
    {
        "nazev": "Hlavní město Praha",
        "kod": "3018",
        "okresy": [
            {
                "nazev": "Praha",
                "kod": "3018"
            }
        ]
    },
    {
        "nazev": "Jihomoravský kraj",
        "kod": "3115",
        "okresy": [
            {
                "nazev": "Celý Jihomoravský kraj",
                "kod": "3115"
            },
            {
                "nazev": "Blansko",
                "kod": "40703"
            },
            {
                "nazev": "Brno-město",
                "kod": "40711"
            },
            {
                "nazev": "Brno-venkov",
                "kod": "40720"
            },
            {
                "nazev": "Břeclav",
                "kod": "40738"
            },
            {
                "nazev": "Hodonín",
                "kod": "40746"
            },
            {
                "nazev": "Vyškov",
                "kod": "40754"
            },
            {
                "nazev": "Znojmo",
                "kod": "40762"
            }
        ]
    },
    {
        "nazev": "Jihočeský kraj",
        "kod": "3034",
        "okresy": [
            {
                "nazev": "Celý Jihočeský kraj",
                "kod": "3034"
            },
            {
                "nazev": "Jindřichův Hradec",
                "kod": "40304"
            },
            {
                "nazev": "Prachatice",
                "kod": "40321"
            },
            {
                "nazev": "Písek",
                "kod": "40312"
            },
            {
                "nazev": "Strakonice",
                "kod": "40339"
            },
            {
                "nazev": "Tábor",
                "kod": "40347"
            },
            {
                "nazev": "České Budějovice",
                "kod": "40282"
            },
            {
                "nazev": "Český Krumlov",
                "kod": "40291"
            }
        ]
    },
    {
        "nazev": "Karlovarský kraj",
        "kod": "3051",
        "okresy": [
            {
                "nazev": "Celý Karlovarský kraj",
                "kod": "3051"
            },
            {
                "nazev": "Cheb",
                "kod": "40428"
            },
            {
                "nazev": "Karlovy Vary",
                "kod": "40436"
            },
            {
                "nazev": "Sokolov",
                "kod": "40444"
            }
        ]
    },
    {
        "nazev": "Kraj Vysočina",
        "kod": "3107",
        "okresy": [
            {
                "nazev": "Celý Kraj Vysočina",
                "kod": "3107"
            },
            {
                "nazev": "Havlíčkův Brod",
                "kod": "40657"
            },
            {
                "nazev": "Jihlava",
                "kod": "40665"
            },
            {
                "nazev": "Pelhřimov",
                "kod": "40673"
            },
            {
                "nazev": "Třebíč",
                "kod": "40681"
            },
            {
                "nazev": "Žďár nad Sázavou",
                "kod": "40690"
            }
        ]
    },
    {
        "nazev": "Královéhradecký kraj",
        "kod": "3085",
        "okresy": [
            {
                "nazev": "Celý Královéhradecký kraj",
                "kod": "3085"
            },
            {
                "nazev": "Hradec Králové",
                "kod": "40568"
            },
            {
                "nazev": "Jičín",
                "kod": "40576"
            },
            {
                "nazev": "Náchod",
                "kod": "40584"
            },
            {
                "nazev": "Rychnov nad Kněžnou",
                "kod": "40592"
            },
            {
                "nazev": "Trutnov",
                "kod": "40606"
            }
        ]
    },
    {
        "nazev": "Liberecký kraj",
        "kod": "3077",
        "okresy": [
            {
                "nazev": "Celý Liberecký kraj",
                "kod": "3077"
            },
            {
                "nazev": "Jablonec nad Nisou",
                "kod": "40533"
            },
            {
                "nazev": "Liberec",
                "kod": "40541"
            },
            {
                "nazev": "Semily",
                "kod": "40550"
            },
            {
                "nazev": "Česká Lípa",
                "kod": "40525"
            }
        ]
    },
    {
        "nazev": "Moravskoslezský kraj",
        "kod": "3140",
        "okresy": [
            {
                "nazev": "Celý Moravskoslezský kraj",
                "kod": "3140"
            },
            {
                "nazev": "Bruntál",
                "kod": "40860"
            },
            {
                "nazev": "Frýdek-Místek",
                "kod": "40878"
            },
            {
                "nazev": "Karviná",
                "kod": "40886"
            },
            {
                "nazev": "Nový Jičín",
                "kod": "40894"
            },
            {
                "nazev": "Opava",
                "kod": "40908"
            },
            {
                "nazev": "Ostrava-město",
                "kod": "40916"
            }
        ]
    },
    {
        "nazev": "Olomoucký kraj",
        "kod": "3123",
        "okresy": [
            {
                "nazev": "Celý Olomoucký kraj",
                "kod": "3123"
            },
            {
                "nazev": "Jeseník",
                "kod": "40771"
            },
            {
                "nazev": "Olomouc",
                "kod": "40789"
            },
            {
                "nazev": "Prostějov",
                "kod": "40797"
            },
            {
                "nazev": "Přerov",
                "kod": "40801"
            },
            {
                "nazev": "Šumperk",
                "kod": "40819"
            }
        ]
    },
    {
        "nazev": "Pardubický kraj",
        "kod": "3093",
        "okresy": [
            {
                "nazev": "Celý Pardubický kraj",
                "kod": "3093"
            },
            {
                "nazev": "Chrudim",
                "kod": "40614"
            },
            {
                "nazev": "Pardubice",
                "kod": "40622"
            },
            {
                "nazev": "Svitavy",
                "kod": "40631"
            },
            {
                "nazev": "Ústí nad Orlicí",
                "kod": "40649"
            }
        ]
    },
    {
        "nazev": "Plzeňský kraj",
        "kod": "3042",
        "okresy": [
            {
                "nazev": "Celý Plzeňský kraj",
                "kod": "3042"
            },
            {
                "nazev": "Domažlice",
                "kod": "40355"
            },
            {
                "nazev": "Klatovy",
                "kod": "40363"
            },
            {
                "nazev": "Plzeň-jih",
                "kod": "40380"
            },
            {
                "nazev": "Plzeň-město",
                "kod": "40371"
            },
            {
                "nazev": "Plzeň-sever",
                "kod": "40398"
            },
            {
                "nazev": "Rokycany",
                "kod": "40401"
            },
            {
                "nazev": "Tachov",
                "kod": "40410"
            }
        ]
    },
    {
        "nazev": "Středočeský kraj",
        "kod": "3026",
        "okresy": [
            {
                "nazev": "Celý Středočeský kraj",
                "kod": "3026"
            },
            {
                "nazev": "Benešov",
                "kod": "40169"
            },
            {
                "nazev": "Beroun",
                "kod": "40177"
            },
            {
                "nazev": "Kladno",
                "kod": "40185"
            },
            {
                "nazev": "Kolín",
                "kod": "40193"
            },
            {
                "nazev": "Kutná Hora",
                "kod": "40207"
            },
            {
                "nazev": "Mladá Boleslav",
                "kod": "40223"
            },
            {
                "nazev": "Mělník",
                "kod": "40215"
            },
            {
                "nazev": "Nymburk",
                "kod": "40231"
            },
            {
                "nazev": "Praha-východ",
                "kod": "40240"
            },
            {
                "nazev": "Praha-západ",
                "kod": "40258"
            },
            {
                "nazev": "Příbram",
                "kod": "40266"
            },
            {
                "nazev": "Rakovník",
                "kod": "40274"
            }
        ]
    },
    {
        "nazev": "Zlínský kraj",
        "kod": "3131",
        "okresy": [
            {
                "nazev": "Celý Zlínský kraj",
                "kod": "3131"
            },
            {
                "nazev": "Kroměříž",
                "kod": "40827"
            },
            {
                "nazev": "Uherské Hradiště",
                "kod": "40835"
            },
            {
                "nazev": "Vsetín",
                "kod": "40843"
            },
            {
                "nazev": "Zlín",
                "kod": "40851"
            }
        ]
    },
    {
        "nazev": "Ústecký kraj",
        "kod": "3069",
        "okresy": [
            {
                "nazev": "Celý Ústecký kraj",
                "kod": "3069"
            },
            {
                "nazev": "Chomutov",
                "kod": "40461"
            },
            {
                "nazev": "Děčín",
                "kod": "40452"
            },
            {
                "nazev": "Litoměřice",
                "kod": "40479"
            },
            {
                "nazev": "Louny",
                "kod": "40487"
            },
            {
                "nazev": "Most",
                "kod": "40495"
            },
            {
                "nazev": "Teplice",
                "kod": "40509"
            },
            {
                "nazev": "Ústí nad Labem",
                "kod": "40517"
            }
        ]
    }
]


document.addEventListener('DOMContentLoaded', function() {
    krajeLoader();
});

function krajeLoader() {
    var krajDropdown = document.getElementById('kraj-dropdown');
    var okresDropdown = document.getElementById('okres-dropdown');

    for (const kraj of kraje) {
        krajDropdown.options[krajDropdown.options.length] = new Option(kraj.nazev, kraj.kod);
    }

    krajDropdown.addEventListener('change', function () {
        adjustKraje();
    });

    function adjustKraje() {
        var krajid = parseInt(krajDropdown.value);
        okresDropdown.innerHTML = ''; // Clear existing options in end_year
        for (const kraj of kraje) {
            if(krajid == kraj.kod){
                var selectedKraj = kraj;
            }
        }

        for (const okres of selectedKraj.okresy){
            okresDropdown.options[okresDropdown.options.length] = new Option(okres.nazev, okres.kod);
        }
    }

    adjustKraje();
}