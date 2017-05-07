"""CLI around the system generator script.

Tested with python 3.6. May work with all 3.x.

"""


import argparse
from itertools import cycle
import create


def dedicated_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(dest='system_type')

    arbitrary = subparsers.add_parser('arbitrary', help='create an arbitrary system')
    arbitrary.add_argument('--ring', type=int, default=3,
                           help='number of ring to generate')
    arbitrary.add_argument('--planet-per-ring', type=int, metavar='N', nargs='+',
                           help='number of planet per ring', default=[42])
    arbitrary.add_argument('--planet-mass', type=float, metavar='N', nargs='+',
                           help='Planets mass in M⊕', default=[1])

    # special cases
    superearth = subparsers.add_parser('super_earth', help='create a system with super earth planets')
    earth_like = subparsers.add_parser('earth_like',  help='create a system with earth-like planets')
    smallearth = subparsers.add_parser('small_earth', help='create a system with small earth planets')


    # common parameters
    parser.add_argument('star', type=str, help='name of the star to populate')
    parser.add_argument('planet_file', type=str,
                        help='file to write the planets in')
    parser.add_argument('--min-ring-dist', type=float, default=1,
                        help='distance in AU from star to the closer ring')
    parser.add_argument('--ring-gap', type=float, metavar='N', nargs='+',
                        help='distance in AU between rings', default=0)
    parser.add_argument('--inclination-delta', type=float,
                        metavar='N', nargs='+', default=[0],
                        help='Modifier(s) to inclination to apply to ring orbits')

    return parser


def parsed_cli() -> 'namespace':
    return dedicated_parser().parse_args()


if __name__ == "__main__":
    args = parsed_cli()
    print(args)
    if args.system_type == 'arbitrary':
        create.write_system(
            create.create_system(
                ring=args.ring,
                gen_planet_per_ring=args.planet_per_ring,
                star_name=args.star,
                gen_distance_between_rings=args.ring_gap,
                min_distance_to_star=args.min_ring_dist,
                gen_planet_mass=args.planet_mass,
                gen_ring_inclinations=args.inclination_delta,
            ),
            args.planet_file
        )
    elif args.system_type == 'super_earth':
        create.write_system(
            create.create_system(
                ring=3,
                gen_planet_per_ring=19,
                star_name=args.star,
                gen_distance_between_rings=args.ring_gap,
                min_distance_to_star=args.min_ring_dist,
                gen_planet_mass=10,
                gen_ring_inclinations=args.inclination_delta,
            ),
            args.planet_file
        )
    elif args.system_type == 'earth_like':
        create.write_system(
            create.create_system(
                ring=6,
                gen_planet_per_ring=42,
                star_name=args.star,
                gen_distance_between_rings=args.ring_gap,
                min_distance_to_star=args.min_ring_dist,
                gen_planet_mass=1,
                gen_ring_inclinations=args.inclination_delta,
            ),
            args.planet_file
        )
    elif args.system_type == 'small_earth':
        create.write_system(
            create.create_system(
                ring=13,
                gen_planet_per_ring=89,
                star_name=args.star,
                gen_distance_between_rings=args.ring_gap,
                min_distance_to_star=args.min_ring_dist,
                gen_planet_mass=0.1,
                gen_ring_inclinations=args.inclination_delta,
            ),
            args.planet_file
        )
    else:
        raise ValueError("System type '{}' is unknow".format(args.system_type))
