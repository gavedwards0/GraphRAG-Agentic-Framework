from typing import List, Dict, Any

class GraphEngine:
    """Base interface for Knowledge Graph interaction."""
    def get_neighbors(self, entity_id: str) -> List[Dict[str, Any]]:
        raise NotImplementedError

    def get_path(self, start_entity: str, end_entity: str) -> List[Dict[str, Any]]:
        raise NotImplementedError

class MockBiomedicalGraph(GraphEngine):
    """A simulated Knowledge Graph for biomedical entities."""
    def __init__(self):
        self.graph_data = {
            "Drug_A": [
                {"relation": "targets", "entity": "Gene_X"},
                {"relation": "associated_with", "entity": "Pathway_1"}
            ],
            "Gene_X": [
                {"relation": "regulates", "entity": "Phenotype_Z"},
                {"relation": "interacts_with", "entity": "Gene_Y"}
            ],
            "Pathway_1": [
                {"relation": "influences", "entity": "Phenotype_Z"}
            ]
        }

    def get_neighbors(self, entity_id: str) -> List[Dict[str, Any]]:
        """Returns neighboring nodes for a given entity."""
        return self.graph_data.get(entity_id, [])

    def get_path(self, start_entity: str, end_entity: str) -> List[Dict[str, Any]]:
        """Simulates finding a path between two entities."""
        # Simple hardcoded path for demonstration
        if start_entity == "Drug_A" and end_entity == "Phenotype_Z":
            return [
                {"step": 1, "node": "Drug_A", "relation": "targets", "next_node": "Gene_X"},
                {"step": 2, "node": "Gene_X", "relation": "regulates", "next_node": "Phenotype_Z"}
            ]
        return []
