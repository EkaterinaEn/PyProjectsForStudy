calls = 0
def count_calls ():
    global calls
    calls = calls + 1
def string_info (str):
    count_calls()
    list1 = []
    list1.append(len(str))
    list1.append(str.upper())
    list1.append(str.lower())
    return list1
def is_contains (str, str_finder):
    count_calls()
    is_finde = False
    for s in str_finder:
        if str.lower() == s.lower():
            is_finde = True
    return is_finde

print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))
print(is_contains('cycle', ['recycle', 'cyclic']))
print(calls)