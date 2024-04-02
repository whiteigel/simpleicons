from simpleicons.all import icons

def get_button(brand):
    icon = icons.get(brand)
    if icon:
        res = f"![{icon.title}](https://img.shields.io/badge/-{icon.slug}-{icon.hex}?logo={icon.slug}&logoColor=white)"
        return res
    else:
        return "No such brand in Simpleicon DB."

def main_menu():
    brand_name = input("Enter brand name: ").lower()
    return get_button(brand_name)

print(main_menu())
