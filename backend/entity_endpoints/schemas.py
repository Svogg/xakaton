from pydantic import BaseModel


class UserAnalyticsSchema(BaseModel):
    session: int
    user_id: str
    target_region: str
    current_city: str
    target_city: str
    airplane_ticket_to: str
    airplane_ticket_back: str
    target_hotel: str
    target_restaurant: str
    target_excursion: str
    bought: int


class DataMlSchema(BaseModel):
    item_id: str
    username: str
    bought: int
