import collections

class filter(object):
        def __init__(self, alias='filter', equals=False, **conditions):
                self.alias = alias
                self._c = conditions
                for k, v in self._c.iteritems():
                        if isinstance(v, basestring) or not isinstance(v, collections.Iterable):
                                self._c[k] = [v]
                if equals:
                        self._compare = self._equals_compare

        def _equals_compare(self, v, gv):
                return any([gv == e for e in v]) #if any value matches the current key

        def _compare(self, v, gv):
                try:
                        return any([e in gv for e in v]) #if any value contains the current key
                except: # in case some values are integers or something
                        return any([gv == e for e in v]) #if any value matches the current key

        def check_filter(self, **values):
                gen = ((c, self._c[c]) for c in self._c if self._c[c] is not None)
                trues = [self._compare(v, values[k]) for k, v in gen if values.get(k, None) != None]
                return all(trues) if trues else False
                #true when all values match for at least one value in all conditions