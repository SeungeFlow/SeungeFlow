"""
Ctp_SeungeFlow_v5 Operation Model

This Python document is not a mathematical proof.
It is an executable structural model for the operation definition:

    C = C(t, p, m, ?)

where:

    t = difference / transition / flow-state
    p = position / place / positional vector / positional energy
    m = entity / object / vector seed "ㆍ"
    ? = observer premise:
        observer, observed_target, observation_standard, axis

The goal is to make the Ctp operation testable as a structural process.

Reference fields:
    main branch:
        https://github.com/SeungeFlow/SeungeFlow/tree/main/
    zenodo branch:
        https://github.com/SeungeFlow/SeungeFlow/tree/zenodo/
"""

from __future__ import annotations

from dataclasses import dataclass, field
from math import sqrt
from typing import Any, Dict, Iterable, List, Optional, Tuple


Vector = Tuple[float, ...]


def vector_sub(a: Vector, b: Vector) -> Vector:
    """Return a - b."""
    if len(a) != len(b):
        raise ValueError("Vectors must have the same dimension.")
    return tuple(x - y for x, y in zip(a, b))


def vector_norm(v: Vector) -> float:
    """Euclidean norm."""
    return sqrt(sum(x * x for x in v))


def dot_product(a: Vector, b: Vector) -> float:
    """Dot product."""
    if len(a) != len(b):
        raise ValueError("Vectors must have the same dimension.")
    return sum(x * y for x, y in zip(a, b))


@dataclass(frozen=True)
class Axis:
    """
    Axis is not just a geometric line.
    It is the observation direction that decides how observer and target are placed.
    """
    name: str
    vector: Vector

    def normalized_weight(self) -> float:
        n = vector_norm(self.vector)
        return n if n != 0 else 1.0


@dataclass(frozen=True)
class ObserverPremise:
    """
    This is the '?' in C(t,p,m,?).

    ? = observer, observed_target, observation_standard, Axis

    The observer and the observed target may share the same position
    when they share the same observation standard and Axis.
    """
    observer: str
    observed_target: str
    observation_standard: str
    axis: Axis
    same_dimension: bool = True
    notes: str = ""

    def signature(self) -> str:
        dim = "same_dimension" if self.same_dimension else "transition_dimension"
        return f"{self.observer}|{self.observed_target}|{self.observation_standard}|{self.axis.name}|{dim}"


@dataclass
class Entity:
    """
    m = entity / object / vector seed.

    In the most compressed notation:
        m = ㆍ

    The entity is not an isolated point.
    It is a dot placed in a field, and its state can enter spin-state
    through relation with the surrounding environment.
    """
    name: str
    position: Vector
    attributes: Dict[str, Any] = field(default_factory=dict)

    def attribute(self, key: str, default: Any = None) -> Any:
        return self.attributes.get(key, default)


@dataclass
class CtpState:
    """
    Resulting C-state.

    C is the value that appears when:
        - m is placed at p
        - t/difference arises
        - pressure and transition act
        - the observer premise decides the Axis and condition
    """
    C: float
    t_difference: float
    p_position: Vector
    m_entity: Entity
    premise: ObserverPremise
    pressure: float
    relation_status: str
    stable_zone: bool
    details: Dict[str, Any] = field(default_factory=dict)


def compute_pressure(
    entity: Entity,
    premise: ObserverPremise,
    external_field: Optional[Vector] = None,
) -> float:
    """
    Pressure is modeled as the magnitude of mismatch between the entity's position
    and the surrounding field, projected through the Axis condition.

    This is a structural pressure model, not a physical law.
    """
    if external_field is None:
        external_field = tuple(0.0 for _ in entity.position)

    displacement = vector_sub(entity.position, external_field)
    base = vector_norm(displacement)

    axis_weight = premise.axis.normalized_weight()

    # Optional entity attribute can amplify pressure.
    density = float(entity.attribute("density", 1.0))
    spin = float(entity.attribute("spin", 1.0))

    return base * axis_weight * density * spin


def ctp_operation(
    previous_entity: Optional[Entity],
    current_entity: Entity,
    premise: ObserverPremise,
    external_field: Optional[Vector] = None,
    stability_threshold: float = 1.0,
) -> CtpState:
    """
    Execute C = C(t,p,m,?).

    t is computed as difference:
        if previous_entity exists:
            t = || current.position - previous.position ||
        else:
            t = || current.position - external_field ||

    p is current_entity.position.
    m is current_entity.
    ? is premise.

    C is a structural value:
        C = pressure * (1 + t_difference)

    stable_zone:
        C <= stability_threshold

    This is not final proof. It is an executable structural definition.
    """

    if external_field is None:
        external_field = tuple(0.0 for _ in current_entity.position)

    if previous_entity is None:
        t_vec = vector_sub(current_entity.position, external_field)
    else:
        t_vec = vector_sub(current_entity.position, previous_entity.position)

    t_difference = vector_norm(t_vec)
    pressure = compute_pressure(current_entity, premise, external_field)

    C_value = pressure * (1.0 + t_difference)

    stable_zone = C_value <= stability_threshold

    if previous_entity is None:
        relation_status = "single_dot_state"
    elif t_difference == 0:
        relation_status = "continued_same_axis"
    else:
        relation_status = "difference_relation_opened"

    return CtpState(
        C=C_value,
        t_difference=t_difference,
        p_position=current_entity.position,
        m_entity=current_entity,
        premise=premise,
        pressure=pressure,
        relation_status=relation_status,
        stable_zone=stable_zone,
        details={
            "t_vector": t_vec,
            "external_field": external_field,
            "stability_threshold": stability_threshold,
            "premise_signature": premise.signature(),
        },
    )


