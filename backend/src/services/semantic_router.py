from src.utils.constants import RouteCategory, Role


class SemanticRouter:
    def __init__(self):
        pass

    def initialize(self):
        pass

    def get_route(self, query: str, role: Role) -> RouteCategory:
        return RouteCategory.SQL
