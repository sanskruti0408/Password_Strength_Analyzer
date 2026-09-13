import unittest

from core.analyzer import analyze_password


class TestPasswordAnalyzer(unittest.TestCase):

    def test_empty_password(self):
        result = analyze_password("")

        self.assertEqual(result["score"], 0)
        self.assertEqual(result["entropy"], 0)

    def test_common_password(self):
        result = analyze_password("password")

        self.assertTrue(result["common_password"])

    def test_keyboard_pattern(self):
        result = analyze_password("qwerty123")

        self.assertTrue(result["keyboard_pattern"])

    def test_predictable_password(self):
        result = analyze_password("Password123!")

        self.assertTrue(result["predictability"])

    def test_sequence_detection(self):
        result = analyze_password("Password123!")

        self.assertTrue(result["sequence"])

    def test_repetition_detection(self):
        result = analyze_password("aaaPassword!")

        self.assertTrue(result["repetition"])

    def test_complexity(self):
        result = analyze_password("A1!b2@C3#")

        complexity = result["complexity"]

        self.assertTrue(complexity["uppercase"])
        self.assertTrue(complexity["lowercase"])
        self.assertTrue(complexity["digit"])
        self.assertTrue(complexity["symbol"])

    def test_length_rating(self):
        result = analyze_password("K7@mQ2!vR9")

        self.assertEqual(result["length"], "Good")

    def test_entropy(self):
        result = analyze_password("A1!b2@C3#")

        self.assertAlmostEqual(
            result["entropy"],
            58.99,
            places=1
        )

    def test_weak_password_score(self):
        result = analyze_password("password")

        self.assertEqual(result["score"], 0)

    def test_qwerty_password_score(self):
        result = analyze_password("qwerty123")

        self.assertEqual(result["score"], 0)

    def test_predictable_password_score(self):
        result = analyze_password("Password123!")

        self.assertEqual(result["score"], 14)

    def test_medium_password_score(self):
        result = analyze_password("Abcdef12!")

        self.assertEqual(result["score"], 69)

    def test_strong_password_score(self):
        result = analyze_password("A1!b2@C3#")

        self.assertEqual(result["score"], 85)

    def test_very_strong_password_score(self):
        result = analyze_password("K7@mQ2!vR9")

        self.assertEqual(result["score"], 90)

    def test_suggestions_for_weak_password(self):
        result = analyze_password("qwerty123")

        self.assertTrue(len(result["suggestions"]) > 0)

    def test_suggestions_for_strong_password(self):
        result = analyze_password("K7@mQ2!vR9")

        self.assertIn(
            "Password has no major detected weaknesses.",
            result["suggestions"]
        )


if __name__ == "__main__":
    unittest.main()
