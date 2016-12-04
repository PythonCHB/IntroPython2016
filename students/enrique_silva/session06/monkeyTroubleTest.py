#monkey trouble

from monkeyTrouble import monkey_trouble

def test_monkey_true_true():
	assert monkey_trouble(True, True)


def test_monkey_false_false():
	assert monkey_trouble (False,False)

def test_monkey_true_false():
	assert monkey_trouble(True,False) is False




