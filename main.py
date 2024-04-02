from simpleicons.all import icons

def get_button(brand):
    icon = icons.get(brand)
    if icon:
        res = f"![{icon.title}](https://img.shields.io/badge/-{icon.slug}-{icon.hex}?logo={icon.slug}&logoColor=white)"
        return res
    else:
        return "Brand not found in the icon database."

if __name__ == "__main__":
    brand_name = input("Enter the brand name: ").lower()
    result = get_button(brand_name)
    print(result)
