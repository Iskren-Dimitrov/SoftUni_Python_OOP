def vowel_filter(function):
    def wrapper():
        vol = ["a", "e", "i", "o", "u"]
        res = function()
        result = [s for s in res if s in vol]
        return result

    return wrapper


@vowel_filter
def get_letters():
    return ["a", "b", "c", "d", "e"]


print(get_letters())
