# The config file is located in the user's home directory.
# The home directory is different on different platforms.
# The following code is a cross-platform way to get the home directory.

# Get the user's home directory.
home_dir = os.path.expanduser('~')

# Get the full path to the config file.
config_file_path = os.path.join(home_dir, '.config', 'my_app', 'config.ini')

# Create the config parser object.
config = configparser.ConfigParser()

# Read the config file.
config.read(config_file_path)

# Get the value of the "Server" setting in the "[network]" section.
server = config.get('network', 'server')

# Get the value of the "Port" setting in the "[network]" section.
port = config.getint('network', 'port')

# Get the value of the "Log File" setting in the "[logging]" section.
log_file = config.get('logging', 'log file')

# Get the value of the "Log Level" setting in the "[logging]" section.
log_level = config.get('logging', 'log level')

# Get the value of the "Log Format" setting in the "[logging]" section.
log_format = config.get('logging', 'log format')

# Print the values.
print('Server:', server)
print('Port:', port)
print('Log File:', log_file)
print('Log Level:', log_level)
print('Log Format:', log_format)

# Write the config file.
with open(config_file_path, 'w') as config_file:
    config.write(config_file)