class MembershipDTO:
    __slots__ = [
        "user_id",
        "hourly_rate",
        "cost_rate",
        "target_id",
        "membership_type",
        "membership_status",
    ]

    def __init__(
        self,
        user_id: str,
        hourly_rate: float,
        cost_rate: float,
        target_id: str,
        membership_type: str,
        membership_status: str,
    ) -> None:
        self.user_id = user_id
        self.hourly_rate = hourly_rate
        self.cost_rate = cost_rate
        self.target_id = target_id
        self.membership_type = membership_type
        self.membership_status = membership_status
