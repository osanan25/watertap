Electrochemical Nutrient Removal (ZO)
=====================================

Model Type
----------
This unit model is formulated as a **reactive single-inlet, double-outlet** model form.
See documentation for :ref:`reactive single-inlet, double-outlet Helper Methods<sidor_methods>`.

Electricity Consumption
-----------------------
The constraint used to calculate energy consumption is described in the Additional Constraints section below. More details can be found in the unit model class.

Costing Method
--------------
Costing is calculated using the **cost_electrochemical_nutrient_removal** method in the zero-order costing package.
See documentation for the :ref:`zero-order costing package<zero_order_costing>`.

Additional Variables
--------------------

.. csv-table::
   :header: "Description", "Variable Name", "Units"

   "Electricity consumption of unit", "electricity", ":math:`kW`"
   "Electricity intensity with respect to struvite byproduct flowrate of unit", "energy_electric_flow_mass", ":math:`kWh/kg`"
   "Dosage of magnesium chloride per struvite", "magnesium_chloride_dosage", ":math:`dimensionless`"
   "Magnesium chloride flowrate", "MgCl2_flowrate", ":math:`kg/hr`"

Additional Constraints
----------------------

.. csv-table::
   :header: "Description", "Constraint Name"

   "Constraint for electricity consumption based on struvite flowrate.", "electricity_consumption"
   "Constraint for magnesium chloride demand based on struvite flowrate.", "MgCl2_demand"

.. index::
   pair: watertap.unit_models.zero_order.electrochemical_nutrient_removal_zo;electrochemical_nutrient_removal_zo

.. currentmodule:: watertap.unit_models.zero_order.electrochemical_nutrient_removal_zo

Class Documentation
-------------------

.. automodule:: watertap.unit_models.zero_order.electrochemical_nutrient_removal_zo
    :members:
    :noindex:
