import abc
from typing import List

class NewsFetcherAdapter(metaclass= abc.ABCMeta):
    @abc.abstractclassmethod
    def