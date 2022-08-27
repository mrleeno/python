#*args, tuple args
def function(named_arg, *args):
    print(named_arg)
    print(args)
function(0, 1, 2, 3, 4, 5)

#**kwargs, dictionary kwargs
def my_func(x, y=7, *args, **kwargs):
    print(kwargs)
my_func(2, 3, 4, 5, 6, a=7, b=8)


def my_min(*args):
    return min(args)

print(my_min(13, 4, 42, 120, 7))
