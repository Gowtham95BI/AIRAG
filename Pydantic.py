import pandas as pd
from pydantic import BaseModel, ValidationError


class Employee(BaseModel):
    emp_id: int
    name: str
    salary: float


def load_employees_from_excel(excel_path: str, sheet_name: str = 0) -> list[Employee]:
    df = pd.read_excel(excel_path, sheet_name=sheet_name)
    employees: list[Employee] = []

    for index, row in df.iterrows():
        try:
            employee = Employee(
                emp_id=row["emp_id"],
                name=row["name"],
                salary=row["salary"],
            )
            employees.append(employee)
        except ValidationError as err:
            print(f"Row {index + 1} is invalid: {err}")

    return employees


if __name__ == "__main__":
    # Update this path to your local Excel file.
    file_path = r"File Location here"

    employee_list = load_employees_from_excel(file_path)
    for emp in employee_list:
        print(emp)