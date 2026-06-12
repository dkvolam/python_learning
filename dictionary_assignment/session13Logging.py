import logging
logging.basicConfig(filename='C:\python_learning\python_learning\etllog.log',level=logging.INFO,format='%(asctime)s:%(levelname)s:%(message)s')

etlStages = ['stage', 'dimlayer', 'warehouse']

logging.info('ETL process started')

for file in etlStages:
    logging.info(f'{file} processing started')
    # Simulate processing
    logging.info(f'{file} processing completed')

logging.info('ETL process completed')

#use logging in function and try it 