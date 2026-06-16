from basePizza import BasePizza
from cheezeAddons import Cheese

if __name__ == "__main__":
    pza = BasePizza()
    print(pza.get_price()) # we don't wan't any addons
    cheeze_pza = Cheese(pza)
    print(cheeze_pza.get_price())