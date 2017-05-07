"""Generation of Space Engine data files for creating the constellation of
the Ultimate Engineered System.

"""


from random import randint
from itertools import cycle
from templates import PLANET_TEMPLATE


DEFAULT_SYSTEM_FILE_NAME = 'generated_planets.sc'
DEFAULT_STAR_NAME = 'RS 1228-511-0-0-320/EngineeredSystemStar'
DEFAULT_DIST_BETWEEN_RINGS = 0.2
DEFAULT_MIN_DISTANCE_TO_STAR = 1
DEFAULT_PLANET_NAME_TEMPLATE = 'ES {number} {ring}'
DEFAULT_RING_NUMBER, DEFAULT_PLANET_PER_RING = 6, 42
DEFAULT_RING_INCLINATION_STEP = 5
DEFAULT_PLANET_MASS = 1
MIN_COLOR, MAX_COLOR = 150, 255  # range of RGB values

# Ground knowledge
MAX_DEGREES = 360


def planet_script(name:str, star_name:str, semimajoraxis:float,
                  mass:float=1, radius:float=10000,
                  ascending_node:float=0., eccentricity:float=0.,
                  inclination:float=0., mean_anomaly:float=0.,
                  color:(int, int, int)=None):
    color = color or tuple(randint(MIN_COLOR, MAX_COLOR) for _ in range(3))
    return PLANET_TEMPLATE.format(
        name=name,
        star_name=star_name,
        color=' '.join(map(str, color)),
        semimajoraxis=semimajoraxis,
        eccentricity=eccentricity,
        inclination=inclination,
        ascending_node=ascending_node,
        mean_anomaly=mean_anomaly,
        mass=float(mass),
        radius=float(radius),
    )


def _iterable(value:object or iter) -> iter:
    try:
        iter(value)
        return cycle(value)
    except TypeError:
        return cycle((value,))


def create_system(ring:int, gen_planet_per_ring:int,
                  star_name:str=DEFAULT_STAR_NAME,
                  gen_distance_between_rings:float=DEFAULT_DIST_BETWEEN_RINGS,
                  min_distance_to_star:float=DEFAULT_MIN_DISTANCE_TO_STAR,
                  planet_name_template:str=DEFAULT_PLANET_NAME_TEMPLATE,
                  gen_ring_inclinations:float=DEFAULT_RING_INCLINATION_STEP,
                  gen_planet_mass:float=DEFAULT_PLANET_MASS):
    # get iterable values
    gen_planet_per_ring = _iterable(gen_planet_per_ring)
    gen_distance_between_rings = _iterable(gen_distance_between_rings)
    gen_planet_mass = _iterable(gen_planet_mass)
    gen_ring_inclinations = _iterable(gen_ring_inclinations)

    # generate planet one by one
    for ring_number in range(ring):
        reverse_move = bool(ring_number % 2)
        ring_inclination = ring_number * next(gen_ring_inclinations)
        sens_inclination = (MAX_DEGREES / 2) if reverse_move else 0  # orbit direction
        inclination = ring_inclination + sens_inclination
        planet_per_ring = next(gen_planet_per_ring)
        distance_between_rings = next(gen_distance_between_rings)
        planet_mass = next(gen_planet_mass)
        for planet_number in range(planet_per_ring):
            dist_to_star = min_distance_to_star + distance_between_rings * ring_number
            name = planet_name_template.format(ring=ring_number, star=star_name, number=planet_number)
            angle_per_planet = planet_number * MAX_DEGREES / planet_per_ring
            yield planet_script(
                name, star_name, dist_to_star,
                mass=planet_mass,
                mean_anomaly=angle_per_planet,
                inclination=inclination
            )


def write_system(planets:iter, filename:str):
    with open(filename, 'w') as fd:
        for planet in planets:
            fd.write(planet + '\n\n')


if __name__ == "__main__":
    write_system(create_system(DEFAULT_RING_NUMBER, DEFAULT_PLANET_PER_RING), DEFAULT_SYSTEM_FILE_NAME)
