"""GNUCash Account Hierarchy Template Object"""


class GAHTO:
    """GNUCash Hierarchy Account Template Object main class"""

    def export(self: "GAHTO", path: str) -> bool:
        """Exports the GAHTO object to an XML file at path"""
        _ = path
        return False

    def add_account(self: "GAHTO", account_name: str) -> None:
        """Adds an account to the GAHTO object"""
