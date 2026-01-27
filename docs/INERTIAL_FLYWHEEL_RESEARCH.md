# Research: The Inertial Flywheel (PID Stabilization)

**Core Concept**: A raw PLL is "reactive" (Trauma Response). A PID-Controlled PLL is "predictive" (Mastery).

## 1. The Components of Stabilization
*   **Proportional (P) - "The Clutch"**:
    *   Reacts to the *Current Error*.
    *   High P = Tight coupling, but "Grinds" on noise.
    *   Low P = Slips constantly.
*   **Integral (I) - "The Flywheel"**:
    *   Reacts to the *Accumulated Error*.
    *   **Metaphysics**: This is "Faith". It represents the momentum of the system. If the external signal (God/Earth) goes silent, the Integral term keeps the wheel spinning at the last known truth.
*   **Derivative (D) - "The Vision"**:
    *   Reacts to the *Rate of Change*.
    *   **Metaphysics**: This is "Prophecy". It sees the drift before it becomes an error and applies a counter-force.

## 2. Tuning for Biological Resonance
*   **Critical Damping ($\zeta = 1.0$)**:
    *   We do not want the brain to oscillate (ring) around the Earth frequency.
    *   We want it to slide smoothly into lock and stay there.
    *   **Implication**: We need a strong **D** term to dampen the **P** term's reactivity.

## Implementation Strategy (`harmonic_gearbox.py`)
*   Upgrade `HarmonicGearbox` to `PIDHarmonicGearbox`.
*   **Coefficients**:
    *   $K_p = 0.5$ (Responsive)
    *   $K_i = 0.05$ (Slow build up of Faith)
    *   $K_d = 0.1$ (Smoothing the jolt)
*   **Equation**:
    $$ u(t) = K_p e(t) + K_i \int e(t) dt + K_d \frac{de(t)}{dt} $$
