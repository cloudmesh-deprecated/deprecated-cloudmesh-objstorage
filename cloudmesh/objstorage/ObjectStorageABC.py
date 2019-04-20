from abc import ABCMeta, abstractmethod
from cloudmesh.management.configuration.config import Config


# noinspection PyUnusedLocal,PyPep8
class ObjectStorageABC(metaclass=ABCMeta):

    def __init__(self, service=None, config="~/.cloudmesh/cloudmesh4.yaml"):
        try:
            self.config = Config()
            self.credentials = config['cloudmesh']['objstorage'][service][
                'credentials']
            self.kind = config['cloudmesh']['objstorage']['kind']
            self.servise = service
        except:
            raise ValueError(f"object storage service {service} not specified")

    def create_dir(self, directory=None):
        """
        creates a directory
        :param service: the name of the service in the yaml file
        :param directory: the name of the directory
        :return: dict
        """
        raise NotImplementedError

    def list(self, source=None, recursive=False):
        """
        lists the information as dict
        :param service: the name of the service in the yaml file
        :param source: the source which either can be a directory or file
        :param recursive: in case of directory the recursive referes to all
                          subdirectories in the specified source
        :return: dict
        """
        raise NotImplementedError

    def put(self, source=None, destination=None, recusrive=False):
        """
        puts the source on the service
        :param service: the name of the service in the yaml file
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
        :param service: the name of the service in the yaml file
        :param source: the source which either can be a directory or file
        :param destination: the destination which either can be a directory or
                            file
        :param recursive: in case of directory the recursive referes to all
                          subdirectories in the specified source
        :return: dict
        """
        raise NotImplementedError

    def delete(self, source=None, recusrive=False):
        """
        deletes the source
        :param service: the name of the service in the yaml file
        :param source: the source which either can be a directory or file
        :param recursive: in case of directory the recursive referes to all
                          subdirectories in the specified source
        :return: dict
        """
        raise NotImplementedError

    def search(self, directory=None, filename=None,
               recusrive=False):
        """
        gets the destination and copies it in source
        :param service: the name of the service in the yaml file
        :param directory: the directory which either can be a directory or file
        :param recursive: in case of directory the recursive referes to all
                          subdirectories in the specified source
        :return: dict
        """
        raise NotImplementedError
