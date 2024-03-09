from pandas.core.common import flatten


class FlatIterator:

    def __init__(self, list_of_list):
        self.list_of_list = list_of_list
        self.new_list = []
        self.count_element = 0
        self.item = ''

    def __iter__(self):
        self.new_list = list(flatten(self.list_of_list))
        return self

    def __next__(self):
        if len(self.new_list) == self.count_element:
            # print('Второй тест пройден!')
            raise StopIteration
        self.item = self.new_list[self.count_element]
        self.count_element += 1
        return self.item


def test_3():
    list_of_lists_2 = [
        [['a'], ['b', 'c']],
        ['d', 'e', [['f'], 'h'], False],
        [1, 2, None, [[[[['!']]]]], []]
    ]

    for flat_iterator_item, check_item in zip(
            FlatIterator(list_of_lists_2),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']
    ):
        assert flat_iterator_item == check_item
    print('Второй тест пройден!')
    assert list(FlatIterator(list_of_lists_2)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']
