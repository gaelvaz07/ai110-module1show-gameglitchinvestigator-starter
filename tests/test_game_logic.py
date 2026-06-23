from logic_utils import check_guess, get_range_for_difficulty, update_score

# --- Existing tests (fixed to handle tuple return) ---

def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    outcome, message = check_guess(50, 50)
    assert outcome == "Win"

def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    outcome, message = check_guess(60, 50)
    assert outcome == "Too High"

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    outcome, message = check_guess(40, 50)
    assert outcome == "Too Low"

# --- New tests targeting fixed bugs ---

def test_hint_says_lower_when_too_high():
    # FIX: Hints were backwards - too high should say Go LOWER
    outcome, message = check_guess(60, 50)
    assert "LOWER" in message

def test_hint_says_higher_when_too_low():
    # FIX: Hints were backwards - too low should say Go HIGHER
    outcome, message = check_guess(40, 50)
    assert "HIGHER" in message

def test_hard_difficulty_range():
    # FIX: Hard was wrongly set to 1-50, should be harder than Normal
    low, high = get_range_for_difficulty("Hard")
    assert high == 200

def test_wrong_guess_loses_points():
    # FIX: Wrong guesses were rewarding points on even attempts
    score = update_score(100, "Too High", 2)
    assert score == 95  # should always subtract 5