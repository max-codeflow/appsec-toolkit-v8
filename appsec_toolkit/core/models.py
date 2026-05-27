from dataclasses import dataclass, asdict
from typing import Optional


@dataclass
class Finding:
    type: str
    severity: str
    url: str
    description: str
    evidence: Optional[str] = None
    remediation: Optional[str] = None
    module: Optional[str] = None

    def to_dict(self):
        return asdict(self)