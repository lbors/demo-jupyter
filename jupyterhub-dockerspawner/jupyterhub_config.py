c = get_config()  # noqa

# dummy for testing. Don't use this in production!
c.JupyterHub.authenticator_class = "dummy"

# launch with docker
#c.JupyterHub.spawner_class = "docker"
c.JupyterHub.spawner_class = "dockerspawner.DockerSpawner"


# we need the hub to listen on all ips when it is in a container
c.JupyterHub.hub_ip = '0.0.0.0'
# the hostname/ip that should be used to connect to the hub
# this is usually the hub container's name
c.JupyterHub.hub_connect_ip = 'jupyterhub'

# pick a docker image. This should have the same version of jupyterhub
# in it as our Hub.
#c.DockerSpawner.image = 'jupyter/base-notebook'
c.DockerSpawner.image = 'demo/notebook-server:latest'

# tell the user containers to connect to our docker network
c.DockerSpawner.network_name = 'jupyterhub'

# delete containers when the stop
c.DockerSpawner.remove = True

c.Spawner.cmd=["jupyter-labhub"]
c.JupyterHub.allow_named_servers = True
