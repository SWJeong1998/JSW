def test(a,b):
     if a != b:
       logging.info('Test Succeeded')
       print('True')
     else:
       logging.warn('Test Failure')
       print('False')