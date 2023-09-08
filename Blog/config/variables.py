from dotenv import dotenv_values

ENV = dotenv_values()

# NEW VARIABLES
SECRET_KEY = ENV["SECRET_KEY"]