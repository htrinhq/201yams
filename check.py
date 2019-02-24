def error() -> int:
    """Error message."""
    print("\tINVALID ARGUMENT")
    print("->\ttype \"-h\" for help\t<-")
    exit(84)

def check_dices(argv) -> int:
    """Check if dices values are correct."""
    for index, value in enumerate(argv, 0):
        if index == 0 or index == 6:
            continue
        elif value.isnumeric() == False:
            return 1
        elif (int(value) < 0 or int(value) > 6) and (index != 0 or index != 7):
            return 1
        else:
            continue
    return 0


def check_last_value(argv):
    """Check last arg, to see if resukt expected is correct."""
    value = argv[6].split('_')
    if value[0] != 'pair' and value[0] != 'three' and value[0] != 'four' and\
    value[0] != 'full' and value[0] != 'straight' and value[0] != 'yams':
        error()
    if len(value) == 1:
        error()
    if len(value) == 2 and (value[1].isnumeric() == False or int(value[1]) < 1
    or int(value[1]) > 6):
        error()
    if len(value) == 3 and (value[2].isnumeric() == False or int(value[2]) < 1
    or int(value[2]) > 6 or int(value[1]) == int(value[2])) or\
    int(value[1]) < 1 or int(value[1]) > 6:
        error()
    return value
