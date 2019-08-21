def mean(num_list):
    assert isinstance(num_list, list)
#    if len(num_list) == 0:
#        raise Exception("The algebraic mean of an empty list is undefined. "
#        "Please provide a list of numbers")
#    else:
#        return sum(num_list)/len(num_list)
    try:
        return sum(num_list)/len(num_list)
# To get error message with detailed message
#    except ZeroDivisionError as detail:
#        msg = "Please provide a list of numbers, currently empty"
#        raise ZeroDivisionError(detail.__str__() + "\n" + msg)

    except ZeroDivisionError :
        return 0
    except TypeError as detail:
        msg="Please provide list of numbers."
        raise TypeError(detail.__str__() + "\n" + msg)
    
#Assert num_list is actually a list and don't divide by 0
