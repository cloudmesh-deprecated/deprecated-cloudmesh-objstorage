## Cloudmesh Object Store


## Instalation for Users

At this time we do not offer this but it will be

```bash
pip install cloudmesh-community
```

Gregor will set this up, so please do not do this yourself. 

# Instalation for Developers

This install only works if you use ssh-keys with github

```bash
mkdir cm
cd cm
pip install cloudmesh-installer
#
# if you have not uploaded your ssh key to git do so. One option is
# cloudmesh-installer git key
#
cloudmesh-installer clone storage
cloudmesh-installer install storage -e
git clone git@github.com:cloudmesh/cloudmesh-objstorage.git
cd sp19-616-111/project-code/cloudmesh-objstorage
pip install -e .
```

## TBD

put your documentation here
