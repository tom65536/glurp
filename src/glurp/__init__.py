"""Glob-like URL processing."""

from __future__ import annotations

import collections.abc


__version__ = '0.1.0'



def urlfilter(urls: collections.abc.Iterable[str], pat: str) ->
collections.abc.Iterable[str]:
    pass

def urlmatch(url: str, pat: str) -> bool:
    pass


def translate(pat: str) -> str:
    pass
