# exceptions
def fetcher(obj, index):
    return obj[index]

x = 'spam'

def catcher(index):
    y = False
    try:
        y = fetcher(x,index)
    except IndexError:
        print("Exception: incorrect index requested")
    finally:
        return y

for i in range(0,5):
    print(catcher(i))