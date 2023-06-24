def command_checker(results_range: range, **commands):
    """Проверяет результаты выполнения команд на соответствие диапазону."""
    for command, result in commands.items():
        # if result in results_range:
            # result_str = 'SUCCESS'
        # else:
            # result_str = 'FAIL'
        result_str = 'SUCCESS' if result in results_range else 'FAIL'
        print(f'{command} — {result} — {result_str}')


command_checker(range(1, 1000), comm1=10, comm2=15, comm3=-1, comm4=200)
# comm1 — 10 — SUCCESS
# comm2 — 15 — SUCCESS
# comm3 — -1 — FAIL
# comm4 — 200 — SUCCESS

commands = {'comm1': 10, 'comm2': 15, 'comm3': -1, 'comm4': 200}

command_checker(range(-10, 11), **commands)
# comm1 — 10 — SUCCESS
# comm2 — 15 — FAIL
# comm3 — -1 — SUCCESS
# comm4 — 200 — FAIL

