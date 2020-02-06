def help(*args):
    return 'No help for U!'


def lmgtfy_search(*args):
    if len(args) == 0:
        return 'Введите **непустой** поисковой запрос!'

    q = ' '.join(args)
    return 'https://google.com/search?q=' + str(q.encode('utf-8')).replace('\\x', '%').replace(' ', '+')[2:-1]
