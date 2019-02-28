#!/usr/bin/env python

x = 23.45

values = [5.9, 4.8, 3.6, 0, 5.1, 7.2, 'wombat']

for v in values:
    try:
        result = x / v
    except ZeroDivisionError as err:
        print(err)
    except TypeError as err:
        print(err)
    except (KeyError, IndexError) as err:
        print("Huh??")
    except: #  Exception as err:
        #print("{}: {}".format(type(err).__name__, err))
        result = float('Nan')
        exit()
    else:  # no exceptions
        pass
    finally:
        pass
    print(result)

