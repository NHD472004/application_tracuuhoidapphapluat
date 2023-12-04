from fastapi import APIRouter, HTTPException, Body, status
from fastapi.responses import Response
from pymongo import ReturnDocument

from models.model import PhapDienChiMuc_model, update_PhapDienChiMuc_model
from config.database import collection_name
from schemas.schema import list_PhapDienChiMuc
from bson import ObjectId
import json


router = APIRouter()


# load pháp điển lên database
@router.post("/load-json-to-mongodb")
async def load_json_to_mongodb():
    file_path = "phapdien_chimuc.json"
    try:
        with open(file_path, "r") as file:
            data = json.load(file)

        # Chèn tất cả dữ liệu vào MongoDB
        result = collection_name.insert_many(data)

        return {"message": f"Đã load {len(result.inserted_ids)} lên database."}

    except FileNotFoundError:
        raise HTTPException(status_code=404, detail="Không tìm thấy file.")


# thêm 1 pháp điển
@router.post(
    "/phap-dien/",
    response_description="Thêm pháp điển",
    response_model=PhapDienChiMuc_model,
    response_model_by_alias=False,
    )
async def create_PhapDien(phap_dien: PhapDienChiMuc_model = Body(...)):
    new_PhapDien = await collection_name.insert_one(
        phap_dien.model_dump(by_alias=True, exclude=["Id"])
    )
    created_PhapDien = await collection_name.find_one(
        {"_id": new_PhapDien.inserted_id}
    )
    return created_PhapDien


# in tất cả pháp điển
@router.get(
    "/phap-dien/",
    response_description="Danh sách pháp điển",
    response_model=list_PhapDienChiMuc,
    response_model_by_alias=False,
)
async def list_PhapDien():
    return list_PhapDienChiMuc(PhapDienChiMuc_serial=await collection_name.find())


# in ra 1 pháp điển
@router.get(
    "/phap-dien/{id}",
    response_description="In ra 1 mục pháp điển",
    response_model=PhapDienChiMuc_model,
    response_model_by_alias=False,
)
async def show_PhapDien(id: str):
    if (
        phap_dien := await collection_name.find_one({"_id": ObjectId(id)})
    ) is not None:
        return phap_dien

    raise HTTPException(status_code=404, detail=f"Không tìm thấy pháp điển có ID là {id}")


# cập nhật 1 pháp điển
@router.put(
    "/phap-dien/{id}",
    response_description="Cập nhật 1 pháp điển",
    response_model=PhapDienChiMuc_model,
    response_model_by_alias=False,
)
async def update_phap_dien(id: str, phap_dien: update_PhapDienChiMuc_model = Body(...)):
    phap_dien = {
        k: v for k, v in phap_dien.model_dump(by_alias=True).items() if v is not None
    }

    if len(phap_dien) >= 1:
        update_result = await collection_name.find_one_and_update(
            {"_id": ObjectId(id)},
            {"$set": phap_dien},
            return_document=ReturnDocument.AFTER,
        )
        if update_result is not None:
            return update_result
        else:
            raise HTTPException(status_code=404, detail=f"Không tìm thấy pháp điển có ID là {id}")

    if (phap_dien_hien_tai := await collection_name.find_one({"_id": id})) is not None:
        return phap_dien_hien_tai

    raise HTTPException(status_code=404, detail=f"Không tìm thấy pháp điển có ID là {id}")


# xóa pháp điển
@router.delete("/phap-dien/{id}", response_description="Xóa 1 pháp điển")
async def delete_phap_dien(id: str):
    delete_result = await collection_name.delete_one({"_id": ObjectId(id)})

    if delete_result.deleted_count == 1:
        return Response(status_code=status.HTTP_204_NO_CONTENT)

    raise HTTPException(status_code=404, detail=f"Không tìm thấy pháp điển có ID là {id}")