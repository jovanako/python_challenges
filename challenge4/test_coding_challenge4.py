from coding_challenge4 import wash_hands

def test_wash_hands():
  assert wash_hands(8, 7) == "588 minutes and 0 seconds"

  assert wash_hands(0, 0) == "0 minutes and 0 seconds"

  assert wash_hands(7, 9) == "661 minutes and 30 seconds"

def test_something_else():
  assert 1 == 1