#!/usr/bin/env python2

import itertools


def first(p, l, default=None):
  """
  Returns the first element x in l that satisfies p(x), or default if no such element exist
  """
  return next(itertools.ifilter(p, l), default)


def last(p, l, default=None):
  """
  Returns the last element x in l that satisfies p(x), or default if no such element exist
  """
  return first(p, reversed(l), default)


def contains(p, l):
  """
  Returns True if there is at least one element x in l such that p(x) is True
  """
  return any(p(x) for x in l)


def count(p, l=lambda _: True):
  """
  Returns the number of items x in l for which p(x) is True
  """
  return sum(1 for x in l if p(x))


def select_many(f, l):
  """
  Returns an iterator over a flattened enumerable containing the enumerables f(x) for all x in l
    >>> selectMany(lambda l: l[:2], ((A, B, C), (D, E, F)))
    (A, B, D, E)
  """
  return itertools.chain.from_iterable(f(x) for x in l)


def partition(p, l):
  """
  Returns two lists: the first of the elements x in l such that p(x) is True for all,
  the second of the elements s x in l that are not in the first list, i.e. for which p(x)
  is False
  """
  tl, fl = list(), list()
  # Caching the append lookup for a miniscule speedup
  ta, fa = tl.append, fl.append

  for x in l:
    (ta if p(x) else fa)(x)
  return tl, fl


def chunks(n, l):
  """
  Returns an iterator over lists of n consecutive elements from l
  """
  for i in xrange(0, len(l), n):
    yield l[i:(i + n)]


def map_vals(f, d):
  """
  Maps the values in the dictionary d, using the function f, while keeping the keys
  """
  return {k: f(v) for k, v in d.iteritems()}


def map_keys(f, d):
  """
  Maps the keys in the dictionary d, using the function f, while keeping the values
  """
  return {f(k): v for k, v in d.iteritems()}
