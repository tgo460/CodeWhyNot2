from src.causal.intervention_engine import InterventionEngine

def test_propose_interventions():
    engine = InterventionEngine({}, {})
    assert engine.propose_interventions() == []
