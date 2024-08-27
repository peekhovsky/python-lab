import time
import inspect

separator = ', '


def log(decorated_func):
    def wrapper(*args, **kwargs):
        start = time.time()
        res = decorated_func(*args, **kwargs)
        end = time.time()

        param_names = inspect.getfullargspec(decorated_func).args

        args_names = list(filter(lambda name: name not in kwargs.keys(), param_names))

        str_args = []
        for i in range(0, len(args_names)):
            str_args.append(f"{args_names[i]}={args[i]}")

        args_param = separator.join(str_args)

        str_kwargs = []
        for key, value in kwargs.items():
            str_kwargs.append(f"{key}={value}")

        kwargs_param = separator.join(str_kwargs)

        fn_name = decorated_func.__name__
        exec_time = end - start

        log_line = f"{fn_name}; args: {args_param}; kwargs: {kwargs_param}; execution time: {exec_time} sec.\n"
        print(f'log_line: {log_line}')

        log_file = open('log.txt', 'a+')
        log_file.write(log_line)
        log_file.close()

        return res

    return wrapper


@log
def foo(a, b, c):
    time.sleep(0.5)
    return f'result of foo(a={a}, b={b}, c={c})'


if __name__ == '__main__':
    res1 = foo(10, 20, c=30)
    print(f"res1: {res1}")
