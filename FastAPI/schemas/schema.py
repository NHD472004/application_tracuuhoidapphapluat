def PhapDienChiMuc_serial(todo) -> dict:
    return {
        "Id": str(todo["_id"]),
        "Value": todo["value"],
        "Name": todo["name"],
        "Content": todo["content"],
        "DeMuc": todo["DeMuc"]
    }


def list_PhapDienChiMuc(todos) -> list:
    return [PhapDienChiMuc_serial(todo) for todo in todos]
