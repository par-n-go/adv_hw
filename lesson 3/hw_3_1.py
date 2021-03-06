import time

def multiple_times(repeat_times):

    def actual_decorator(func):

        def wrapper(*args):
            result = {}
            result['start_time'] = time.time()
            result['iteration_times'] = []
            result['iteration_results'] = []
            result['final_result'] = None
            for i in range(repeat_times):
                start_time_iteration = time.time()
                temp_result = func(*args)
                iteration_time = time.time() - start_time_iteration
                result['iteration_times'].append(iteration_time)
                result['iteration_results'].append(temp_result)
                result['final_result'] = temp_result
                #print(f'Затрачено времени на вызов функции: {str(time.time() - start_time_iteration)} секунд')
            result['total_time'] = time.time() - result['start_time']
            result['function_name'] = func.__name__
            #print(f'Всего затрачено времени на все вызовы функций: {str(result["total_time"])} секунд')

            return result

        return wrapper

    return actual_decorator

@multiple_times(5)
def addition(a, b):
    result = 0
    for i in range(a*b):
        result += a + b
    return result

function_result = addition(10, 50)
print(f'Начало исполнения функций: {function_result["start_time"]}')
print(f'Общее время исполнения функций: {function_result["total_time"]}')
print(f'Название функции: {function_result["function_name"]}')
print(f'Последний результат функции: {function_result["final_result"]}')
for single_time in function_result['iteration_times']:
    print(f'Время исполнения функции: {single_time}')
for single_result in function_result['iteration_results']:
    print (f'Значение выполнения функции: {single_result}')

