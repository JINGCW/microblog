class Loader(dict):
    def __init__(self, seq=None, **kwargs):
        super(Loader, self).__init__(seq, **kwargs)

    def __getattr__(self, item):
        try:
            value = self[item]
            if isinstance(value, dict):
                value = Loader(value)
            return value
        except KeyError:
            raise AttributeError('Dict object has no attribute %(item)s' % {'item': item})

    def __setattr__(self, key, value):
        self[key] = value


__source_path={
    'barline':'./src/match_large.csc'
}

print(__source_path['barline'])

def _barline_loader():
    return

# barline_loader=
