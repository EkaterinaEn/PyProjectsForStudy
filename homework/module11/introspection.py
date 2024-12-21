
def introspection_info(obj):
    obj_type = type(obj).__name__
    attributes = [attribute for attribute in dir(obj) if not callable(getattr(obj, attribute))]
    methods = [method for method in dir(obj) if callable(getattr(obj, method))]
    module = obj.__class__.__module__
    info = {'type': obj_type, 'attributes': attributes, 'methods': methods, 'module': module}
    return info

number_info = introspection_info(42)
print(number_info)

string_info = introspection_info('я объект')
print(string_info)

list_info = introspection_info([1, 2, 3, 'я объект'])
print(list_info)