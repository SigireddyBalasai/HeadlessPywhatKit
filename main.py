from HeadlessPywhatKit.sqsworker import process_sqs_que
from HeadlessPywhatKit.app import create_app
import sys

#if args[1] is flask then run create app
if sys.argv[1] == 'flask':
    app = create_app()
    app.run(host='0.0.0.0')
if sys.argv[1] == 'sqs':
    process_sqs_que()

