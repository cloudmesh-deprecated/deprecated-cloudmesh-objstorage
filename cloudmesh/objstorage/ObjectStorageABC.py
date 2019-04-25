from abc import ABCMeta

from cloudmesh.management.configuration.config import Config


# noinspection PyUnusedLocal,PyPep8
class ObjectStorageABC(metaclass=ABCMeta):

    def __init__(self, service=None, config="~/.cloudmesh/cloudmesh4.yaml"):
        try:
            self.config = Config(config_path=config)

            spec = self.config["cloudmesh.objstorage"]
            self.credentials = spec[service]['credentials']
            self.kind = spec[service]['cm']['kind']
            self.cloud = service
            self.service = service
        except Exception  as e:
            raise ValueError(f"object storage service {service} not specified")
            print (e)

    def create_dir(self, directory=None):
        """
        creates a directory
        :param directory: the name of the directory
        :return: dict
        """
        raise NotImplementedError

    def list(self, source=None, recursive=False):
        """
        lists the information as dict
        :param source: the source which either can be a directory or file
        :param recursive: in case of directory the recursive referes to all
                          subdirectories in the specified source
        :return: dict
        """
        raise NotImplementedError

    def put(self, source=None, destination=None, recursive=False):
        """
        puts the source on the service
        :param source: the source which either can be a directory or file
        :param destination: the destination which either can be a directory or
                            file
        :param recursive: in case of directory the recursive referes to all
                          subdirectories in the specified source
        :return: dict
        """
        raise NotImplementedError

    def get(self, source=None, destination=None, recursive=False):
        """
        gets the destination and copies it in source
        :param source: the source which either can be a directory or file
        :param destination: the destination which either can be a directory or
                            file
        :param recursive: in case of directory the recursive referes to all
                          subdirectories in the specified source
        :return: dict
        """
        raise NotImplementedError

    def delete(self, source=None, recursive=False):
        """
        deletes the source
        :param source: the source which either can be a directory or file
        :param recursive: in case of directory the recursive referes to all
                          subdirectories in the specified source
        :return: dict
        """
        raise NotImplementedError

    def search(self, directory=None, filename=None, recursive=False):
        """
        gets the destination and copies it in source
        :param directory: the directory which either can be a directory or file
        :param filename: the filename
        :param recursive: in case of directory the recursive referes to all
                          subdirectories in the specified source
        :return: dict
        """
        raise NotImplementedError
