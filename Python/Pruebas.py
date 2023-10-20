def quitar_repetidos(h):
    pas , h = 0 , list(h)
    while len(h) != 0:
        if h[pas] == h[pas+1]:
            h.pop(pas), h.pop(pas)
            pas = 0
            continue
        elif pas+1 != len(h)-1:
            pas += 1
            continue
        break
    return '"'+''.join(h)+'"'