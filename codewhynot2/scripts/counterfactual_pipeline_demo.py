from dotenv import load_dotenv
load_dotenv()

from src.models.llm_wrapper import get_llm
from src.utils.config_loader import LLMConfig
from src.ast_engine.ast_parser import ASTParser
from src.ast_engine.ast_differ import ASTDiffer
from src.scoring.fidelity_metrics import FidelityScorer

# 1. User prompt
original_prompt = "Write a Python function that adds two numbers."

# 2. Get LLM (Hugging Face API)
config = LLMConfig(type="huggingface_api", model_name="bigcode/starcoder2-3b")
llm = get_llm(config)

# 3. Generate original code
original_code = llm.generate(original_prompt)
print("Original code:\n", original_code)

# 4. Simulate a counterfactual prompt (for demo, just add 'with type hints')
counterfactual_prompt = original_prompt + " with type hints"
counterfactual_code = llm.generate(counterfactual_prompt)
print("\nCounterfactual code:\n", counterfactual_code)

# 5. Parse both codes into ASTs
parser = ASTParser()
original_ast = parser.parse(original_code, language="python")
counterfactual_ast = parser.parse(counterfactual_code, language="python")

# 6. Compute AST diff
differ = ASTDiffer()
ast_diff = differ.diff(original_ast, counterfactual_ast)
print("\nAST diff:", ast_diff)

# 7. Compute fidelity score
scorer = FidelityScorer()
score = scorer.calculate_score(ast_diff, original_code, counterfactual_code)
print("\nFidelity score:", score)
