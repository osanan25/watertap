###############################################################################
# WaterTAP Copyright (c) 2021, The Regents of the University of California,
# through Lawrence Berkeley National Laboratory, Oak Ridge National
# Laboratory, National Renewable Energy Laboratory, and National Energy
# Technology Laboratory (subject to receipt of any required approvals from
# the U.S. Dept. of Energy). All rights reserved.
#
# Please see the files COPYRIGHT.md and LICENSE.md for full copyright and license
# information, respectively. These files are also available online at the URL
# "https://github.com/watertap-org/watertap/"
#
###############################################################################

import pytest
from idaes.core.solvers import get_solver
from pyomo.environ import value, assert_optimal_termination
from pyomo.util.check_units import assert_units_consistent
from watertap.core.util.initialization import assert_degrees_of_freedom
from watertap.examples.flowsheets.case_studies.wastewater_resource_recovery.amo_1575_magprex.magprex import (
    build,
    set_operating_conditions,
    initialize_system,
    solve,
    add_costing,
    display_results,
    display_costing,
)

solver = get_solver()


class TestMagprexFlowsheet:
    @pytest.fixture(scope="class")
    def system_frame(self):
        m = build()
        return m  # return model

    @pytest.mark.unit()
    def test_build(self, system_frame):
        m = system_frame
        assert_units_consistent(m)
        assert_degrees_of_freedom(m, 14)

    @pytest.mark.component
    def test_set_operating_conditions(self, system_frame):
        m = system_frame
        set_operating_conditions(m)
        initialize_system(m)

        # test feed water flow
        assert value(m.fs.feed.properties[0].flow_mass_comp["H2O"]) == pytest.approx(
            35.043286, rel=1e-3
        )
        assert value(
            m.fs.feed.properties[0].flow_mass_comp["phosphates"]
        ) == pytest.approx(0.0122694, rel=1e-5)
        assert value(
            m.fs.feed.properties[0].flow_mass_comp["struvite"]
        ) == pytest.approx(0, abs=1e-10)

    @pytest.mark.component
    def test_solve(self, system_frame):
        m = system_frame
        results = solve(m)
        assert_optimal_termination(results)

        # check two struvite product flow
        assert value(
            m.fs.struvite_product.properties[0].flow_mass_comp["H2O"]
        ) == pytest.approx(4.302064e-21, rel=1e-3)
        assert value(
            m.fs.struvite_product.properties[0].flow_mass_comp["struvite"]
        ) == pytest.approx(0.01165597, rel=1e-3)
        assert value(
            m.fs.struvite_product.properties[0].flow_mass_comp["phosphates"]
        ) == pytest.approx(0, abs=1e-6)

        # check two biosolid product flow
        assert value(
            m.fs.biosolid_product.properties[0].flow_mass_comp["H2O"]
        ) == pytest.approx(4.302064e-21, rel=1e-3)
        assert value(
            m.fs.biosolid_product.properties[0].flow_mass_comp["struvite"]
        ) == pytest.approx(0, abs=1e-6)
        assert value(
            m.fs.biosolid_product.properties[0].flow_mass_comp["phosphates"]
        ) == pytest.approx(0.000582799, rel=1e-3)

        # check two centrate flow
        assert value(
            m.fs.centrate.properties[0].flow_mass_comp["H2O"]
        ) == pytest.approx(35.0432861, rel=1e-3)
        assert value(
            m.fs.centrate.properties[0].flow_mass_comp["struvite"]
        ) == pytest.approx(0, abs=1e-6)
        assert value(
            m.fs.centrate.properties[0].flow_mass_comp["phosphates"]
        ) == pytest.approx(3.067361e-5, rel=1e-3)

    @pytest.mark.component
    def test_costing(self, system_frame):
        m = system_frame

        add_costing(m)
        m.fs.costing.initialize()
        results = solve(m)

        assert_optimal_termination(results)

        # check costing
        assert value(m.fs.costing.LCOW) == pytest.approx(
            0.017063757, rel=1e-3
        )  # in $/m**3
        assert value(m.fs.costing.LCOS) == pytest.approx(0.05131957, rel=1e-3)

    @pytest.mark.component
    def test_display(self, system_frame):
        m = system_frame
        display_results(m)
        display_costing(m)
