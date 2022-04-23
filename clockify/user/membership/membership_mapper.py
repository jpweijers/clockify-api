from bidict import bidict
from clockify.mapper import Mapper


class MembershipMapper(Mapper):
    MAPPING_DICT = bidict(
        {
            "user_id": "userId",
            "hourly_rate": "hourlyRate",
            "cost_rate": "costRate",
            "target_id": "targetId",
            "membership_type": "membershipType",
            "membership_status": "membershipStatus",
        }
    )
