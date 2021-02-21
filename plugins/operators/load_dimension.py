from airflow.hooks.postgres_hook import PostgresHook
from airflow.models import BaseOperator
from airflow.utils.decorators import apply_defaults

class LoadDimensionOperator(BaseOperator):
    """
    Airflow custom operator to load dimension tables in Redshift
    """
    truncate_sql = """
    TRUNCATE TABLE {};
    """
    insert_sql = """
    INSERT INTO {} {};
    """
    ui_color = '#80BD9E'

    @apply_defaults
    def __init__(self,
                 redshift_conn_id = "redshift",
                 table = "",
                 truncate = True,
                 sql_query = "",
                 *args, **kwargs):

        super(LoadDimensionOperator, self).__init__(*args, **kwargs)
        self.redshift_conn_id = redshift_conn_id
        self.table = table
        self.truncate = truncate
        self.sql_query = sql_query
        

    def execute(self, context):
        self.log.info(f'Loading Dimension table {self.table}')
        redshift_hook = PostgresHook(postgres_conn_id=self.redshift_conn_id)
        
     
        if self.truncate:
            redshift_hook.run(LoadDimensionOperator.truncate_sql.format(self.table))
        
        redshift_hook.run(LoadDimensionOperator.insert_sql.format(self.table, self.sql_query))
        
       
    
       