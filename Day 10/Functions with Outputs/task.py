def format_name(f_name, l_name):
    name = f_name.title() + " " + l_name.title()
    return name
    # return f"{f_name.title()} {l_name.title()}"

print(format_name("RENUKA", "ANBALAGAN"))
result_name = format_name("riya", "dineshkUMAR")
print(result_name)


def outer_function(a, b):
    def inner_function(c, d):
        return c + d

    return inner_function(a, b)


result = outer_function(5, 10)
print(result)