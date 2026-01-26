import unittest
from hyper_sovereign import DozenalLogic

class TestShibboleth(unittest.TestCase):
    
    def test_cycle_of_return(self):
        """Verifies the Cycle of Return via the Sovereign API."""
        original_v = 144
        encoded = DozenalLogic.to_dozen_str(original_v)
        decoded = DozenalLogic.from_dozen_str(encoded)
        self.assertEqual(original_v, decoded)

    def test_void_rejection(self):
        """Verifies the system rejects The Void (Empty/Whitespace)."""
        with self.assertRaisesRegex(ValueError, "VOID ERROR"):
            DozenalLogic.from_dozen_str("")
        with self.assertRaisesRegex(ValueError, "VOID ERROR"):
            DozenalLogic.from_dozen_str("   ")

    def test_shadow_handling(self):
        """Verifies handling of Negative Sovereign States."""
        self.assertEqual(DozenalLogic.to_dozen_str(-10), "-X")
        self.assertEqual(DozenalLogic.from_dozen_str("-X"), -10)
        
        # Test malformed shadow
        with self.assertRaisesRegex(ValueError, "FORMAT ERROR"):
            DozenalLogic.from_dozen_str("-")

    def test_archon_crash(self):
        """Verifies standard Int() crashes on Sovereign Glyphs."""
        with self.assertRaises(ValueError):
            int("1E") # 1 dozen + 11 = 23

if __name__ == "__main__":
    unittest.main()
