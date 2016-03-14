
.. image:: https://img.shields.io/badge/licence-AGPL--3-blue.svg
    :alt: License

User roles
==========

This module was written to extend the standard functionality regarding users
and groups management.
It helps creating well-defined user roles and associating them to users.

It can become very hard to maintain a large number of user profiles over time,
juggling with many technical groups. For this purpose, this module will help
you to:

  * defining functional roles by aggregating low-level groups,
  * setting user accounts with the predefined roles (roles are cumulative),
  * updating groups of all relevant user accounts (all at once),
  * ensuring that user accounts will have the groups defined in their roles
    (nothing more, nothing less). In other words, you can not set groups
    manually on a user as long as there is roles configured on it,
  * getting a quick overview of roles and the related user accounts.

That way you make clear the different responsabilities within a company, and
are able to add and update user accounts in a scalable and reliable way.

Configuration
=============

To configure this module, you need to go to *Configuration / Users / Roles*,
and create a new role. From there, you can add groups to compose your role,
and then associate users to it.

Credits
=======

Contributors
------------

* Sébastien Alix <sebastien.alix@osiell.com>