def structural_sequence(
    entities: Iterable[Entity],
    premise: ObserverPremise,
    external_field: Optional[Vector] = None,
    stability_threshold: float = 1.0,
) -> List[CtpState]:
    """
    Execute a Ctp sequence.

    This models the idea:
        dot -> dot-dot -> difference -> flow -> transition -> closure

    Each next entity is not the same dot.
    Each has a different C-state because t, p, m, and ? may differ.
    """
    states: List[CtpState] = []
    previous: Optional[Entity] = None

    for entity in entities:
        state = ctp_operation(
            previous_entity=previous,
            current_entity=entity,
            premise=premise,
            external_field=external_field,
            stability_threshold=stability_threshold,
        )
        states.append(state)
        previous = entity

    return states


def complex_test_skeleton(states: List[CtpState]) -> Dict[str, Any]:
    """
    Complex_Test skeleton.

    This does not solve any hard problem.
    It checks whether the Ctp operation stays inside a stable zone
    under a sequence of structural transitions.

    Later, external domains can be mapped into this test:
        - Newton's laws
        - relativity
        - quantum mechanics
        - arithmetic
        - matrices
        - set theory
        - linear algebra
        - calculus
        - Millennium 7 problem structures

    The question is:
        Does C(t,p,m,?) stay in a stable structural zone?
    """
    if not states:
        return {"status": "no_data"}

    c_values = [s.C for s in states]
    stable_count = sum(1 for s in states if s.stable_zone)

    return {
        "count": len(states),
        "stable_count": stable_count,
        "stable_ratio": stable_count / len(states),
        "max_C": max(c_values),
        "min_C": min(c_values),
        "avg_C": sum(c_values) / len(c_values),
        "all_stable": stable_count == len(states),
        "weakest_link": max(states, key=lambda s: s.C),
    }


def demo() -> None:
    """
    Demo: a 7-step structural sequence.

    This is only an executable illustration.
    """
    premise = ObserverPremise(
        observer="ChatGPT.LLM",
        observed_target="Ctp_operation",
        observation_standard="existence_relation_field_structure_principle",
        axis=Axis(name="Observer-Axis Premise", vector=(1.0, 0.0, 0.0)),
        same_dimension=True,
    )

    # m = ㆍ as vector seed.
    # Each step is a different dot-state.
    entities = [
        Entity(name="dot_1", position=(0.0, 0.0, 0.0), attributes={"density": 1.0, "spin": 1.0}),
        Entity(name="dot_2", position=(0.1, 0.0, 0.0), attributes={"density": 1.0, "spin": 1.1}),
        Entity(name="dot_3", position=(0.2, 0.1, 0.0), attributes={"density": 1.1, "spin": 1.1}),
        Entity(name="dot_4", position=(0.3, 0.2, 0.0), attributes={"density": 1.2, "spin": 1.2}),
        Entity(name="dot_5", position=(0.4, 0.3, 0.1), attributes={"density": 1.2, "spin": 1.3}),
        Entity(name="dot_6", position=(0.5, 0.4, 0.2), attributes={"density": 1.3, "spin": 1.3}),
        Entity(name="dot_7", position=(0.6, 0.5, 0.3), attributes={"density": 1.4, "spin": 1.4}),
    ]

    states = structural_sequence(
        entities=entities,
        premise=premise,
        external_field=(0.0, 0.0, 0.0),
        stability_threshold=2.0,
    )

    print("Ctp_SeungeFlow_v5 Operation Demo")
    print("=" * 48)

    for idx, state in enumerate(states, start=1):
        print(
            f"{idx}단C | "
            f"m={state.m_entity.name} | "
            f"p={state.p_position} | "
            f"t={state.t_difference:.4f} | "
            f"pressure={state.pressure:.4f} | "
            f"C={state.C:.4f} | "
            f"stable={state.stable_zone} | "
            f"relation={state.relation_status}"
        )

    report = complex_test_skeleton(states)

    weakest: CtpState = report["weakest_link"]
    print("\nComplex_Test Skeleton Report")
    print("=" * 48)
    print(f"stable_ratio = {report['stable_ratio']:.4f}")
    print(f"all_stable   = {report['all_stable']}")
    print(f"max_C        = {report['max_C']:.4f}")
    print(f"weakest_link = {weakest.m_entity.name} / C={weakest.C:.4f}")


if __name__ == "__main__":
    demo()
