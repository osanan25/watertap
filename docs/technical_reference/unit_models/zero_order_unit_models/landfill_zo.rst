Landfill  (ZO)
==============

Model Type
----------
This unit model is formulated as a **pass-through** model form.
See documentation for :ref:`pass-through Helper Methods<pt_methods>`.

Electricity Consumption
-----------------------
Electricity consumption is calculated using the **constant_intensity** helper function.
See documentation for :ref:`Helper Methods for Electricity Demand<electricity_methods>`.

Costing Method
--------------
Costing is calculated using the **cost_landfill** method in the zero-order costing package.
See documentation for the :ref:`zero-order costing package<zero_order_costing>`.

Additional Variables
--------------------

.. csv-table::
   :header: "Description", "Variable Name", "Units"

   "capacity basis for capital cost", "capacity_basis", ":math:`kg/hr`"
   "total mass flow rate", "total_mass", ":math:`kg/hr`"

Additional Constraints
----------------------

.. csv-table::
   :header: "Description", "Constraint Name"

   "Total mass constraint", "total_mass_constraint"

.. index::
   pair: watertap.unit_models.zero_order.landfill_zo;landfill_zo

.. currentmodule:: watertap.unit_models.zero_order.landfill_zo

Class Documentation
-------------------

.. automodule:: watertap.unit_models.zero_order.landfill_zo
    :members:
    :noindex:
