def character(rgb_sum):
    if rgb_sum > 700:
        return ' ' * 2
    elif rgb_sum > 650:
        return ';' * 2
    elif rgb_sum > 600:
        return '|' * 2
    elif rgb_sum > 550:
        return '/' * 2
    elif rgb_sum > 500:
        return 'L' * 2
    elif rgb_sum > 450:
        return 'L' * 2
    elif rgb_sum > 400:
        return 'L' * 2
    elif rgb_sum > 350:
        return 'L' * 2
    elif rgb_sum > 300:
        return 'Y' * 2
    elif rgb_sum > 250:
        return 'R' * 2
    elif rgb_sum > 200:
        return 'K' * 2
    elif rgb_sum > 150:
        return 'E' * 2
    elif rgb_sum > 100:
        return 'H' * 2
    elif rgb_sum > 50:
        return 'M' * 2
    else:
        return 'N' * 2


def character2(rgb_sum):
    if rgb_sum > 700:
        return ' ' * 2
    elif rgb_sum > 650:
        return '.' * 2
    elif rgb_sum > 600:
        return ';' * 2
    elif rgb_sum > 550:
        return '|' * 2
    elif rgb_sum > 500:
        return '/' * 2
    elif rgb_sum > 450:
        return 'L' * 2
    elif rgb_sum > 400:
        return 'L' * 2
    elif rgb_sum > 350:
        return 'L' * 2
    elif rgb_sum > 300:
        return 'Y' * 2
    elif rgb_sum > 250:
        return 'R' * 2
    elif rgb_sum > 200:
        return 'K' * 2
    elif rgb_sum > 150:
        return 'E' * 2
    elif rgb_sum > 100:
        return 'H' * 2
    elif rgb_sum > 50:
        return 'M' * 2
    else:
        return 'N' * 2
