import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.agent import GraphRAGAgent
from src.graph_engine import MockBiomedicalGraph

def main():
    print("Initializing Biomedical Knowledge Graph Engine...\n")
    engine = MockBiomedicalGraph()
    
    print("Initializing GraphRAG Agent (Simulated GPT-4)...\n")
    agent = GraphRAGAgent(llm_model="gpt-4", graph_engine=engine)
    
    query = "What is the mechanism of action connecting Drug_A to Phenotype_Z?"
    print(f"User Query: {query}\n")
    
    result = agent.run_query(query)
    print(f"\n{result}\n")

if __name__ == "__main__":
    main()
