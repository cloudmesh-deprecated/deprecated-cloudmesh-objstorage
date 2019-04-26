from cloudmesh.common.parameter import Parameter
from cloudmesh.objstorage.provider.awss3.Provider import Provider
from cloudmesh.shell.command import PluginCommand, map_parameters
from cloudmesh.shell.command import command
from cloudmesh.variables import Variables
from cloudmesh.DEBUG import VERBOSE

# noinspection PyPep8
class ObjstorageCommand(PluginCommand):

    # noinspection PyUnusedLocal
    @command
    def do_objstorage(self, args, arguments):

        """
        ::
          Usage:
                objstorage [--service=SERVICE] create dir DIRECTORY
                objstorage [--service=SERVICE] copy SOURCE DESTINATION [--recursive]
                objstorage [--service=SERVICE] get SOURCE DESTINATION [--recursive]
                objstorage [--service=SERVICE] put SOURCE DESTINATION [--recursive]
                objstorage [--service=SERVICE] list SOURCE [--recursive] [--output=OUTPUT]
                objstorage [--service=SERVICE] delete SOURCE
                objstorage [--service=SERVICE] search  DIRECTORY FILENAME [--recursive] [--output=OUTPUT]
          This command does some useful things.
          Arguments:
              SOURCE        BUCKET | OBJECT  can be a source bucket or object name or file
              DESTINATION   BUCKET | OBJECT can be a destination bucket or object name  or file
              DIRECTORY     DIRECTORY refers to a folder or bucket on the cloud service for ex: awss3
          Options:
              -h, --help
              --service=SERVICE  specify the cloud service name like aws-s3
          Description:
                commands used to upload, download, list files on different cloud objstorage services.
                objstorage put [options..]
                    Uploads the file specified in the filename to specified cloud from the SOURCEDIR.
                objstorage get [options..]
                    Downloads the file specified in the filename from the specified cloud to the DESTDIR.
                objstorage delete [options..]
                    Deletes the file specified in the filename from the specified cloud.
                objstorage list [options..]
                    lists all the files from the container name specified on the specified cloud.
                objstorage create dir [options..]
                    creates a folder with the directory name specified on the specified cloud.
                objstorage search [options..]
                    searches for the source in all the folders on the specified cloud.
          Example:
            set objstorage=s3object
            objstorage put SOURCE DESTINATION --recursive
            is the same as
            objstorage --service=s3object put SOURCE DESTINATION --recursive

            Create a multi file directy in a bucket

            $ cms set objstorge=awss3
            $ tree
                a/a1.tx
                a/b/b1.txt

            cms objstorage create a/b/
            cms objstorage put a/b/b1.txt /a/b



        """
        # arguments.CONTAINER = arguments["--container"]

        map_parameters(arguments,
                       "recursive",
                       "objstorage")
        VERBOSE.print(arguments, verbose=9)

        if arguments.service is None:
            try:
                v = Variables()
                arguments.service = v['objstorage']
            except Exception as e:
                arguments.service = None
                raise ValueError("objstorage provider is not defined")

        arguments.service = Parameter.expand(arguments.service)

        print(arguments)

        provider = Provider(arguments.service)

        if arguments.copy:
            result = provider.copy(
                                  arguments.SOURCE,
                                  arguments.DESTINATION,
                                  arguments.recursive)

        if arguments.get:
            result = provider.get(
                                  arguments.SOURCE,
                                  arguments.DESTINATION,
                                  arguments.recursive)

        elif arguments.put:
            result = provider.put(
                                  arguments.SOURCE,
                                  arguments.DESTINATION,
                                  arguments.recursive)

        elif arguments.create and arguments.dir:
            result = provider.createdir(
                                        arguments.DIRECTORY)

        elif arguments.list:
            for objstorage in arguments.service:
                provider = Provider(objstorage)

                result = provider.list(
                                       arguments.SOURCE,
                                       arguments.recursive)

        elif arguments.delete:

            for objstorage in arguments.service:
                provider = Provider(objstorage)

                provider.delete(
                                arguments.SOURCE)

        elif arguments.search:

            for objstorage in arguments.service:
                provider = Provider(objstorage)

                provider.search(
                                arguments.DIRECTORY,
                                arguments.FILENAME,
                                arguments.recursive)

        return ""