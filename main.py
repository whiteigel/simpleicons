from simpleicons.all import icons

def get_button(brand):
    icon = icons.get(brand)
    if icon:
        res = f"![{icon.title}](https://img.shields.io/badge/-{icon.slug}-{icon.hex}?logo={icon.slug}&logoColor=white)"
        return res
    else:
        return "Бренд не найден в базе данных значков."

def main_menu():
    brand_name = input("Введите имя бренда: ").lower()
    return get_button(brand_name)

print(main_menu())
