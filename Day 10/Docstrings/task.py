# def format_name(f_name, l_name):
#     formated_f_name = f_name.title()
#     formated_l_name = l_name.title()
#     return f"{formated_f_name} {formated_l_name}"
#
#
# formatted_name = format_name("AnGeLa", "YU")
#
# length = len(formatted_name)
#

def outer_function(a, b):
    def inner_function(c, d):
        return c + d
    return inner_function(a, b)

result = outer_function(5, 10)
print(result)
