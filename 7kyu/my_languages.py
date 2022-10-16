# My Language Skills

def my_languages(results):
    # sort
    results = {k: v for k, v in sorted(results.items(), key=lambda item: item[1], reverse = True)}

    return_result = []
    for k, v in results.items():
        if v>=60:
            return_result.append(k)
    return return_result
