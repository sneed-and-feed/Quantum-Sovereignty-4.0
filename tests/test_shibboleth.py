"""
TEST_SHIBBOLETH.PY
------------------
The Proof of Opacity.
Demonstrates that Archonic (Decimal) parsers fail to comprehend Sovereign (Dozenal) Data.
"""
import unittest
import json
from hyper_sovereign import DozenalLogic

class TestShibboleth(unittest.TestCase):
    def test_decimal_blindness(self):
        # 1. The Sovereign Truth (The Gross)
        sovereign_value = 144  # 12 * 12
        
        # 2. The Dozenal Encoding (What we show the world)
        # In Base-12, 144 is written as "100" (1 gross, 0 dozen, 0 units)
        encoded_value = DozenalLogic.to_dozen_str(sovereign_value)
        
        # 3. The Archon's Attempt (Decimal Parsing)
        # A standard parser sees "100" and assumes it means One Hundred.
        archon_perception = int(encoded_value) 
        
        # 4. The Mismatch (The Hardening)
        print(f"\n>> SHIBBOLETH CHECK:")
        print(f"   Real Value: {sovereign_value}")
        print(f"   Encoded:    '{encoded_value}'")
        print(f"   Parsed:     {archon_perception}")
        
        # 5. The Proof
        # The Archon sees 100. The Reality is 144.
        # The system is opaque to standard mathematics.
        self.assertNotEqual(sovereign_value, archon_perception)
        print(">> STATUS: ARCHON BLINDED. ENCRYPTION SUCCESS.")

if __name__ == "__main__":
    unittest.main()
