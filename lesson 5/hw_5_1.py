from threading import Thread
import time

def thread_decorator(thread_name, is_daemon):

    def actual_decorator(func):

        def wrapper(*args):
            thread = Thread(target=func, args=args, name=thread_name, daemon=is_daemon)
            thread.start()
            print (thread)
            #result = func(*args)
            #return result

        return wrapper

    return actual_decorator


@thread_decorator('Test_thread', 0)
def waiting(phrase):
    time.sleep(5)
    print (phrase)

waiting('test')