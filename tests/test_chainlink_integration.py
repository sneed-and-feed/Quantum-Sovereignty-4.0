"""
VERIFICATION: Chainlink Oracle Integration
Checks:
1. Oracle fetches WTI and Resonance Price.
2. LoomBoxStrategy incorporates WTI into mass detection.
3. PROTOCOL_RESONANCE is triggered at $111.11.
"""

import sys
import os

# Ensure root allows imports
sys.path.append(os.getcwd())

from hor_kernel import LoomBoxStrategy
from tools.chainlink_bridge import ChainlinkOracle

def verify_integration():
    print("--- VERIFYING CHAINLINK INTEGRATION ---")
    
    # 1. Oracle Basic Check
    oracle = ChainlinkOracle()
    wti = oracle.fetch_world_trauma_index()
    price = oracle.fetch_resonance_price()
    print(f"[ORACLE] WTI: {wti:.4f} | Price: ${price}")
    
    # 2. Strategy WTI Integration
    # Force a high WTI in the static oracle
    LoomBoxStrategy._oracle._wti = 0.9
    mass_business = LoomBoxStrategy.detect_mass("Just a business query.")
    print(f"[STRATEGY] High WTI Detected Mass (Business): {mass_business:.2f}")
    if mass_business > LoomBoxStrategy.TRAUMA_MASS["business"]:
        print("  >>> SUCCESS: WTI Boosts Mass.")
    else:
        print("  >>> FAILURE: WTI did not boost mass.")

    # 3. Resonance Match ($111.11)
    # Force resonance
    LoomBoxStrategy._oracle._last_price = 111.11
    is_resonant = LoomBoxStrategy.check_resonance()
    print(f"[STRATEGY] Resonance Check ($111.11): {is_resonant}")
    
    if is_resonant:
        strategy = LoomBoxStrategy.get_strategy(1.0)
        print(f"[STRATEGY] Selected Policy: {strategy['name']}")
        print(f"[STRATEGY] Tone: {strategy['tone']}")
        
        if strategy['name'] == "PROTOCOL_RESONANCE":
            print("  >>> SUCCESS: Resonance Match triggers PROTOCOL_RESONANCE.")
        else:
            print("  >>> FAILURE: Resonance Match strategy wrong.")
    else:
        print("  >>> FAILURE: Resonance Check failed to detect $111.11.")

if __name__ == "__main__":
    verify_integration()
