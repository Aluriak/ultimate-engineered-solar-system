"""Generation of Space Engine data files for creating the constellation of
the Ultimate Engineered System.

"""


from random import randint
from templates import PLANET_TEMPLATE


DEFAULT_SYSTEM_FILE_NAME = '/home/lucas/.wine/drive_c/SpaceEngine/addons/catalogs/planets/EngineeredSystem.sc'
MIN_COLOR, MAX_COLOR = 150, 255  # range of RGB values
DEFAULT_STAR_NAME = 'RS 1228-511-0-0-320/EngineeredSystemStar'
DEFAULT_DIST_BETWEEN_RINGS = 0.5
DEFAULT_MIN_DISTANCE_TO_STAR = 1.0
DEFAULT_PLANET_NAME_TEMPLATE = 'ES {number} {ring}'

MAX_DEGREES = 360


def planet_script(name:str, star_name:str, semimajoraxis:float,
                  ascending_node:float=0., eccentricity:float=0.0,
                  mean_anomaly:float=0.0, color:(int, int, int)=None):
    color = color or tuple(randint(MIN_COLOR, MAX_COLOR) for _ in range(3))
    return PLANET_TEMPLATE.format(
        name=name,
        star_name=star_name,
        color=' '.join(map(str, color)),
        semimajoraxis=semimajoraxis,
        eccentricity=eccentricity,
        ascending_node=ascending_node,
        mean_anomaly=mean_anomaly
    )


def create_system(ring:int, planet_per_ring:int, star_name:str=DEFAULT_STAR_NAME,
                  distance_between_rings:float=DEFAULT_DIST_BETWEEN_RINGS,
                  min_distance_to_star:float=DEFAULT_MIN_DISTANCE_TO_STAR,
                  planet_name_template:str=DEFAULT_PLANET_NAME_TEMPLATE):
    for ring_number in range(ring):
        reverse_move = bool(ring_number % 2)
        for planet_number in range(planet_per_ring):
            dist_to_star = min_distance_to_star + distance_between_rings * ring_number
            name = planet_name_template.format(ring=ring_number, star=star_name, number=planet_number)
            angle_per_planet = planet_number * MAX_DEGREES / planet_per_ring
            yield planet_script(name, star_name, dist_to_star, mean_anomaly=angle_per_planet)


def write_system(planets:iter, filename:str):
    with open(filename, 'w') as fd:
        for planet in planets:
            fd.write(planet + '\n\n')


if __name__ == "__main__":
    write_system(create_system(2, 10), DEFAULT_SYSTEM_FILE_NAME)
