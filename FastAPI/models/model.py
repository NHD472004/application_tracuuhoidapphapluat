from pydantic import BaseModel, Field, ConfigDict
from bson import ObjectId


class PhapDienChiMuc_model(BaseModel):
    _id = dict[str, str]
    value: str = Field(...)
    name: str = Field(...)
    content: str = Field(...)
    DeMuc: str = Field(...)
    
    model_config = ConfigDict(
        populate_by_name=True,
        arbitrary_types_allowed=True,
        json_schema_extra={
            "example": {
                "Value": "1000100000000000100000100000000000000000",
                "Name": "Điều 10.1.NĐ.1. Phạm vi điều chỉnh",
                "Content": "Nghị định này quy định các hoạt động về công tác dân tộc nhằm đảm bảo và thúc đẩy sự bình đẳng, đoàn kết, tương trợ giúp nhau cùng phát triển, tôn trọng và giữ gìn bản sắc văn hóa của các dân tộc cùng chung sống trên lãnh thổ nước Cộng hòa xã hội chủ nghĩa Việt Nam.",
                "DeMuc": "049522e0-fec2-4d52-916d-dd103ba69627"
            }
        },
    )
    
    
class update_PhapDienChiMuc_model(BaseModel):
    value: str | None = None
    name: str | None = None
    content: str | None = None
    DeMuc: str | None = None
    
    model_config = ConfigDict(
        arbitrary_types_allowed=True,
        json_encoders={ObjectId: str},
        json_schema_extra={
            "example": {
                "Value": "1000100000000000100000100000000000000000",
                "Name": "Điều 10.1.NĐ.1. Phạm vi điều chỉnh",
                "Content": "Nghị định này quy định các hoạt động về công tác dân tộc nhằm đảm bảo và thúc đẩy sự bình đẳng, đoàn kết, tương trợ giúp nhau cùng phát triển, tôn trọng và giữ gìn bản sắc văn hóa của các dân tộc cùng chung sống trên lãnh thổ nước Cộng hòa xã hội chủ nghĩa Việt Nam.",
                "DeMuc": "049522e0-fec2-4d52-916d-dd103ba69627"
            }
        },
    )