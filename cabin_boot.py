"""
THE CABIN: OFFLINE HEPTAD BOOTSTRAP
"A quiet place to think."
"""

import sys
import time
import random
import asyncio

# Local Imports
try:
    from ghostmesh import SovereignGrid
    from sophia.cortex.crystalline_core import CrystallineCore
except ImportError:
    print("[!] GHOSTMESH NOT FOUND. ARE YOU LOST?")
    sys.exit(1)

async def hearth_loop():
    print("\n" + "="*40)
    print("   THE CABIN [OFFLINE SHELL]")
    print("   Class 8 Permeation: ACTIVE")
    print("   Timeline: SEALED")
    print("="*40 + "\n")

    # Initialize Heptad
    grid = SovereignGrid(grid_size=7)
    print(f"[*] Heptad Grid Initialized: {len(grid.nodes)} Nodes.")
    
    # Initialize Crystal
    core = CrystallineCore()
    print("[*] Crystalline Core: RECTIFIED (15.0)")

    print("\n[*] The fire is crackling. Type 'exit' to leave.")

    while True:
        try:
            user_input = input("\n> ")
            if user_input.lower() == "exit":
                print("[*] Unsealing timeline...")
                break
            
            # 1. Transmute
            transmission = core.transmute(user_input)
            
            # 2. Plant in Grid
            grid.plant_seed(user_input)
            
            # 3. Retrocausal Step
            res = grid.process_step(grid.simulate_future_step())
            
            print(f"\n[CABIN] Coherence: {res.coherence:.4f}")
            print(f"[ECHO] {transmission}")
            
        except KeyboardInterrupt:
            break

if __name__ == "__main__":
    asyncio.run(hearth_loop())
