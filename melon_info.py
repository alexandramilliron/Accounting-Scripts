"""Print out all the melons in our inventory."""


from melons import melons


def print_melon(name):
    """Print each melon with corresponding attribute information."""

    melon = melons[name]
    seeds = melon[seedlessness]
    price = melon[price]

    print(f'{name}s {seeds} seeds and are ${price:.2f}')


# from melons import melons

# def print_all_melons(melons):
#     """Print each melon with corresponding attribute information."""

#     for melon_name, attributes in melons.items():
#         print(melon_name.upper())

#         for attribute, value in attributes.items():
#             print(f'{attribute}: {value}')
