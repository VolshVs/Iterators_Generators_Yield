import types

from pandas.core.common import flatten


def flat_generator(list_of_list):
    new_list = list(flatten(list_of_list))
    len_ = len(new_list)
    for i in range(len_):
        yield new_list[i]


def test_4():
    list_of_lists_2 = [
        [['a'], ['b', 'c']],
        ['d', 'e', [['f'], 'h'], False],
        [1, 2, None, [[[[['!']]]]], []]
    ]

    for flat_iterator_item, check_item in zip(
            flat_generator(list_of_lists_2),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']
    ):
        assert flat_iterator_item == check_item

    assert list(flat_generator(list_of_lists_2)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']
    print('Четвертый тест пройден!')
    assert isinstance(flat_generator(list_of_lists_2), types.GeneratorType)
