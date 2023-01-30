import sys

print(sys.argv[1])
#if args[1] is flask then run create app
if sys.argv[1] == 'flask':
    from HeadlessPywhatKit.app import create_app
    
    app = create_app()
    app.run(host='0.0.0.0')

if sys.argv[1] == 'sqs':
    from HeadlessPywhatKit.sqsworker import process_sqs_que
    process_sqs_que()

