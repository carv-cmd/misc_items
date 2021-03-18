# Prints all available environment variables
# Env Var 'key' and its 'value'

env_vars = os.environ
for var_key in env_vars.keys():
    print(f'\nEnvVar_Key: {var_key}'
          f'\n\tEnvVar_Val: {env_vars[var_key]}')
