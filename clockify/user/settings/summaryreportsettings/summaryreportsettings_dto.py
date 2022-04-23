class SummaryreportsettingsDTO:
    __slots__ = [
        "group",
        "subgroup",
    ]

    def __init__(
        self,
        group: str,
        subgroup: str,
    ) -> None:
        self.group = group
        self.subgroup = subgroup
