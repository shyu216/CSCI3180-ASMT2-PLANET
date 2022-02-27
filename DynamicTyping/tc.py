from sys import float_repr_style


def is_pos(i):
    if i > 0:
        return True
    else:
        return False
is_pos(100)
is_pos(3.1)
is_pos("100")