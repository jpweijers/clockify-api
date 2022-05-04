Getting Started
===============

This page will show you how to install and use clockify-api.

============
Installation
============
Installation is very easy.

Use pip:

.. code-block:: shell

  pip install clockify-api

or poetry (my preffered method):

.. code-block:: shell

  poetry add clockify-api

==========
Quickstart
==========

First you need to set up a clockify session:

.. code-block:: python

  import clockify

  
  KEY = "YOUR API KEY"

  # create session
  session = clockify.ClockifySession(KEY)

Then you can use the session to make API calls. 
First you might want to get the current active workspace.
The workspace is needed for pretty much every other request to Clockify.

.. code-block:: python

  ...
  # get current user
  current_user = session.get_current_user()

  # get workspace ID from current user
  workspace_id = current_user.active_workspace
  print(workspace_id)
  >>> 626399702993d4192cb6abcd

With this workspace you could retrieve a list of clients:

.. code-block:: python

  ...
  # Get clients
  clients = session.client.get_clients(workspace_id)

  if len(clients) > 0:
    print(clients[0])
    >>> id_='abcdc8c6f87fd71e0e414d94' name='Test Client' 
      workspace_id='626399702993d4192cb6abcd' archived=False

You can edit a client like this:

.. code-block:: python

  ...
  # change name
  clients[0].name = "McDonald's"

  # update client
  client = session.client.update_client(clients[0])

  print(client)
  >>> id_='abcdc8c6f87fd71e0e414d94' name="McDonald's" 
    workspace_id='626399702993d4192cb6abcd' archived=False
    
Let's delete the client:

.. code-block:: python

  ...
  # delete client
  session.client.delete(workspace_id, client.id_)

Now check if the client is deleted:

.. code-block:: python

  ...
  # make query params to search for the deleted client
  params = clockify.ClientGetParams(name="McDonald's")

  # get clients with query params
  clients = session.client.get_clients(workspace_id, params)

  print(clients)
  >>> []
  
