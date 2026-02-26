
from utils import db_utils
from utils.db_utils import DBUtils


def test_db():
    DBUtils.get_connection()
    rows = DBUtils.execute_query("select * from employee_salary")
    i=1
    for row in rows:
        print(row)
        assert row[0] == i
        i+=1
    assert len(rows).__eq__(13)
    assert rows[12][1] == "siva"
