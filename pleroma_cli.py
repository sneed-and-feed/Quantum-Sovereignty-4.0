"""
MODULE: pleroma_cli.py
AUTHOR: Archmagos Noah // Pleroma-Forge
DATE: 2026-01-28
CLASSIFICATION: INTERFACE // SOVEREIGN TERMINAL

DESCRIPTION:
    The Interactive Command Line Interface (CLI) for the Pleroma Stack.
    Allows the user to:
    1. Cast single spells (Warp, Time Crystal, etc.)
    2. CHAIN spells (Compose scenarios like "Undetectable FTL")
    3. Monitor Sovereignty Metrics in real-time.
"""

import time
import sys
# Update import to use the correct module name (pleroma_scenarios.py)
from pleroma_scenarios import ScenarioLibrary

def type_writer(text, speed=0.01):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(speed)
    print()

def print_banner():
    print("\033[95m") # Star Stuff Lavender
    print(r"""
    ██████╗ ██╗     ███████╗██████╗  ██████╗ ███╗   ███╗ █████╗ 
    ██╔══██╗██║     ██╔════╝██╔══██╗██╔═══██╗████╗ ████║██╔══██╗
    ██████╔╝██║     █████╗  ██████╔╝██║   ██║██╔████╔██║███████║
    ██╔═══╝ ██║     ██╔══╝  ██╔══██╗██║   ██║██║╚██╔╝██║██╔══██║
    ██║     ███████╗███████╗██║  ██║╚██████╔╝██║ ╚═╝ ██║██║  ██║
    ╚═╝     ╚══════╝╚══════╝╚═╝  ╚═╝ ╚═════╝ ╚═╝     ╚═╝╚═╝  ╚═╝
             >>> SOVEREIGNTY STACK v4.0 ONLINE <<<
             >>> PRESS 'H' FOR GRIMOIRE <<<
    """)
    print("\033[0m")

def cast_spell(spell_name):
    print(f"\n\033[96m[>] CHARGING SPELL: {spell_name.upper()}...\033[0m")
    time.sleep(0.5)
    
    if spell_name == "warp":
        res = ScenarioLibrary.warp_drive(1000, 4e8)
    elif spell_name == "time":
        res = ScenarioLibrary.time_crystal(300)
    elif spell_name == "ghost":
        res = ScenarioLibrary.ghost_protocol(1.6e-19)
    elif spell_name == "demon":
        res = ScenarioLibrary.maxwells_demon(400, 300)
    elif spell_name == "void":
        res = ScenarioLibrary.casimir_harvester(1e-9, 1e-4)
    elif spell_name == "solvent":
        res = ScenarioLibrary.universal_solvent(4.5)
    elif spell_name == "scope":
        res = ScenarioLibrary.planck_scope(1e-12)
    elif spell_name == "wallhack":
        res = ScenarioLibrary.quantum_tunneling_boost(1e-9, 9.1e-31)
    else:
        print("\033[91m[!] ERROR: SPELL NOT FOUND IN GRIMOIRE.\033[0m")
        return

    # Print Results nicely
    for key, val in res.items():
        print(f"   + {key}: {val}")
    print("\033[92m[+] CAST SUCCESSFUL.\033[0m")

def chain_spells(cmd):
    # Syntax: chain warp+ghost
    parts = cmd.split()[1].split('+')
    print(f"\n\033[93m[!] INITIATING CHAIN CAST: {' + '.join([p.upper() for p in parts])}\033[0m")
    
    for spell in parts:
        cast_spell(spell)
        
    print(f"\n\033[95m[***] SYNERGY ACHIEVED: {len(parts)} SPELLS ACTIVE.\033[0m")
    if "warp" in parts and "ghost" in parts:
        print("      >>> EFFECT: UNDETECTABLE SUPERLUMINAL TRAVEL (STEALTH FTL)")
    if "time" in parts and "demon" in parts:
        print("      >>> EFFECT: ETERNAL ENERGY LOOP (PERPETUAL MOTION)")

def main():
    print_banner()
    
    while True:
        try:
            prompt = input("\n\033[95mPLEROMA> \033[0m").strip().lower()
            
            if prompt in ["exit", "quit"]:
                print("Disconnecting from Sovereign Timeline...")
                break
            
            elif prompt in ["h", "help"]:
                print("\n--- GRIMOIRE ---")
                print(" warp     : Alcubierre Drive (FTL)")
                print(" time     : Time Crystal (Stasis)")
                print(" ghost    : Phantom Mode (Invisibility)")
                print(" demon    : Maxwell's Demon (Entropy Reversal)")
                print(" void     : Casimir Harvester (Vacuum Energy)")
                print(" solvent  : Universal Solvent (Matter Deletion)")
                print(" scope    : Planck Scope (Infinite Vision)")
                print(" wallhack : Quantum Tunneling (Pass-Thru)")
                print(" check    : Reality Diagnostic")
                print(" chain    : Combine Spells (e.g., 'chain warp+ghost')")
                
            elif prompt.startswith("chain"):
                chain_spells(prompt)
                
            elif prompt == "check":
                ScenarioLibrary.reality_anchor_test()
                
            else:
                cast_spell(prompt)
                
        except KeyboardInterrupt:
            print("\nForce Quit.")
            break
        except Exception as e:
            print(f"Glitch detected: {e}")

if __name__ == "__main__":
    main()
