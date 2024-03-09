import types


def flat_generator(list_of_lists):
    new_list = []
    for element in list_of_lists:
        new_list.extend(element)
    len_ = len(new_list)
    for i in range(len_):
        yield new_list[i]


def test_2():
    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    for flat_iterator_item, check_item in zip(
            flat_generator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):
        assert flat_iterator_item == check_item

    assert list(flat_generator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    print('Третий тест пройден!')
    assert isinstance(flat_generator(list_of_lists_1), types.GeneratorType)
