# Cloudmesh Object Storage Interfaces

## Object Storage with ASW S3

Object Storage is one of the feature in AWS S3 and this feature integrated with cloudmesh library and is available 
for use via commandline. 

Follow the below steps:

- Modify `cloudmesh4.yaml` config file in 'cloudmesh-objstorage' section. User need to add required object storage parameters to communicate with cloud(AWS S3)

- In the credentials section under awss3, add the parameter values of access_key_id and secret_access_key, these credentials will be gained from appropriate cloud vendor(For ex: AWS), in the case of AWS, these will be available which will be available in the AWS console under 
`AWS IAM service` -> `Users` -> `Security Credentials`. 


Here is a sample.

```bash
cloudmesh:
  ...
  objstorage:
    awss3:
      cm:
        heading: aws
        host: amazon.aws.com
        label: aws
        kind: awss3
        version: 1.0
      default:
        directory: AWS
      credentials:
        access_key_id: *********
        secret_access_key: *******
```

The Cloudmesh command line library offers several functions as part of objstorage command: 
get, put, search, list, create, and delete. 
Once you have installed Cloudmesh, type `cms` into the command line to start the
cms shell. 

```bash
$ cms
+-------------------------------------------------------+
|   ____ _                 _                     _      |
|  / ___| | ___  _   _  __| |_ __ ___   ___  ___| |__   |
| | |   | |/ _ \| | | |/ _` | '_ ` _ \ / _ \/ __| '_ \  |
| | |___| | (_) | |_| | (_| | | | | | |  __/\__ \ | | | |
|  \____|_|\___/ \__,_|\__,_|_| |_| |_|\___||___/_| |_| |
+-------------------------------------------------------+
|                  Cloudmesh CMD5 Shell                 |
+-------------------------------------------------------+

cms>
```

To view the docopt for objstorage command, type in 

```bash
cms> help objstorage 
```

Help command gives a detail level understanding of what each command does and 
how to use the command line to interact with different object storage providers and 
different parameters / options available in a particular command. 

In this, default object storage invokes AWS S3 service, we need to pass awss3 as parameter to storage 
and suffix with the function call with the function parameters.

```bash
cms> objstorage --objstorage='aws3' list ''
```

Alternatively, objstorage command can also be called directly without starting the 
cms shell.

```bash
$ cms objstorage --objstorage='awss3' list ''
```

### objstorage functions overview


### Create Object Directory 

This command helps to create a new bucket before storage an object on AWS S3. You must specify the 
full path of the new directory you would like to create. 

```bash
$ cms objstorage --objstorage='awss3' create bucket_name /base_path/
```

### Put

The put command uploads object from your local system to AWS S3 object storage 

```bash
$ cms objstorage --objstorage='awss3' put ~/.cloudmesh/objstorage/src /base_path/dest --recursive
```


### Get

The put command retrieve or download a object from AWS S3 object storage 

```bash
$ cms objstorage --objstorage='awss3' get /bucket_name/src ~/.cloudmesh/objstorage/dest --recursive
```


### Search

The advantage of search command to search a given object in specified bucket location


```bash
$ cms objstorage --objstorage='aws3' search //bucket_name/dest "<<objectname>>" --recursive
```

### List

The list command lists all the contents of a cloud object details. If the recursive 
option is specified, it will list the contents of all the nested objects information 

```bash
$ cms objstorage --objstorage='awss3' list /bucket_name/dest --recursive
```


### Delete

The delete command can delete objects on cloud storage. Once object deletes it will never be rollback and delete applicable to nested objects when function `--recursive` used. 
Deleting a folder will delete its contents as well (including the 
sub-directories).

```bash
$ cms objstorage --objstorage='awss3' delete /bucket_name/est --recursive
```

