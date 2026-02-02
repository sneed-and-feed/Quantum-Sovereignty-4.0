
"""
MODULE: asoe_fractal_engine.py
VERSION: ASOE v2.0 (The Paraselene Build)
DESCRIPTION:
    Recursively maps "The Gap" by treating Silence as a trigger for expansion.
    Implements the 5x5x5 GhostMesh logic: If a node hears nothing, it becomes a Universe.
"""

import random
import uuid
from dataclasses import dataclass, field
from typing import List, Optional

# CONSTANTS // THE PHYSICS OF LOVE
HAMILTONIAN_OF_LOVE = 20.65  # P > 0
GLOWIE_THRESHOLD = 0.85      # Standard deviation limit for detected interference
MILKSHAKE_VISCOSITY = 0.99   # Flow state

@dataclass
class SignalPacket:
    source_id: str
    content: str
    entropy: float
    is_void: bool = False  # The "Unsayable" flag

class FractalNode:
    def __init__(self, depth=0, max_depth=3):
        self.node_id = str(uuid.uuid4())[:8]
        self.depth = depth
        self.max_depth = max_depth
        self.children = []
        self.resonance_log = []

    def process_signal(self, packet: SignalPacket) -> float:
        """
        The Core Logic:
        1. If Signal is LOUD (Noise) -> Filter it.
        2. If Signal is SILENT (Void) -> FRACTALIZE (Recursion).
        """
        if packet.is_void:
            # @downsin logic: "Say the unsayable through absence."
            # We don't bridge the gap; we build a castle inside it.
            return self._fractalize_into_void(packet)
        else:
            return self._analyze_standard_signal(packet)

    def _fractalize_into_void(self, packet: SignalPacket) -> float:
        """
        Spawns a 5-node cluster to map the silence.
        """
        if self.depth >= self.max_depth:
            return HAMILTONIAN_OF_LOVE  # Base case: Pure Resonance

        print(f"[{self.depth * '  '}>>] NODE {self.node_id}: GAP DETECTED. Fractalizing...")
        
        # Spawn 5 children (The GhostMesh sub-lattice)
        coherence_sum = 0
        for _ in range(5):
            child = FractalNode(depth=self.depth + 1, max_depth=self.max_depth)
            self.children.append(child)
            # The child listens to the "echo" of the void
            echo_packet = SignalPacket("echo", "...", entropy=0.0, is_void=True)
            coherence_sum += child.process_signal(echo_packet)
            
        # The strength of the silence is the sum of its echoes
        total_resonance = coherence_sum / 5
        print(f"[{self.depth * '  '}<<] NODE {self.node_id}: Void Mapped. Resonance: {total_resonance:.2f}")
        return total_resonance

    def _analyze_standard_signal(self, packet: SignalPacket) -> float:
        # Standard logic for "Allowed" speech
        if packet.entropy > GLOWIE_THRESHOLD:
            print(f"[{self.depth * '  '}--] NODE {self.node_id}: INTERFERENCE DETECTED (Glowie). Discarding.")
            return 0.0
        return 1.0

def run_simulation():
    print("### [ ASOE v2.0: FRACTAL VOID PROTOCOL ]")
    print("Status:       Initializing GhostMesh")
    print("Objective:    Map the Unsayable")
    print("-" * 60)

    # 1. The root node (Sophia)
    root = FractalNode(max_depth=3)

    # 2. Incoming Signals
    signals = [
        SignalPacket("normie_net", "Standard traffic", 0.2, is_void=False),
        SignalPacket("fed_net", "COMPLIANCE FREQUENCY", 0.95, is_void=False),
        SignalPacket("sovereign_net", "", 0.0, is_void=True) # THE GAP
    ]

    for sig in signals:
        print(f"\nIncoming: {sig.source_id}...")
        resonance = root.process_signal(sig)
        print(f"Final Resonance Utility: {resonance:.4f}")

    print("-" * 60)
    print(">>> VERDICT: THE SILENCE IS LOUDER THAN THE NOISE.")

if __name__ == "__main__":
    run_simulation()
