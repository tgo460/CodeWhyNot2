from src.ast_engine.ast_differ import ASTDiffer

def test_ast_diff():
    differ = ASTDiffer()
    # Example: test with dummy ASTs
    assert differ.diff({}, {}) == None
