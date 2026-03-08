import pytest
import sys
from pathlib import Path

# Add parent directory to path so we can import logic_utils
sys.path.insert(0, str(Path(__file__).parent.parent))

from logic_utils import check_guess, parse_guess, get_range_for_difficulty, update_score


# ============================================================================
# ORIGINAL TESTS (FIXED FOR TUPLE RETURN)
# ============================================================================


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


# ============================================================================
# ADDITIONAL TESTS FOR CHECK_GUESS
# ============================================================================


class TestCheckGuess:
    """Comprehensive tests for check_guess function"""

    def test_winning_guess_returns_correct_message(self):
        outcome, message = check_guess(50, 50)
        assert outcome == "Win"
        assert message == "🎉 Correct!"

    def test_too_high_returns_correct_message(self):
        outcome, message = check_guess(75, 50)
        assert outcome == "Too High"
        assert message == "📈 Go LOWER!"

    def test_too_low_returns_correct_message(self):
        outcome, message = check_guess(25, 50)
        assert outcome == "Too Low"
        assert message == "📉 Go HIGHER!"

    def test_boundary_values_high(self):
        outcome, message = check_guess(100, 1)
        assert outcome == "Too High"

    def test_boundary_values_low(self):
        outcome, message = check_guess(1, 100)
        assert outcome == "Too Low"

    def test_negative_numbers(self):
        outcome, message = check_guess(-10, 0)
        assert outcome == "Too Low"

    def test_zero_guess(self):
        outcome, message = check_guess(0, 0)
        assert outcome == "Win"

    def test_large_numbers(self):
        outcome, message = check_guess(1000000, 999999)
        assert outcome == "Too High"


# ============================================================================
# TESTS FOR PARSE_GUESS
# ============================================================================


class TestParseGuess:
    """Comprehensive tests for parse_guess function"""

    def test_valid_positive_integer(self):
        ok, value, error = parse_guess("50")
        assert ok is True
        assert value == 50
        assert error is None

    def test_valid_decimal_is_converted_to_int(self):
        ok, value, error = parse_guess("50.5")
        assert ok is True
        assert value == 50
        assert error is None

    def test_decimal_rounds_down(self):
        ok, value, error = parse_guess("99.9")
        assert ok is True
        assert value == 99
        assert error is None

    def test_empty_string_returns_error(self):
        ok, value, error = parse_guess("")
        assert ok is False
        assert value is None
        assert error == "Enter a guess."

    def test_none_input_returns_error(self):
        ok, value, error = parse_guess(None)
        assert ok is False
        assert value is None
        assert error == "Enter a guess."

    def test_non_numeric_string_returns_error(self):
        ok, value, error = parse_guess("abc")
        assert ok is False
        assert value is None
        assert error == "That is not a number."

    def test_mixed_alphanumeric_returns_error(self):
        ok, value, error = parse_guess("123abc")
        assert ok is False
        assert value is None
        assert error == "That is not a number."

    def test_negative_integer(self):
        ok, value, error = parse_guess("-50")
        assert ok is True
        assert value == -50
        assert error is None

    def test_negative_decimal(self):
        ok, value, error = parse_guess("-50.7")
        assert ok is True
        assert value == -50
        assert error is None

    def test_large_number(self):
        ok, value, error = parse_guess("9999999")
        assert ok is True
        assert value == 9999999
        assert error is None

    def test_zero(self):
        ok, value, error = parse_guess("0")
        assert ok is True
        assert value == 0
        assert error is None

    def test_whitespace_only_returns_error(self):
        ok, value, error = parse_guess("   ")
        assert ok is False
        assert value is None
        assert error == "That is not a number."

    def test_decimal_point_only_returns_error(self):
        ok, value, error = parse_guess(".")
        assert ok is False
        assert value is None
        assert error == "That is not a number."


# ============================================================================
# TESTS FOR GET_RANGE_FOR_DIFFICULTY
# ============================================================================


class TestGetRangeForDifficulty:
    """Comprehensive tests for get_range_for_difficulty function"""

    def test_easy_difficulty_range(self):
        low, high = get_range_for_difficulty("Easy")
        assert low == 1
        assert high == 20

    def test_normal_difficulty_range(self):
        low, high = get_range_for_difficulty("Normal")
        assert low == 1
        assert high == 50

    def test_hard_difficulty_range(self):
        low, high = get_range_for_difficulty("Hard")
        assert low == 1
        assert high == 100

    def test_unknown_difficulty_defaults_to_hard(self):
        low, high = get_range_for_difficulty("Unknown")
        assert low == 1
        assert high == 100

    def test_empty_string_defaults_to_hard(self):
        low, high = get_range_for_difficulty("")
        assert low == 1
        assert high == 100

    def test_case_sensitive_mismatch(self):
        # If difficulty is lowercase, should default to hard
        low, high = get_range_for_difficulty("easy")
        assert low == 1
        assert high == 100


# ============================================================================
# TESTS FOR UPDATE_SCORE
# ============================================================================


class TestUpdateScore:
    """Comprehensive tests for update_score function"""

    def test_perfect_game_score(self):
        # Win on first attempt = 100 points
        score = update_score(0, "Win", 1)
        assert score == 100

    def test_one_wrong_guess_deduction(self):
        # Win on second attempt (1 wrong guess) = 95 points
        score = update_score(0, "Win", 2)
        assert score == 95

    def test_multiple_wrong_guesses_deduction(self):
        # Win after 5 attempts (4 wrong guesses) = 80 points
        score = update_score(0, "Win", 5)
        assert score == 80

    def test_ten_wrong_guesses_deduction(self):
        # Win after 11 attempts (10 wrong guesses) = 50 points
        score = update_score(0, "Win", 11)
        assert score == 50

    def test_score_floor_at_zero(self):
        # If points would be negative, return 0
        score = update_score(0, "Win", 30)
        assert score == 0
        assert score >= 0

    def test_too_high_does_not_update_score(self):
        current = 50
        score = update_score(current, "Too High", 3)
        assert score == current

    def test_too_low_does_not_update_score(self):
        current = 75
        score = update_score(current, "Too Low", 2)
        assert score == current

    def test_arbitrary_loss_outcome_preserves_score(self):
        current = 100
        score = update_score(current, "Some Other Outcome", 5)
        assert score == current

    def test_win_score_calculation_formula(self):
        # Verify the formula: 100 - (5 * wrong_guesses)
        # For 6 attempts: 100 - (5 * 5) = 75
        score = update_score(0, "Win", 6)
        assert score == 75

    def test_score_with_zero_attempts(self):
        # Edge case: attempt number is 0
        score = update_score(0, "Win", 0)
        # Formula: 100 - (5 * (0 - 1)) = 100 - (-5) = 105, but clamped to 0
        assert score >= 0
