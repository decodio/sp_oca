=============
Visual Export
=============

Visual export is an openERP module, it add a one click button on the top of view list
it allow to export what you see to an OpenDocument (ods). The export looks like the view list,
getting data from the search domain and user context, keeping "groups by",
notice metadata about the export information.

    |screenshot|


.. note::

    **Grouped by** value are by default an ods SUM() formula.


Documentation
=============

visual_export_use_read_group
----------------------------

If you overload `read_group` method, you may want that value as value on
the ods grouped by line.

To do that, you have to set in in the field option like this::

    _columns = {
        ...
        'my_field': fields.integer(u"My field name", visual_export_use_read_group=True),
        ...

.. |screenshot| image:: https://bytebucket.org/anybox/visual_export/raw/default/screenshot.png

Default visual_export_use_read_group
------------------------------------

By default, **grouped by** values are ods formula using sum or average, you
can manage the default behavior to export the result value from read_group
openERP computation method as used to display values in openERP. To do so you
have to set the following key/value in `system settings` from technical
configuration menu

:key: ``visual_export.default_visual_export_use_read_group``
:value: ``True``


