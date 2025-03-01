Supercritical Salt Precipitation (ZO)
=====================================

Model Type
----------
This unit model is formulated as a **single-input, double-output** model form.
See documentation for :ref:`single-input, double-output Helper Methods<sido_methods>`.

Electricity Consumption
-----------------------
The constraint used to calculate energy consumption is described in the Additional Constraints section below. More details can be found in the unit model class.

Costing Method
--------------
Costing is calculated using the **cost_supercritical_salt_precipitation** method in the zero-order costing package.
See documentation for the :ref:`zero-order costing package<zero_order_costing>`.

Additional Variables
--------------------

.. csv-table::
   :header: "Description", "Variable Name", "Units"

   "Inlet mass flowrate", "flow_mass_in", ":math:`t/hr`"
   "Electricity consumption of unit", "electricity", ":math:`kW`"
   "Electricity intensity with respect to inlet flowrate", "energy_electric_flow_mass", ":math:`kWh/t`"

Additional Constraints
----------------------

.. csv-table::
   :header: "Description", "Constraint Name"

   "Constraint for inlet mass flowrate.", "cons_flow_mass"
   "Constraint for electricity consumption based on inlet flowrate.", "electricity_consumption"

.. index::
   pair: watertap.unit_models.zero_order.supercritical_salt_precipitation_zo;supercritical_salt_precipitation_zo

.. currentmodule:: watertap.unit_models.zero_order.supercritical_salt_precipitation_zo

Class Documentation
-------------------

.. automodule:: watertap.unit_models.zero_order.supercritical_salt_precipitation_zo
    :members:
    :noindex:
