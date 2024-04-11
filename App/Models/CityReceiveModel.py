from pydantic import BaseModel

class CityReceiveModel(BaseModel):
    city: str | None = None