from cloudmesh.management.configuration.config import Config
from pprint import pprint


config = Config()
pprint(config.dict())
print(config)
print(type(config.data))

# cloudmesh:
#   objstorage:
#     awss3:
#       cm:
#         heading: AWS
#         host: aws.com
#         label: AWS
#         kind: awss3
#         version: 1.0
#       default:
#         directory: AWS
#       credentials:
#         ACCESS_KEY_ID: ""
#         SECRET_ACCESS_KEY: ""

# data = config["cloudmesh"]["objstorage"]["awss3"]["credentials"]
data = config["cloudmesh.objstorage.awss3.credentials"]
print(data)