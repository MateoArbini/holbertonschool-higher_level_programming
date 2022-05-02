def multiple_returns(sentence):
    tuple_a = ()
    length = len(sentence)
    first = sentence[0]
    if(length == 0):
        first = None

    added_value_tuple = (length,)
    added_value_tuple2 = (first,)
    tuple_a = tuple_a + added_value_tuple + added_value_tuple2

    return tuple_a
