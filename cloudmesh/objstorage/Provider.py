from cloudmesh.ojectstore.provider.awss3 import Provider as Awss3Provider

class Provider(ObjectStorageABC):


    def __init__(self, service=None, config="~/.cloudmesh/cloudmesh4.yaml"):
        super().__init__(service=service, config=config)


        if self.kind == "awss3":
            self.provider = Awss3Provider(service=service, config=config)
        else:
            raise ValueError(
                f"Storage provider '{self.kind}' not yet supported")

    def cm_update(self, d):

        cm = {
            'cm': {
                'kind': 'define me from d',
                'name': 'define me from d',
                'cloud': 'define me from d'
            }
        }
        d.update(cm)

    @DatabaseUpdate()
    def create_dir(self,  directory=None):
        """
        creates a directory
        :param service: the name of the service in the yaml file
        :param directory: the name of the directory
        :return: dict
        """
        d = self.provider.create_dir(self,
                              directory=directory)
        d = self.cm_update(d)

        return d


    @DatabaseUpdate()
    def list(self, source=None, recursive=False):
        """
        lists the information as dict
        :param service: the name of the service in the yaml file
        :param source: the source which either can be a directory or file
        :param recursive: in case of directory the recursive referes to all
                          subdirectories in the specified source
        :return: dict
        """
        d = self.provider.list(self,
                              source=source,
                              recusrive=recursive)
        d = self.cm_update(d)

        return d

    @DatabaseUpdate()
    def put(self, source=None, destination=None, recursive=False):
        """
        puts the source on the service
        :param service: the name of the service in the yaml file
        :param source: the source which either can be a directory or file
        :param destination: the destination which either can be a directory or file
        :param recursive: in case of directory the recursive referes to all
                          subdirectories in the specified source
        :return: dict
        """
        d = self.provider.get(self,
                              source=source,
                              destination=destination,
                              recusrive=recursive)
        d = self.cm_update(d)

        return d

    # not yet sure if service is needed
    @DatabaseUpdate()
    def get(self, source=None, destination=None, recusrive=False):
        """
        gets the destination and copies it in source
        :param service: the name of the service in the yaml file
        :param source: the source which either can be a directory or file
        :param destination: the destination which either can be a directory or file
        :param recursive: in case of directory the recursive referes to all
                          subdirectories in the specified source
        :return: dict
        """
        d = self.provider.get(self,
                              source=source,
                              destination=destination,
                              recusrive=recusrive)

        d = self.cm_update(d)

        return d

    @DatabaseUpdate()
    def delete(self, source=None, recusrive=False):
        """
        deletes the source
        :param service: the name of the service in the yaml file
        :param source: the source which either can be a directory or file
        :param recursive: in case of directory the recursive referes to all
                          subdirectories in the specified source
        :return: dict
        """
        d = self.provider.delete(self,
                              source=source,
                              recusrive=recusrive)

        d = self.cm_update(d)

        return d

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
        d = self.provider.get(self,
                              directory=directory,
                              filename=filename,
                              recusrive=recusrive)

        d = self.cm_update(d)

        return d





