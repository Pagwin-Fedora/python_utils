def for_iter(init,conditional,incrementor):
    val = init()
    while conditional(val):
        yield val
        val = incrementor(val)
