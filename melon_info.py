"""Print out all the melons in our inventory."""


from melons import melons_traits

def print_melon(melons_traits):
    """Print each melon with corresponding attribute information."""

    # itemized melons into melon-attribute 
    for melon, attributes in melons_traits.items():
        print(melon.upper())
        # for each melon call their attributes as key-values
        for attribute in attributes:
            print(f"    {attribute}: {attributes[attribute]}")

print_melon(melons_traits)