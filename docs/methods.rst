Available Methods
=================

.. testsetup:: *

   import requests
   from gandalf.client import GandalfClient
   gandalf = GandalfClient("localhost", 8001, requests.request)

repository_new
--------------

Create a new repository

Arguments:

* name: The repository's name
* users: List of users to grant access
* ispublic: Flag to public repository (default: False)

Example:

.. testcode:: repository_new

   gandalf.repository_new('my-project-repository', ['rfloriano'])

repository_get
--------------

Get repository data

Arguments:

* name: The repository's name

Example:

.. testcode:: repository_get

   gandalf.repository_get('my-project-repository')


repository_rename
-----------------

Rename a repository

Arguments:

* old_name: The actual repository's name
* new_name: The new name to repository

Example:

.. testcode:: repository_rename

   gandalf.repository_rename('my-project-repository', 'project-repository')


repository_grant
----------------

Grant access to users in repositories

Arguments:

* users: List of users to grant accesss
* repositories: List of repositories to grant users acesss

Example:

.. testcode:: repository_grant

   gandalf.repository_grant(['rfloriano'], ['project-repository'])


repository_revoke
-----------------

Revoke access to users in repositories

Arguments:

* users: List of users to revoke accesss
* repositories: List of repositories to revoke users acesss

Example:

.. testcode:: repository_grant

   gandalf.repository_grant(['rfloriano'], ['project-repository'])


repository_archive
------------------

Arguments:

* name: The repository's name
* ref: Git reference to file
* format: The file format


repository_contents
-------------------
Arguments:

* name: The repository's name
* path: File's path


repository_delete
-----------------

Delete a repository

Arguments:

* name: The repository's name

Example:

.. testcode:: repository_delete

   gandalf.repository_delete('project-repository')


user_add_key
------------

Add ssh public key to an user

Arguments:

* name: The username
* keys: Dictionary of public key to associate with user account (Ie: {'macbook-key': 'ssh-dss my-public-key== f@foo.bar'})

Example:

.. testcode:: user_add_key

   gandalf.user_add_key('rfloriano', {'my-ssh-key-another': 'content-of-my-ssh-public-another-key'})


user_get_keys
-------------

Get keys from an user

Arguments:

* name: The username

Example:

.. testcode:: user_get_keys

   gandalf.user_get_keys('rfloriano')


user_delete_key
---------------

Delete keys from an user

Arguments:

* name: The username
* keyname: The key name to remove (Ie: 'macbook-key')

Example:

.. testcode:: user_delete_key

   gandalf.user_delete_key('rfloriano', 'my-ssh-key-another')

user_new
--------

Create an new user

Arguments:

* name: The username
* keys: Dictionary of public key to associate with user account (Ie: {'macbook-key': 'ssh-dss my-public-key== f@foo.bar'})

Example:

.. testcode:: user_new

   gandalf.user_new('rfloriano', {'my-ssh-key': 'content-of-my-ssh-public-key'})


user_delete
-----------

Delete an user

Arguments:

* name: The username

Example:

.. testcode:: user_delete

   gandalf.user_delete('rfloriano')


hook_add
--------

Add git server hook

Arguments:

* name: The hook's name
* content: Content of hook

healthcheck
-----------

Validates if the gandalf server responds to healthcheck.

Example:

.. testcode:: healthcheck

   assert gandalf.healthcheck()
