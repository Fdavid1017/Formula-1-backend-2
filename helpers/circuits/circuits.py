from exceptions.not_found_exception import NotFoundException

circuits = {
    'bahrain': {
        "circuit_id": "bahrain",
        "image_name": "bahrain.png",
        "first_gp": 2004,
        "number_of_laps": 57,
        "length": 5.412,
        "race_distance": 308.238,
        "gjson_map": "bh-2002.geojson",
        "primary_color": "#ce1127",
        "secondary": "#a50e1f",
        "tertiary": "#ffffff"
    },
    'imola': {
        "circuit_id": "imola",
        "image_name": "imola.png",
        "first_gp": 1980,
        "number_of_laps": 63,
        "length": 4.909,
        "race_distance": 309.049,
        "gjson_map": "it-1953.geojson",
        "primary_color": "#009247",
        "secondary": "#ffffff",
        "tertiary": "#cf2b36"
    },
    'portimao': {
        "circuit_id": "portimao",
        "image_name": "portimao.png",
        "first_gp": 2020,
        "number_of_laps": 66,
        "length": 4.653,
        "race_distance": 306.826,
        "gjson_map": "pt-2008.geojson",
        "primary_color": "#006401",
        "secondary": "#fe0002",
        "tertiary": "#fffc0d"
    },
    'catalunya': {
        "circuit_id": "catalunya",
        "image_name": "catalunya.png",
        "first_gp": 1991,
        "number_of_laps": 66,
        "length": 4.675,
        "race_distance": 308.424,
        "gjson_map": "es-1991.geojson",
        "primary_color": "#c20f15",
        "secondary": "#fec400",
        "tertiary": "#9e0918"
    },
    'monaco': {
        "circuit_id": "monaco",
        "image_name": "monaco.png",
        "first_gp": 1991,
        "number_of_laps": 66,
        "length": 4.675,
        "race_distance": 308.424,
        "gjson_map": "mc-1929.geojson",
        "primary_color": "#ce1127",
        "secondary": "#ffffff",
        "tertiary": "#a50e1f"
    },
    'BAK': {
        "circuit_id": "BAK",
        "image_name": "BAK.png",
        "first_gp": 2016,
        "number_of_laps": 51,
        "length": 6.003,
        "race_distance": 306.049,
        "gjson_map": "az-2016.geojson",
        "primary_color": "#0097c2",
        "secondary": "#e00034",
        "tertiary": "#00ae66"
    },
    'ricard': {
        "circuit_id": "ricard",
        "image_name": "ricard.png",
        "first_gp": 2016,
        "number_of_laps": 51,
        "length": 6.003,
        "race_distance": 306.049,
        "gjson_map": "fr-1969.geojson",
        "primary_color": "#002496",
        "secondary": "#ffffff",
        "tertiary": "#ed2839"
    },
    'red_bull_ring': {
        "circuit_id": "red_bull_ring",
        "image_name": "red_bull_ring.png",
        "first_gp": 1970,
        "number_of_laps": 71,
        "length": 4.318,
        "race_distance": 306.452,
        "gjson_map": "at-1969.geojson",
        "primary_color": "#ed2839",
        "secondary": "#ffffff",
        "tertiary": "#be202e"
    },
    'silverstone': {
        "circuit_id": "silverstone",
        "image_name": "silverstone.png",
        "first_gp": 1950,
        "number_of_laps": 52,
        "length": 5.891,
        "race_distance": 306.198,
        "gjson_map": "gb-1948.geojson",
        "primary_color": "#d0142c",
        "secondary": "#042373",
        "tertiary": "#ffffff"
    },
    'hungaroring': {
        "circuit_id": "hungaroring",
        "image_name": "hungaroring.png",
        "first_gp": 1986,
        "number_of_laps": 70,
        "length": 4.381,
        "race_distance": 306.63,
        "gjson_map": "hu-1986.geojson",
        "primary_color": "#ce1127",
        "secondary": "#ffffff",
        "tertiary": "#008651"
    },
    'spa': {
        "circuit_id": "spa",
        "image_name": "spa.png",
        "first_gp": 1950,
        "number_of_laps": 44,
        "length": 7.004,
        "race_distance": 308.052,
        "gjson_map": "be-1925.geojson",
        "primary_color": "#ed2839",
        "secondary": "#fae043",
        "tertiary": "#000000"
    },
    'zandvoort': {
        "circuit_id": "zandvoort",
        "image_name": "zandvoort.png",
        "first_gp": 1952,
        "number_of_laps": 72,
        "length": 4.259,
        "race_distance": 306.648,
        "gjson_map": "nl-1948.geojson",
        "primary_color": "#ae1c27",
        "secondary": "#ffffff",
        "tertiary": "#21468c"
    },
    'monza': {
        "circuit_id": "monza",
        "image_name": "monza.png",
        "first_gp": 1950,
        "number_of_laps": 53,
        "length": 5.793,
        "race_distance": 306.72,
        "gjson_map": "it-1922.geojson",
        "primary_color": "#009247",
        "secondary": "#cf2a38",
        "tertiary": "#ffffff"
    },
    'sochi': {
        "circuit_id": "sochi",
        "image_name": "sochi.png",
        "first_gp": 2014,
        "number_of_laps": 53,
        "length": 5.848,
        "race_distance": 309.745,
        "gjson_map": "ru-2014.geojson",
        "primary_color": "#d52b1e",
        "secondary": "#0038a5",
        "tertiary": "#ffffff"
    },
    'marina_bay': {
        "circuit_id": "marina_bay",
        "image_name": "marina_bay.png",
        "first_gp": 2008,
        "number_of_laps": 61,
        "length": 5.063,
        "race_distance": 308.706,
        "gjson_map": "sg-2008.geojson",
        "primary_color": "#d52b1e",
        "secondary": "#0038a5",
        "tertiary": "#ffffff"
    },
    'suzuka': {
        "circuit_id": "suzuka",
        "image_name": "suzuka.png",
        "first_gp": 1987,
        "number_of_laps": 53,
        "length": 5.807,
        "race_distance": 307.471,
        "gjson_map": "jp-1962.geojson",
        "primary_color": "#bb002b",
        "secondary": "#ffffff",
        "tertiary": "#960022"
    },
    'americas': {
        "circuit_id": "americas",
        "image_name": "americas.png",
        "first_gp": 2012,
        "number_of_laps": 56,
        "length": 5.513,
        "race_distance": 308.405,
        "gjson_map": "us-2012.geojson",
        "primary_color": "#b90b30",
        "secondary": "#002665",
        "tertiary": "#ffffff"
    },
    'rodriguez': {
        "circuit_id": "rodriguez",
        "image_name": "rodriguez.png",
        "first_gp": 1963,
        "number_of_laps": 71,
        "length": 4.304,
        "race_distance": 305.354,
        "gjson_map": "mx-1962.geojson",
        "primary_color": "#006847",
        "secondary": "#ce1127",
        "tertiary": "#ffffff"
    },
    'interlagos': {
        "circuit_id": "interlagos",
        "image_name": "interlagos.png",
        "first_gp": 1973,
        "number_of_laps": 71,
        "length": 4.309,
        "race_distance": 305.909,
        "gjson_map": "br-1940.geojson",
        "primary_color": "#009c3b",
        "secondary": "#fddf01",
        "tertiary": "#002776"
    },
    'albert_park': {
        "circuit_id": "albert_park",
        "image_name": "albert_park.png",
        "first_gp": 1996,
        "number_of_laps": 58,
        "length": 5.303,
        "race_distance": 307.574,
        "gjson_map": "au-1953.geojson",
        "primary_color": "#01008c",
        "secondary": "#ef0707",
        "tertiary": "#ffffff"
    },
    'jeddah': {
        "circuit_id": "jeddah",
        "image_name": "jeddah.png",
        "first_gp": 2021,
        "number_of_laps": 50,
        "length": 6.175,
        "race_distance": 308.75,
        "gjson_map": "sa-2021.geojson",
        "primary_color": "#006c35",
        "secondary": "#00562a",
        "tertiary": "#ffffff"
    },
    'yas_marina': {
        "circuit_id": "yas_marina",
        "image_name": "yas_marina.png",
        "first_gp": 2009,
        "number_of_laps": 55,
        "length": 5.554,
        "race_distance": 305.355,
        "gjson_map": "ae-2009.geojson",
        "primary_color": "#ce1127",
        "secondary": "#009e49",
        "tertiary": "#000000"
    },
    'istanbul': {
        "circuit_id": "istanbul",
        "image_name": "yas_marina.png",
        "first_gp": 2005,
        "number_of_laps": 58,
        "length": 5.338,
        "race_distance": 309.396,
        "gjson_map": "ae-2009.geojson",
        "primary_color": "#ce1127",
        "secondary": "#009e49",
        "tertiary": "#000000"
    },
    'losail': {
        "circuit_id": "losail",
        "image_name": "quatar.png",
        "first_gp": 2021,
        "number_of_laps": 57,
        "length": 5.38,
        "race_distance": 306.66,
        "gjson_map": "qt-2021.geojson",
        "primary_color": "#8a1437",
        "secondary": "#630f28",
        "tertiary": "#ffffff"
    }
}


def get_circuit(id):
    circuit = circuits[id]

    if circuit is None:
        raise NotFoundException(f'No circuit found with the id of {id}')

    return circuit
