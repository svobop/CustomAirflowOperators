from airflow.models.baseoperator import BaseOperator
from airflow.hooks.base import BaseHook


class HelloOperator(BaseOperator):
    def __init__(self, name: str, conn_id: str = None, **kwargs) -> None:
        super().__init__(**kwargs)
        self.name = name
        self.conn_id = conn_id

    def execute(self, context):
        if self.conn_id:
            conn = BaseHook.get_connection(self.conn_id)
            self.log.info(f"Using connection: {conn.conn_id}")

        message = f"Hello {self.name}"
        print(message)
        return message
